#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import sys
import moveit_commander
from scipy.spatial.transform import Rotation as R
import numpy as np
import copy

class MoveGroupDemo(object):
    def __init__(self):
        super(MoveGroupDemo, self).__init__()

        # 初始化moveit_commander API和rospy节点
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('demo', anonymous=True)

        # 初始化机器人控制对象
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.move_group = moveit_commander.MoveGroupCommander("fr5_arm")

        # We can get the name of the reference frame for this robot:
        planning_frame = self.move_group.get_planning_frame()
        rospy.loginfo("Planning frame: %s" % planning_frame)

        # We can also set the end-effector link for this group:
        # self.move_group.set_end_effector_link("tool_Link")
        eef_link = self.move_group.get_end_effector_link()
        rospy.loginfo("End effector link: %s" % eef_link)

        # We can get a list of all the groups in the robot:
        group_names = self.robot.get_group_names()
        print("[INFO]: Available Planning Groups:", self.robot.get_group_names())

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

    def plan_cartesian_path(self, radius=0.1, num_points=100):
        """Generate a circle path with a given radius and center."""
        move_group = self.move_group

        # 假设初始位置和目标位置已知，末端执行器的姿态随着路径变化
        waypoints = []
        current_pose = move_group.get_current_pose().pose

        # 设置中心点
        center_x = current_pose.position.x
        center_y = current_pose.position.y
        center_z = current_pose.position.z
        # 构建路径点 1/4 圆
        for angle in np.linspace(1.5 * np.pi, 2.5 * np.pi, num_points):  # num_points 可调节平滑度
            next_pose = copy.deepcopy(current_pose)
            next_pose.position.x = radius * np.cos(angle) + center_x
            next_pose.position.y = radius * np.sin(angle) + center_y
            next_pose.position.z = center_z # Keep z constant (planar circle)
            
            # 在这里根据需要调整姿态，旋转角度可以是随位置变化的
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
        (plan, fraction) = move_group.compute_cartesian_path(
                waypoints, 0.01  # waypoints to follow  # eef_step
        )
        
        # Note: We are just planning, not asking move_group to actually move the robot yet:
        return plan, fraction, waypoints
    
    def execute_plan(self, plan, fraction, waypoints, retry_threshold=0.95, max_retries=5):
        move_group = self.move_group
        retries = 0
        eef_step = 0.01  # 初始步长

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


def normal_vector_to_quaternion(nx, ny, nz):
    # 将输入法向量归一化
    normal_vector = np.array([nx, ny, nz])
    normal_vector = normal_vector / np.linalg.norm(normal_vector)
    
    # 计算x轴：与法向量叉乘，如果结果为零向量则手动指定
    x_axis = np.cross([0, 0, 1], normal_vector)
    if np.allclose(x_axis, 0):  # 若为零向量
        x_axis = np.array([1, 0, 0])  # 选择默认x轴方向
    else:
        x_axis /= np.linalg.norm(x_axis)  # 归一化x轴
    
    # 根据 x 和 z 轴计算 y 轴
    y_axis = np.cross(normal_vector, x_axis)
    
    # 形成旋转矩阵
    rotation_matrix = np.column_stack((x_axis, y_axis, normal_vector))
    
    # 转换为四元数
    r = R.from_matrix(rotation_matrix)
    quaternion = r.as_quat()  # [qx, qy, qz, qw]
    
    return quaternion

def main():
    try:
        move_group = MoveGroupDemo()
        move_group.publish_end_effector_position()  # 使用 move_group 发布节点当前位置

        # 规划路径，生成轨迹点
        cartesian_plan, fraction, waypoints = move_group.plan_cartesian_path()
        rospy.loginfo("Trajectory planning completed, waiting for execution...")

        # 执行路径规划
        move_group.execute_plan(cartesian_plan, fraction, waypoints)
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()