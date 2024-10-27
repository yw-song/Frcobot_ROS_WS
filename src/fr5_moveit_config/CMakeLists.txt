cmake_minimum_required(VERSION 3.1.3)
project(fr5_moveit_config)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(PROGRAMS
  scripts/move_group_test.py
  scripts/joint_motion.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
