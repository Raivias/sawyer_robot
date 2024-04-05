set(CMAKE_CXX_STANDARD 14)
cmake_minimum_required(VERSION 3.3)

project(sawyer_description)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

ament_package()


# TODO need to insall xacros into shared directory
foreach(dir config launch meshes params urdf)
   install(DIRECTORY ${dir}/
      DESTINATION share/${PROJECT_NAME})
endforeach(dir)
