# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/song/frcobot_ros/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/song/frcobot_ros/build

# Include any dependencies generated for this target.
include frcobot_camera/CMakeFiles/binpicking.dir/depend.make

# Include the progress variables for this target.
include frcobot_camera/CMakeFiles/binpicking.dir/progress.make

# Include the compile flags for this target's objects.
include frcobot_camera/CMakeFiles/binpicking.dir/flags.make

frcobot_camera/CMakeFiles/binpicking.dir/src/binPicking.cpp.o: frcobot_camera/CMakeFiles/binpicking.dir/flags.make
frcobot_camera/CMakeFiles/binpicking.dir/src/binPicking.cpp.o: /home/song/frcobot_ros/src/frcobot_camera/src/binPicking.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/song/frcobot_ros/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object frcobot_camera/CMakeFiles/binpicking.dir/src/binPicking.cpp.o"
	cd /home/song/frcobot_ros/build/frcobot_camera && /usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/binpicking.dir/src/binPicking.cpp.o -c /home/song/frcobot_ros/src/frcobot_camera/src/binPicking.cpp

frcobot_camera/CMakeFiles/binpicking.dir/src/binPicking.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/binpicking.dir/src/binPicking.cpp.i"
	cd /home/song/frcobot_ros/build/frcobot_camera && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/song/frcobot_ros/src/frcobot_camera/src/binPicking.cpp > CMakeFiles/binpicking.dir/src/binPicking.cpp.i

frcobot_camera/CMakeFiles/binpicking.dir/src/binPicking.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/binpicking.dir/src/binPicking.cpp.s"
	cd /home/song/frcobot_ros/build/frcobot_camera && /usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/song/frcobot_ros/src/frcobot_camera/src/binPicking.cpp -o CMakeFiles/binpicking.dir/src/binPicking.cpp.s

# Object files for target binpicking
binpicking_OBJECTS = \
"CMakeFiles/binpicking.dir/src/binPicking.cpp.o"

# External object files for target binpicking
binpicking_EXTERNAL_OBJECTS =

/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: frcobot_camera/CMakeFiles/binpicking.dir/src/binPicking.cpp.o
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: frcobot_camera/CMakeFiles/binpicking.dir/build.make
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/libroscpp.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libpthread.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libboost_chrono.so.1.71.0
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libboost_filesystem.so.1.71.0
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/librosconsole.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/librosconsole_log4cxx.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/librosconsole_backend_interface.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/liblog4cxx.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libboost_regex.so.1.71.0
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/libxmlrpcpp.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/libroscpp_serialization.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/librostime.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libboost_date_time.so.1.71.0
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /opt/ros/noetic/lib/libcpp_common.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libboost_system.so.1.71.0
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libboost_thread.so.1.71.0
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /usr/lib/x86_64-linux-gnu/libconsole_bridge.so.0.4
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/librobotAPI.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/libxmlrpc.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/libxmlrpc_client.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/libxmlrpc_util.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/libxmlrpc_xmlparse.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/libxmlrpc_xmltok.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: /home/song/frcobot_ros/src/frcobot_camera/lib/libz.so
/home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking: frcobot_camera/CMakeFiles/binpicking.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/song/frcobot_ros/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable /home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking"
	cd /home/song/frcobot_ros/build/frcobot_camera && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/binpicking.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
frcobot_camera/CMakeFiles/binpicking.dir/build: /home/song/frcobot_ros/devel/lib/frcobot_camera/binpicking

.PHONY : frcobot_camera/CMakeFiles/binpicking.dir/build

frcobot_camera/CMakeFiles/binpicking.dir/clean:
	cd /home/song/frcobot_ros/build/frcobot_camera && $(CMAKE_COMMAND) -P CMakeFiles/binpicking.dir/cmake_clean.cmake
.PHONY : frcobot_camera/CMakeFiles/binpicking.dir/clean

frcobot_camera/CMakeFiles/binpicking.dir/depend:
	cd /home/song/frcobot_ros/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/song/frcobot_ros/src /home/song/frcobot_ros/src/frcobot_camera /home/song/frcobot_ros/build /home/song/frcobot_ros/build/frcobot_camera /home/song/frcobot_ros/build/frcobot_camera/CMakeFiles/binpicking.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : frcobot_camera/CMakeFiles/binpicking.dir/depend

