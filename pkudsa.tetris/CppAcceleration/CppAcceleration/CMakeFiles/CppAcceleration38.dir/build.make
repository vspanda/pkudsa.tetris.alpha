# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

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
CMAKE_SOURCE_DIR = /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration

# Include any dependencies generated for this target.
include CMakeFiles/CppAcceleration38.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/CppAcceleration38.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/CppAcceleration38.dir/flags.make

CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o: CMakeFiles/CppAcceleration38.dir/flags.make
CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o: GetAllValidPositions.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o -c /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/GetAllValidPositions.cpp

CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/GetAllValidPositions.cpp > CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.i

CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/GetAllValidPositions.cpp -o CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.s

CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.requires:

.PHONY : CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.requires

CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.provides: CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.requires
	$(MAKE) -f CMakeFiles/CppAcceleration38.dir/build.make CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.provides.build
.PHONY : CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.provides

CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.provides.build: CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o


# Object files for target CppAcceleration38
CppAcceleration38_OBJECTS = \
"CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o"

# External object files for target CppAcceleration38
CppAcceleration38_EXTERNAL_OBJECTS =

CppAcceleration38.cpython-38-x86_64-linux-gnu.so: CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o
CppAcceleration38.cpython-38-x86_64-linux-gnu.so: CMakeFiles/CppAcceleration38.dir/build.make
CppAcceleration38.cpython-38-x86_64-linux-gnu.so: CMakeFiles/CppAcceleration38.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared module CppAcceleration38.cpython-38-x86_64-linux-gnu.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/CppAcceleration38.dir/link.txt --verbose=$(VERBOSE)
	/usr/bin/strip /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/CppAcceleration38.cpython-38-x86_64-linux-gnu.so

# Rule to build all files generated by this target.
CMakeFiles/CppAcceleration38.dir/build: CppAcceleration38.cpython-38-x86_64-linux-gnu.so

.PHONY : CMakeFiles/CppAcceleration38.dir/build

CMakeFiles/CppAcceleration38.dir/requires: CMakeFiles/CppAcceleration38.dir/GetAllValidPositions.cpp.o.requires

.PHONY : CMakeFiles/CppAcceleration38.dir/requires

CMakeFiles/CppAcceleration38.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/CppAcceleration38.dir/cmake_clean.cmake
.PHONY : CMakeFiles/CppAcceleration38.dir/clean

CMakeFiles/CppAcceleration38.dir/depend:
	cd /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration /home/lab409/pkudsa.tetris/CppAcceleration/CppAcceleration/CMakeFiles/CppAcceleration38.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/CppAcceleration38.dir/depend

