import machine
from machine import RTC, Pin, SPI
from machine import UART
import network
import os
import utime
import ntptime
import config
import ubinascii
import dht
import sds011


WIFI_ssid = config.wifi_config['ssid']
WIFI_pwd = config.wifi_config['password']
Device_ID = config.device_config['device_id']
Device_Room = config.device_config['device_room']

# Indoor
sensor = dht.DHT22(machine.Pin(14))

# Dust Sensor
# initialize a UART object (here P21 in TX and P22 is RX):
uart = UART(1, baudrate=9600, tx=21, rx=22)
dust_sensor = sds011.SDS011(uart)
# Datasheet says to wait for at least 30 seconds...
utime.sleep(30)

led_pin = machine.Pin(config.device_config['led_pin'], Pin.OUT) #built-in LED pin

def on_message(topic, message):
    print((topic,message))

def connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(WIFI_ssid, WIFI_pwd)
        while not sta_if.isconnected():
            print('.', end = '')
            pass
    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print('mac:', mac)
    print('network config:', sta_if.ifconfig())

def set_time():
    ntptime.settime()
    tm = utime.localtime()
    tm = tm[0:3] + (0,) + tm[3:6] + (0,)
    machine.RTC().datetime(tm)
    print('current time: {}'.format(utime.localtime()))


connect()
set_time()

rtc = machine.RTC()
utc_shift = 7
(year, month, mday, week_of_year, hour, minute, second, milisecond) = rtc.datetime()
rtc.init((year, month, mday, week_of_year, hour + utc_shift, minute, second, milisecond))

def main():
    while(True):

        try:
            #Returns NOK if no measurement found in reasonable time
            status = dust_sensor.read()
            #Returns NOK if checksum failed
            pkt_status = dust_sensor.packet_status

            # Stop fan
            # dust_sensor.sleep()

            if(status == False):
                print('Measurement failed.')
                pm25 = 'n/a'
                pm10 = 'n/a' 
            elif(pkt_status == False):
                print('Received corrupted data.')
                pm25 = 'n/a'
                pm10 = 'n/a' 
            else:
                pm25 = dust_sensor.pm25
                pm10 = dust_sensor.pm10
        except:
            pm25 = 'n/a'
            pm10 = 'n/a' 


        try:
            led_pin.value(1)
            sensor.measure()
            inTemp = sensor.temperature()
            inHum = sensor.humidity()
        except:
            inTemp = 'n/a'
            inHum = 'n/a'
        
        t = rtc.datetime()
        now = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(t[0], t[1], t[2], t[4], t[5], t[6])

        line = now + ", " + str(inTemp) + ", " + str(inHum) + ", " + str(pm25) + ", " + str(pm10) + "\n"
        print(line)
        led_pin.value(0)
        utime.sleep(1)  # Delay for 1 seconds.

try:
    
    t = rtc.datetime()
    main()

except OSError as e:
    print('Failed ...', e)
    utime.sleep(5)
    machine.reset()