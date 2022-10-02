import time
import bme680
from machine import Pin
from i2c import I2CAdapter

i2c_dev = I2CAdapter(1, scl=Pin(3), sda=Pin(2), freq=100000)
sensor = bme680.BME680(i2c_device=i2c_dev)

# These oversampling settings can be tweaked to
# change the balance between accuracy and noise in
# the data.
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

while True:
    if sensor.get_sensor_data():
        timestamp = time.localtime()
        
        print("--- BME680 data at %d-%d-%d %d:%d:%d ---" % (
            timestamp[0],
            timestamp[1],
            timestamp[2],
            timestamp[3],
            timestamp[4],
            timestamp[5]))
        print("Temp: %0.2f C" % sensor.data.temperature)
        print("Pres: %0.2f hPa" % sensor.data.pressure)
        print("Humi: %0.3f %%RH" % sensor.data.humidity)
        print("GasR: %d ohm" % sensor.data.gas_resistance)
        print()

        time.sleep(5)

