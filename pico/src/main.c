#include <stdio.h>
#include "pico/stdlib.h"
#include "pico/cyw43_arch.h"
#include "hardware/adc.h"
#include "pico/multicore.h"


#include "server/pico_server.h"






//Two threads:
//
// 0. Control thread:
//      - Process data
//      - Drive motors
//
// 1. Communication thread:
//      - Read data from imu
//      - Send data to pc over wifi
//      - Receive data from pc over wifi

//function to be called on core0
void control_thread(){



}

//function to be called on core1
void communication_thread(){

    //wifi network name and password
    char ssid[] = "Proximus-Home-770867";
    char pass[] = "werx6sh2n4yjzxzw";

    //Constants and variables for temperature reading
    const float temp_conversion_rate = 3.3f / (1<<12);
    uint16_t temp_raw;
    float temp_voltage;
    float temp;
    
    //Configure ADC for temperature readings.
    adc_init();
    adc_set_temp_sensor_enabled(true);
    adc_select_input(4);

    //Connect to the wifi network.
    if (cyw43_arch_init()) {
        printf("Wifi init failed.");
        return;
    }

    printf("Wifi initialised.\n");
        
    cyw43_arch_enable_sta_mode();

    while (cyw43_arch_wifi_connect_timeout_ms(ssid, pass, CYW43_AUTH_WPA2_AES_PSK, 10000)) {
        printf("Failed to connect.\n");
        cyw43_arch_deinit();
        cyw43_arch_init();
        cyw43_arch_enable_sta_mode();

    }
    
    
    printf("Connected to wifi.\n");
    

    TCP_SERVER_T* state = tcp_server_init();

    

    //loop
    while (true) {

        //Read and convert temperature.
        temp_raw = adc_read();
        temp_voltage = temp_raw * temp_conversion_rate;
        temp = 27 - (temp_voltage - 0.706)/0.001721;
        printf("Pico temperature: %f degrees Celsius.\n", temp);

        //Turn LED on and off
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 1);
        printf("LED on.\n");
        sleep_ms(1000);
        cyw43_arch_gpio_put(CYW43_WL_GPIO_LED_PIN, 0);
        printf("LED off.\n");
        sleep_ms(1000);


        //Start server if it is offline.
        if (!state->running)
        {
            run_tcp_server(state);
        }
        

    }
    
}


int main() {
    stdio_init_all();

    communication_thread();

}