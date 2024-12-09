#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moveit_utils.my_move_group import MyMoveGroup
import rospy

def main():
    try:
        move_group = MyMoveGroup()
        move_group.publish_end_effector_position() # 使用 move_group 发布节点当前位置
        # 移动到目标关节位置
        # move_group.go_to_joint_state(-60, -90, 90, -90, -90, 0)
        rospy.loginfo("Successfully moved to the target joint position!")
        
        # 移动到目标笛卡尔位置
        """
        标定点
        Pose1 = [-0.259460, 0.235622, 0.203999, -0.560821, -0.283926, -0.741393, 0.234952]
        Pose2 = [-0.284597, 0.259721, 0.209166, -0.561096, -0.283910, -0.741234, 0.234815]
        Pose3 = [-0.260874, 0.310148, 0.217003, -0.561061, -0.284033, -0.741253, 0.234691]
        Pose4 = [-0.338501, 0.395071, 0.198626, -0.561047, -0.283989, -0.741283, 0.234683]
        Pose5 = [-0.361279, 0.370388, 0.180740, -0.599728, -0.296132, -0.710316, 0.219280]
        Pose6 = [-0.322214, 0.316445, 0.271448, -0.599774, -0.296239, -0.710229, 0.219290]
        """
        Circle_Top = [-0.3852566, 0.3790312, 0.1700710, -1, 0, 0, 0]
        move_group.go_to_pose_goal(*Circle_Top)

        rospy.loginfo("Successfully moved to the target position!")

        # 规划路径，生成轨迹点 -171.2869333	561.8196902	1.120466667
        target_point = [-0.17128, -0.561819, 0.1700710] # z 轴坐标使用的是 Circle_Top 坐标
        # cartesian_plan, fraction, waypoints = move_group.plan_cartesian_path_line(target_point)
        # cartesian_plan, fraction, waypoints = move_group.plan_cartesian_path()
        rospy.loginfo("Trajectory planning completed, waiting for execution...")

        # 执行路径规划
        # move_group.execute_plan(cartesian_plan, fraction, waypoints)

    except Exception as e:
        rospy.logerr(f"Exception: {e}")

if __name__ == '__main__':
    main()
