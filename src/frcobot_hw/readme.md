# 快速开始

1. 首先将 `frcobot_hw` 功能包复制到 ROS 用户工作空间的 `src` 文件夹下，一般路径是：`~/catkin_ws/src`

2. 编译用户空间，在终端执行以下命令：

```bash
cd ~/catkin_ws/
catkin_make
```

3. 编译成功后，需要将 `lib` 文件夹下的文件复制到 `/opt/ros/melodic/lib` 路径下。一般命令如下：

```bash
sudo cp ~/catkin_ws/src/frcobot_cpp_sdk_demo/lib/lib* /opt/ros/melodic/lib
```

4. 可以执行以下命令运行机器人命令示例，将机器人从手动模式切换到自动模式：

```bash
rosrun frcobot_hw frcobot_cmd_demo
```

5. 可以执行以下命令运行机器人状态反馈节点：

```bash
roslaunch frcobot_hw frcobot_hw.launch
```

6. 你可以执行以下命令打印并查看机器人状态反馈信息：

```bash
rostopic echo /frcobot_status
```

7. 有关机器人 SDK 指令的具体使用说明，请参考《ROS C++ SDK 用户手册》。