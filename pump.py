import RPi.GPIO as GPIO
import time
import spidev
A1A = 5
A1B = 6
hum_threshold = 20
hum_max=0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(A1A, GPIO.OUT)
GPIO.setup(A1B, GPIO.OUT)
GPIO.output(A1A,GPIO.LOW)
GPIO.output(A1B,GPIO.LOW)
spi = spidev.SpiDev()
spi.open(0,0)
def read_spi(adcChannel):
    adcvalue=0
    buff = spi.xfer2([1,(8+channel)<<4,0])
    adcvalue = ((buff[1]&3)<<8)+buff[2]
    return adcvalue
def map(value,min_adc,max_adc,min_hum,max_hum):
    adc_range = max_adc-min_adc
    hum_range = max_hum - min_hum
    scale_factor = float(adc_range)/float(hum_range)
    return min_hum+((value-min_adc)/scale_factor)
try:
    adcChannel = 0
    while True:
        adcvalue=read_spi(adcChannel)
        hum = 100-int(map(adcvalue,hum_max,1023,0,100))
        if hum < hum_threshold:
            GPIO.output(A1A,GPIO.HIGH)
            GPIO.output(A1B,GPIO.LOW)
        else:
            GPIO.output(A1A,GPIO.LOW)
            GPIO.output(A1B,GPIO.LOW)
        time.sleep(0.5)
finally:
    GPIO.cleanup()
    spi.close()