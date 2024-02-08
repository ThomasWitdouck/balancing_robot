## Pico W

1.  To build code, run the following commands in terminal:

        cd ~/balancing_robot/pico
        mkdir build
        cd build
        cmake -DPICO_BOARD=pico_w -DWIFI_SSID="Your Network" -DWIFI_PASSWORD="Your Password" ..
        make


2.  To open minicom for serial communication, run the following command in terminal:

        sudo minicom -b 115200 -o -D /dev/ttyACM0
    
    To exit, press ctrl-A followed by Z.

