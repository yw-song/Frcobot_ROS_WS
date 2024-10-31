#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from fr5_moveit_config.srv import GoToPose, GoToPoseResponse  # 替换为你的包名

class MoveGroupTest(object):
    def __init__(self):
        super(MoveGroupTest, self).__init__()

        # 初始化moveit_commander API和rospy节点
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('pose_service', anonymous=True)

        # 初始化机器人控制对象
        self.robot = moveit_commander.RobotCommander()
        self.move_group = moveit_commander.MoveGroupCommander("fr5_arm")

        # 定义定时器，用于定期输出末端执行器位置
        self.timer = rospy.Timer(rospy.Duration(5), self.publish_end_effector_position)

    def publish_end_effector_position(self, event):
        # 获取末端执行器的当前位置
        current_pose = self.move_group.get_current_pose().pose
        current_orientation = current_pose.orientation  # 提取当前的四元数
        rospy.loginfo("当前末端执行器位置: x=%f, y=%f, z=%f",
                      current_pose.position.x,
                      current_pose.position.y,
                      current_pose.position.z)
        rospy.loginfo("当前末端执行器位置: x=%f, y=%f, z=%f, w=%f",
                      current_orientation.orientation.x,
                      current_orientation.orientation.y,
                      current_orientation.orientation.z,
                      current_orientation.orientation.w)

    def go_to_pose_goal(self, x, y, z):
        # 设置并执行末端目标姿态
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = 0.0
        pose_goal.orientation.z = 1.0
        pose_goal.position.x = x
        pose_goal.position.y = y
        pose_goal.position.z = z

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
    rospy.loginfo("接收到请求: x=%f, y=%f, z=%f", req.x, req.y, req.z)
    success = move_group_test.go_to_pose_goal(req.x, req.y, req.z)
    return GoToPoseResponse(success)


def pose_service_server():
    global move_group_test
    move_group_test = MoveGroupTest()  # 仅初始化一次
    rospy.Service('GoToPose', GoToPose, handle_go_to_pose)
    rospy.loginfo("服务已启动，等待请求...")
    rospy.spin()

if __name__ == "__main__":
    pose_service_server()
