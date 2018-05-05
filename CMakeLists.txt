cmake_minimum_required(VERSION 2.8)
project(fast)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

add_definitions(-DCLION=1)

set(SOURCE_FILES
    a.cpp)

add_executable(fast ${SOURCE_FILES})
