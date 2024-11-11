#!/usr/bin/env python
import rospy
import pandas as pd
from fr5_moveit_config.srv import GoToPose  # 替换为你的包名

def call_go_to_pose(pose):
    rospy.wait_for_service('/GoToPose')
    try:
        go_to_pose = rospy.ServiceProxy('/GoToPose', GoToPose)
        # 将字典解包为关键字参数
        response = go_to_pose(**pose)  # 使用**运算符解包字典
        return response
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed: %s" % e)


def main():
    rospy.init_node('trajectory_client', anonymous=True)

    # 读取 CSV 文件
    df = pd.read_csv('/home/song/Frcobot_ROS_WS/data/trajectory_output.csv', header=None)

    for index, row in df.iterrows():
        # 提取位置和方向
        p_x, p_y, p_z = row[0:3]
        o_x, o_y, o_z, o_w = row[3:7]

        pose = {
            'p_x': p_x,
            'p_y': p_y,
            'p_z': p_z,
            'o_x': o_x,
            'o_y': o_y,
            'o_z': o_z,
            'o_w': o_w
        }

        # 调用服务
        response = call_go_to_pose(pose)
        rospy.loginfo(f"Response: {response}")

        # 可以添加延时以避免过快发布
        rospy.sleep(0.1)  # 根据需要调整时间

if __name__ == "__main__":
    main()
