#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import csv
from fr5_moveit_config.srv import GoToPose

def read_csv(file_path):
    """
    读取 CSV 文件，返回文件中的所有点坐标。
    每一行应该包含一个点的 XYZ 坐标。
    """
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        points = [list(map(float, row)) for row in reader]
    return points

def calculate_point_top(p1b, p1c, topc):
    """
    计算目标点 'PointTop' 的坐标。
    通过计算相机坐标系下两点的差异并加上已知基底坐标系下的 P1 点，得到基底坐标系下的 PointTop 坐标。
    """
    # 计算两点坐标差异 ΔP
    delta_p = [topc[i] - p1c[i] for i in range(3)]
    
    # 计算 PointTop 坐标
    point_top = [p1b[i] + delta_p[i] for i in range(3)]
    return point_top

def send_to_service(point_top):
    """
    通过 ROS 服务将计算出的 PointTop 坐标发送到 `/GoToPose` 服务。
    假设姿态（orientation）为单位四元数 (0, 0, 0, 1)，即无旋转。
    """
    rospy.wait_for_service('/GoToPose')  # 等待服务准备好
    try:
        # 创建服务代理，调用 /GoToPose 服务
        go_to_pose = rospy.ServiceProxy('/GoToPose', GoToPose)
        
        # 发送目标点坐标（PointTop）和姿态信息
        response = go_to_pose(point_top[0]*0.001, point_top[1]*0.001, point_top[2]*0.001, -1, 0, 0, 0)
        
        # 输出服务返回的结果
        rospy.loginfo("Service Response: %s", response.success)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s", e)

def moveToTopServer():
    """
    ROS 节点入口函数。读取 CSV 文件，计算 PointTop 坐标，并发送到 GoToPose 服务。
    """
    rospy.init_node('moveToTopServer')  # 初始化 ROS 节点

    # 已知的基底坐标系下的 P1 坐标
    p1b = [0, 66, 0]

    # 从 CSV 文件读取相机坐标系下的点
    file_path = '/home/song/Frcobot_ROS_WS/data/trajectory_output.csv'
    points = read_csv(file_path)

    # 获取相机坐标系下的点 P1 和 top
    p1c = points[0]  # 第一个点 P1 在相机坐标系中的坐标
    topc = points[1]  # 第二个点 top 在相机坐标系中的坐标

    # 计算基底坐标系下的 PointTop 坐标
    point_top = calculate_point_top(p1b, p1c, topc)

    # 在参数服务器中添加 PointTop 坐标
    rospy.set_param("Top_x", point_top[0]*0.001)
    rospy.set_param("Top_y", point_top[1]*0.001)
    rospy.set_param("Top_z", point_top[2]*0.001)

    # 将 PointTop 坐标发送到 ROS 服务
    send_to_service(point_top)

if __name__ == '__main__':
    moveToTopServer()
