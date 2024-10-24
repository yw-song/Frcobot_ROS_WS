# ROS控制样板代码

简单的仿真接口和用于设置ros_control硬件接口的模板。该项目的想法是让你将其作为创建硬件接口的起点，因为[ros_control文档](http://wiki.ros.org/ros_control)较为稀缺。这个样板代码展示了以下内容：

- 为ros_control创建多个关节的hardware_interface
- 位置轨迹控制器
- 控制2个关节的简单机器人“FrRobot”（如下图所示）
- 使用roslaunch和yaml文件加载配置
- 生成随机轨迹并通过actionlib接口发送
- 部分支持关节模式切换（需要改进）
- 关节限制
- 非基于物理的机器人模拟器
- 在Rviz中的可视化

<img src="https://picknik.ai/assets/images/logo.jpg" width="120">

该开源项目由[PickNik Robotics](https://picknik.ai/)开发。如果需要专业的ROS开发和咨询服务，请联系projects@picknik.ai获取免费咨询。

## 维护者

特别感谢以下该仓库的维护者：

- Dave Coleman (@davetcoleman)
- Andy Zelenak (@AndyZe)
- John Morris (@zultron)
- Robert Wilbrandt (@RobertWilbrandt)

## 状态：

* [![Build Status](https://travis-ci.org/PickNikRobotics/ros_control_boilerplate.svg?branch=melodic-devel)](https://travis-ci.org/PickNikRobotics/ros_control_boilerplate) Travis CI
* [![Devel Job Status](http://build.ros.org/buildStatus/icon?job=Mdev__ros_control_boilerplate__ubuntu_bionic_amd64)](http://build.ros.org/job/Mdev__ros_control_boilerplate__ubuntu_bionic_amd64/) 开发状态
* [![Build Status](http://build.ros.org/buildStatus/icon?job=Mbin_uB64__ros_control_boilerplate__ubuntu_bionic_amd64__binary)](http://build.ros.org/job/Mbin_uB64__ros_control_boilerplate__ubuntu_bionic_amd64__binary/) AMD64 Debian构建状态

<img src="https://raw.githubusercontent.com/davetcoleman/ros_control_boilerplate/jade-devel/resources/screenshot.png"/>

## 视频演示

请参见[YouTube](https://www.youtube.com/watch?v=Tpj2tx9uZ-o)的简短视频演示。

## 安装

该包依赖于[gazebo_ros_demos](https://github.com/ros-simulation/gazebo_ros_demos)的``frrobot_description``包，你需要将其从源码添加到你的catkin工作空间：

    git clone https://github.com/ros-simulation/gazebo_ros_demos.git

然后，可以从源码安装本包进行开发，或者从debian安装：

    sudo apt-get install ros-indigo-ros-control-boilerplate

## 运行仿真演示

此包设置了“FrRobot”两关节机器人演示。此“模板包”位于ros_control_boilerplate中的一个子文件夹，可以轻松重命名和重用。要运行其基于ros_control的非物理模拟硬件接口，请运行：

    roslaunch ros_control_boilerplate frrobot_simulation.launch

要在Rviz中可视化其发布的``/tf``坐标变换，请运行：

    roslaunch ros_control_boilerplate frrobot_visualize.launch

要发送一个随机的虚拟轨迹执行，请运行：

    roslaunch ros_control_boilerplate frrobot_test_trajectory.launch

## 自定义

要将此作为你的机器人的仿真接口进行测试，可以使用以下命令快速将子文件夹包重命名为你的机器人名称：

```
function findreplace() {
    grep -lr -e "$1" * | xargs sed -i "s/$1/$2/g" ;
}

function findreplacefilename() {
    find . -depth -name "*$1*" -exec bash -c 'for f; do base=${f##*/}; mv -- "$f" "${f%/*}/${base//'$1'/'$2'}"; done' _ {} +
}

findreplacefilename frrobot myrobot
findreplace frrobot myrobot
findreplace FrRobot MyRobot
findreplace FRROBOT MYROBOT
```

然后在``myrobot_hw_interface.cpp``文件中添加必要的代码，通过USB/串口/以太网等与机器人通信。

## 设置初始位置，配合MoveIt!使用

如果需要让你的机器人在仿真中以特定位置启动，或者想使用此功能配合MoveIt!进行仿真，请参见依赖于此包的下游包[moveit_sim_controller](https://github.com/davetcoleman/moveit_sim_controller)

## 其他工具

### 录制到CSV

将来自轨迹控制器的命令写入CSV文件：

    rosrun ros_control_boilerplate controller_to_csv SAVE_TO_FILE_PATH CONTROLLER_STATE_TOPIC TIME_TO_RECORD

### 从CSV命令

从CSV文件读取并在机器人上执行：

    rosrun ros_control_boilerplate csv_to_controller READ_FROM_FILE_PATH CONTROLLER_STATE_TOPIC TIME_TO_RECORD

### 从键盘命令

通过键盘进行关节级别的遥控（TODO: 删除硬编码的主题名称）：

    rosrun ros_control_boilerplate keyboard_teleop

## 限制

- 未实现急停、传输或ros_control中的其他高级功能
- 没有任何硬实时代码，这在很大取决于您的平台、内核、操作系统等
- 尽管有一些代码用于速度控制，但仅完全实现了位置控制

## 贡献

请添加功能、进行更正并解决上述限制，谢谢！