我现在在构思一个 `ROS` 中的 `Python` 脚本实现服务通信的客户端功能，具体来说他将实现以下功能：一个节点 A 向另一个节点B发送请求，B接收处理请求并产生响应结果返回给A。该脚本实现的是节点B的功能也就是作为服务通信的客户端。

A向B发送一个坐标点，这个坐标点包含了目标点的(x,y,z)坐标。在B文件中可以操控机械臂末端到达这个点，该函数为 `go_to_pose_goal`。成功后返回一个值。现在我自己写了一个小demo，仅仅实现了move功能但是不是ROS中的服务通信，你可以读懂我的代码然后在此基础上实现该功能。注意，注释用中文。

这是我的python代码：

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list


def all_close(goal, actual, tolerance):
    """
    检测实际值是否在目标值的公差范围内
    @param: goal       目标参数，浮点数列表、Pose类型或PoseStamped类型消息
    @param: actual     实际参数，浮点数列表、Pose类型或PoseStamped类型消息
    @param: tolerance  容忍范围，浮点数
    @returns: bool
    """
    if type(goal) is list:
        for index in range(len(goal)):
            if abs(actual[index] - goal[index]) > tolerance:
                return False

    elif type(goal) is geometry_msgs.msg.PoseStamped:
        return all_close(goal.pose, actual.pose, tolerance)

    elif type(goal) is geometry_msgs.msg.Pose:
        return all_close(pose_to_list(goal), pose_to_list(actual), tolerance)

    return True


class MoveGroupTest(object):
    """MoveGroupTest"""

    def __init__(self):
        super(MoveGroupTest, self).__init__()

        # 初始化moveit_commander API和rospy节点
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('move_group_test', anonymous=True)

        # 初始化机器人控制对象，提供机器人的运动学模型和当前关节状态等信息
        robot = moveit_commander.RobotCommander()

        # 初始化规划场景对象，提供机器人与周围环境的接口
        scene = moveit_commander.PlanningSceneInterface()

        # 初始化MoveGroupCommander对象，提供fr5机械臂的运动规划接口
        group_name = "fr5_arm"
        move_group = moveit_commander.MoveGroupCommander(group_name)

        # 创建一个ROS发布器用于在Rviz中显示轨迹信息
        display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                       moveit_msgs.msg.DisplayTrajectory,
                                                       queue_size=20)                                                   

        # 获取机器人参考坐标系
        planning_frame = move_group.get_planning_frame()
        print("============ 规划框架: %s ============" % planning_frame)

        # 获取当前规划组中机器人的末端执行器的链接名称
        eef_link = move_group.get_end_effector_link()
        print("============ 末端执行器链接: %s ============" % eef_link)

        # 获取机器人所有规划组的名称，并将其以数组形式输出
        group_names = robot.get_group_names()
        print("============ 可用的规划组: ============", robot.get_group_names())

        # 获取机器人的当前状态
        print("============ 打印机器人状态 ============")
        print(robot.get_current_state())
        print("")

        self.box_name = ''
        self.robot = robot
        self.scene = scene
        self.move_group = move_group
        self.display_trajectory_publisher = display_trajectory_publisher
        self.planning_frame = planning_frame
        self.eef_link = eef_link
        self.group_names = group_names

    def go_to_joint_state(self):
        # 设置并执行关节目标位置
        joint_goal = self.move_group.get_current_joint_values()
        print("============ 当前关节值: ============", joint_goal)
        joint_goal[0] = 0.873
        joint_goal[1] = -1.571
        joint_goal[2] = -1.571
        joint_goal[3] = -3.142
        joint_goal[4] = - 1.745
        joint_goal[5] = 0
        print("============ 目标关节值: ============", joint_goal)

        # 移动到关节目标位置
        self.move_group.go(joint_goal, wait=True)
        rospy.sleep(1)
        self.move_group.stop()

        # 测试：验证关节目标是否已实现
        current_joints = self.move_group.get_current_joint_values()
        return all_close(joint_goal, current_joints, 0.01)
    
    def go_to_pose_goal(self):
        # 设置并执行末端目标姿态
        pose_goal = geometry_msgs.msg.Pose()
        pose_goal.orientation.w = 1.0
        pose_goal.position.x = 0.4
        pose_goal.position.y = 0.1
        pose_goal.position.z = 0.4

        # 设置目标姿态
        self.move_group.set_pose_target(pose_goal)

        # 移动到目标姿态
        self.move_group.go(wait=True)
        rospy.sleep(1)
        self.move_group.stop()

        # 清除目标姿态
        self.move_group.clear_pose_targets()

        # 测试：验证姿态目标是否已实现
        current_pose = self.move_group.get_current_pose().pose
        return all_close(pose_goal, current_pose, 0.01)


def main():
    try:
        print("----------------------------------------------------------")
        print("-----------基于ROS和MoveIt的FR5机械臂控制演示程序-----------")
        print("----------------------------------------------------------")
        print("按Ctrl+D退出演示")
        print("")
        print("============ 按`Enter`键初始化moveit_commander以开始演示 ============")
        input()
        fr5demo = MoveGroupTest()

        print("============ 按`Enter`键以关节空间移动到末端目标姿态 ============")
        input()
        fr5demo.go_to_pose_goal()

        print("============ 演示完成！============")
    except rospy.ROSInterruptException:
        return
    except KeyboardInterrupt:
        return


if __name__ == '__main__':
    main()

```


现在的问题是这样的：我想让他到达某一个点是 0.4 0.1 0.4，也就是通过这个代码：
```bash
rosservice call /GoToPose 0.4 0.1 0.4
```
但是问题在于我机械臂到达这个点之后的姿态不太合适，因为我想在 `go_to_pose_goal` 函数里能不能加一个四元数的东西让他表达的好点
