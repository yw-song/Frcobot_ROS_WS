#!/usr/bin/env python
# -*- coding: utf-8 -*-
from moveit_utils.my_move_group import MyMoveGroup
import rospy

def main():
    try:
        move_group = MyMoveGroup()
        move_group.publish_end_effector_position() # 使用 move_group 发布节点当前位置
        # 移动到目标关节位置
        # move_group.go_to_joint_state(90, -45, -90, -90, 90, 0)
        # rospy.loginfo("Successfully moved to the target joint position!")
        
        # 移动到目标笛卡尔位置
        # move_group.go_to_pose_goal(0.4, 0.1, 0.4, 0.0, 0.0, 0.0, 1.0)
        # rospy.loginfo("Successfully moved to the target position!")

        # 规划路径，生成轨迹点
        cartesian_plan, fraction, waypoints = move_group.plan_cartesian_path()
        rospy.loginfo("Trajectory planning completed, waiting for execution...")

        # 执行路径规划
        move_group.execute_plan(cartesian_plan, fraction, waypoints)

    except Exception as e:
        rospy.logerr(f"Exception: {e}")

if __name__ == '__main__':
    main()
