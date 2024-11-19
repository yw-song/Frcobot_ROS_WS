#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moveit_utils.my_move_group import MyMoveGroup
import rospy

def main():
    try:
        move_group = MyMoveGroup()
        move_group.publish_end_effector_position() # 使用 move_group 发布节点当前位置
        
        # 移动到目标笛卡尔位置
        Pose1 = [-0.259460, 0.235622, 0.203999, -0.560821, -0.283926, -0.741393, 0.234952]
        Pose2 = [-0.284597, 0.259721, 0.209166, -0.561096, -0.283910, -0.741234, 0.234815]
        Pose3 = [-0.260874, 0.310148, 0.217003, -0.561061, -0.284033, -0.741253, 0.234691]
        Pose4 = [-0.338501, 0.395071, 0.198626, -0.561047, -0.283989, -0.741283, 0.234683]
        Pose5 = [-0.361279, 0.370388, 0.180740, -0.599728, -0.296132, -0.710316, 0.219280]
        Pose6 = [-0.322214, 0.316445, 0.271448, -0.599774, -0.296239, -0.710229, 0.219290]
        move_group.go_to_pose_goal(*Pose1)
        # move_group.go_to_pose_goal(*Pose2)
        # move_group.go_to_pose_goal(*Pose3)
        # move_group.go_to_pose_goal(*Pose4)
        # move_group.go_to_pose_goal(*Pose5)
        # move_group.go_to_pose_goal(*Pose6)

        rospy.loginfo("Successfully moved to the target position!")
    except Exception as e:
        rospy.logerr(f"Exception: {e}")

if __name__ == '__main__':
    main()
