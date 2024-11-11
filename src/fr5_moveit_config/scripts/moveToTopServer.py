#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import moveit_commander
import geometry_msgs.msg
from fr5_moveit_config.srv import GoToPose, GoToPoseResponse  # 替换为你的包名

class MoveGroup(object):
    def __init__(self):
        super(MoveGroup, self).__init__()

        # 初始化moveit_commander API和rospy节点
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('moveToTopServer', anonymous=True)

        # 初始化机器人控制对象
        self.robot = moveit_commander.RobotCommander()
        self.move_group = moveit_commander.MoveGroupCommander("fr5_arm")

    def publish_end_effector_position(self):
        # We can get the name of the reference frame for this robot:
        planning_frame = move_group.get_planning_frame()
        print("Planning frame: %s" % planning_frame)

        # We can also print the name of the end-effector link for this group:
        eef_link = move_group.get_end_effector_link()
        print("End effector link: %s" % eef_link)

        # We can get a list of all the groups in the robot:
        group_names = self.robot.get_group_names()
        print("Available Planning Groups:", self.robot.get_group_names())

        # 获取末端执行器的当前位置
        current_pose = self.move_group.get_current_pose().pose
        current_orientation = current_pose.orientation  # 提取当前的四元数
        rospy.loginfo("当前末端执行器位置: x=%f, y=%f, z=%f | 四元数位置：x=%f, y=%f, z=%f, w=%f",
                      current_pose.position.x,
                      current_pose.position.y,
                      current_pose.position.z,
                      current_orientation.x,
                      current_orientation.y,
                      current_orientation.z,
                      current_orientation.w)

    def go_to_pose_goal(self, p_x, p_y, p_z, o_x, o_y, o_z, o_w):
        # 设置并执行末端目标姿态
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.position.x = p_x
        pose_goal.position.y = p_y
        pose_goal.position.z = p_z
        pose_goal.orientation.x = o_x
        pose_goal.orientation.y = o_y
        pose_goal.orientation.z = o_z
        pose_goal.orientation.w = o_w

        # 设置目标姿态
        self.move_group.set_pose_target(pose_goal)

        # 移动到目标姿态
        success = self.move_group.go(wait=True)
        rospy.sleep(1)
        self.move_group.stop()

        # 清除目标姿态
        self.move_group.clear_pose_targets()

        return success


def handle_go_to_pose(req):
    move_group.publish_end_effector_position()  # 使用 move_group 实例来调用
    rospy.loginfo("接收到请求: 末端坐标p_x=%f, p_y=%f, p_z=%f | 四元数坐标为o_x=%f,o_y=%f,o_z=%f,o_w=%f",
                  req.p_x, req.p_y, req.p_z, req.o_x, req.o_y, req.o_z, req.o_w)
    success = move_group.go_to_pose_goal(req.p_x, req.p_y, req.p_z, req.o_x, req.o_y, req.o_z, req.o_w)
    return GoToPoseResponse(success)


def main():
    global move_group
    move_group = MoveGroup()  # 仅初始化一次
    rospy.Service('GoToPose', GoToPose, handle_go_to_pose)
    rospy.loginfo("服务已启动，等待请求...")
    rospy.spin()

if __name__ == "__main__":
    main()
