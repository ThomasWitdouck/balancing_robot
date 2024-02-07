cmake_minimum_required(VERSION 3.13)
include(${CMAKE_CURRENT_SOURCE_DIR}/pico_sdk_import.cmake)

project(balancing_robot C CXX ASM)
set(CMAKE_C STANDARD 11)

pico_sdk_init()

set(INCLUDE_DIRS
  ${CMAKE_CURRENT_SOURCE_DIR}
  ${CMAKE_CURRENT_SOURCE_DIR}/include
)

include_directories(
	${INCLUDE_DIRS}
)

file(GLOB Sources
    "src/main.c"
    "src/pico_server/*.c"
)

add_executable(
    pico
    ${Sources}
)

pico_enable_stdio_usb(pico 1)
pico_enable_stdio_uart(pico 0)

target_link_libraries(pico
  pico_cyw43_arch_lwip_threadsafe_background
  pico_stdlib
  hardware_adc
  pico_multicore
)

pico_add_extra_outputs(pico)

target_include_directories(pico PRIVATE ${CMAKE_CURRENT_LIST_DIR})


