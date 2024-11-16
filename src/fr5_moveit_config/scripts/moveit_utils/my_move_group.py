#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import sys
import moveit_commander
import geometry_msgs.msg
import math
from moveit_commander.conversions import pose_to_list
from scipy.spatial.transform import Rotation as R
import numpy as np
import copy
from moveit_utils.utils import all_close, normal_vector_to_quaternion  # 引入工具函数


class MyMoveGroup(object):
    def __init__(self):
        super(MyMoveGroup, self).__init__()

        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_group_python_interface', anonymous=True)

        # 初始化机器人控制
        robot = moveit_commander.RobotCommander()
        scene = moveit_commander.PlanningSceneInterface()
        move_group = moveit_commander.MoveGroupCommander("fr5_arm")

        # 规划框架和末端连接
        planning_frame = move_group.get_planning_frame()
        move_group.set_end_effector_link("tool_Link")
        eef_link = move_group.get_end_effector_link()

        # 赋值为实例变量
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = robot.get_group_names()

    def publish_end_effector_position(self):
        # 获取末端执行器的当前位置
        current_pose = self.move_group.get_current_pose().pose
        current_orientation = current_pose.orientation  # 提取当前的四元数
        rospy.loginfo("Current Locatoin: x=%f, y=%f, z=%f",
                      current_pose.position.x,
                      current_pose.position.y,
                      current_pose.position.z,)
        rospy.loginfo("Current Posture: x=%f, y=%f, z=%f, w=%f", 
                      current_orientation.x,
                      current_orientation.y,
                      current_orientation.z,
                      current_orientation.w)

    def go_to_joint_state(self, joint1_angle, joint2_angle, joint3_angle, joint4_angle, joint5_angle, joint6_angle):
        joint_goal = self.move_group.get_current_joint_values()
        joint_goal[0] = math.radians(joint1_angle)
        joint_goal[1] = math.radians(joint2_angle)
        joint_goal[2] = math.radians(joint3_angle)
        joint_goal[3] = math.radians(joint4_angle)
        joint_goal[4] = math.radians(joint5_angle)
        joint_goal[5] = math.radians(joint6_angle)
        self.move_group.go(joint_goal, wait=True)
        rospy.sleep(1)
        self.move_group.stop()
        current_joints = self.move_group.get_current_joint_values()
        return all_close(joint_goal, current_joints, 0.01)

    def go_to_pose_goal(self, x, y, z, qx, qy, qz, qw):
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.position.x = x
        pose_goal.position.y = y
        pose_goal.position.z = z
        pose_goal.orientation.x = qx
        pose_goal.orientation.y = qy
        pose_goal.orientation.z = qz
        pose_goal.orientation.w = qw
        self.move_group.set_pose_target(pose_goal)
        self.move_group.go(wait=True)
        rospy.sleep(1)
        self.move_group.stop()
        self.move_group.clear_pose_targets()
        current_pose = self.move_group.get_current_pose().pose
        return all_close(pose_goal, current_pose, 0.01)

    def plan_cartesian_path(self, radius=0.1, num_points=100):
        move_group = self.move_group
        waypoints = []
        current_pose = move_group.get_current_pose().pose
        center_x = current_pose.position.x
        center_y = current_pose.position.y
        center_z = current_pose.position.z
        for angle in np.linspace(0, 2 * np.pi, num_points):
            next_pose = copy.deepcopy(current_pose)
            next_pose.position.x = radius * np.cos(angle) + center_x
            next_pose.position.y = radius * np.sin(angle) + center_y
            next_pose.position.z = center_z
            nx = 2 * 0.1424 * radius * np.cos(angle)
            ny = 2 * 0.1424 * radius * np.sin(angle)
            nz = -1
            quaternion = normal_vector_to_quaternion(nx, ny, nz)
            next_pose.orientation.x = quaternion[0]
            next_pose.orientation.y = quaternion[1]
            next_pose.orientation.z = quaternion[2]
            next_pose.orientation.w = quaternion[3]
            waypoints.append(copy.deepcopy(next_pose))
        waypoints.append(copy.deepcopy(current_pose))
        (plan, fraction) = move_group.compute_cartesian_path(waypoints, 0.01)
        return plan, fraction, waypoints

    # def execute_plan(self, plan, fraction, waypoints):
    #     self.move_group.execute(plan, wait=True)
    #     rospy.loginfo("Execution completed successfully!")

    def execute_plan(self, plan, fraction, waypoints, retry_threshold=0.95, max_retries=5):
        move_group = self.move_group
        retries = 0
        eef_step = 0.01  # 初始步长

        # 设置速度和加速度的缩放比例
        velocity_scaling = 0.5
        acceleration_scaling = 0.5
        move_group.set_max_velocity_scaling_factor(velocity_scaling)
        move_group.set_max_acceleration_scaling_factor(acceleration_scaling)

        # 如果 fraction 小于阈值，自动增加 eef_step 重试
        while fraction < retry_threshold and retries < max_retries:
            rospy.logwarn("Path fraction low (fraction=%.2f). Retrying with larger eef_step...", fraction)
            eef_step += 0.005  # 增加步长
            (plan, fraction) = move_group.compute_cartesian_path(
                waypoints, eef_step
            )
            retries += 1

        # 检查是否成功达到目标 fraction
        if fraction >= retry_threshold:
            rospy.loginfo("Path planning succeeded with fraction: %.2f. Executing...", fraction)
            move_group.execute(plan, wait=True)
            rospy.loginfo("Done successfully!")
        else:
            rospy.logerr("Failed to plan a complete path after %d retries (final fraction=%.2f)", retries, fraction)

