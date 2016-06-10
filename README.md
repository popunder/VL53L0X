# VL53L0X
Tools to interface ToF ranging sensor VL53L0X from ST Microelectronics.

From product page:
## World smallest Time-of-Flight \(ToF\) ranging sensor
The VL53L0X is a new generation Time-of-Flight \(ToF\) laser-ranging module housed in the smallest package on the market today, providing accurate distance measurement whatever the target reflectances unlike conventional technologies. It can measure absolute distances up to 2m, setting a new benchmark in ranging performance levels, opening the door to various new applications.

Started from C API provided with STSW-IMG005 <https://my.st.com/content/my_st_com/en/products/embedded-software/proximity-sensors-software/stsw-img005.html>

The VL53L0X breakout board \(called satellite\), can be found as a part of NUCLEO-53L0A1 evaluation package or separately \(53L0-SATEL-I1\) is connected to RPI GPIO interface
SDA, SCL, 3.3V and GND

Provided code is Python for Raspberry Pi.
Uses smbus library.
