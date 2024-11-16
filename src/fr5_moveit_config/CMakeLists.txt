cmake_minimum_required(VERSION 3.1.3)
project(fr5_moveit_config)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  moveit_ros_move_group
  moveit_fake_controller_manager
  moveit_kinematics
  moveit_planners_ompl
  moveit_commander
  moveit_ros_visualization
  moveit_setup_assistant
  moveit_simple_controller_manager
  geometry_msgs
  joint_state_publisher
  joint_state_publisher_gui
  robot_state_publisher
  rviz
  tf2_ros
  xacro
  # Add other required dependencies here
)

# 添加服务文件
add_service_files(
  FILES
  GoToPose.srv
)

# 生成消息和服务
generate_messages(
  DEPENDENCIES std_msgs  # 如果你的服务依赖于其他消息
)

catkin_package(
  CATKIN_DEPENDS rospy std_msgs  # 需要列出依赖的包
)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(PROGRAMS
  scripts/move_group_test.py
  scripts/joint_motion.py
  scripts/demo.py
  scripts/pose_client.py
  scripts/pose_service.py
  scripts/moveToTopServer.py
  scripts/moveToTopClient.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
