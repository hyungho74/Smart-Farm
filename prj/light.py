import spidev, time #sudo pip install spidev
import RPi.GPIO as GPIO
GPIO.setwarnings(False) #GPIO핀 초기화
GPIO.setmode(GPIO.BCM) 
pin = 18
GPIO.setup(pin, GPIO.OUT)
spi = spidev.SpiDev() #spi객체 생성
spi.open(0,0) #spi의 버스의 cs(Chip Select) 0신호선을 사용

def analog_read(channel): #mcp3008에서 아날로그 센서값을 받는 코드
        r = spi.xfer2([1,(8+channel)<<4,0])
        adcout = ((r[1]&3)<<8)+r[2]
        return adcout

def lightsensor():
        reading = analog_read(2) #채널 2번의 아날로그 값을 받아옴
        return reading

def led():
        light = lightsensor()
        if(light > 100):
                GPIO.output(pin, GPIO.LOW)
        else:
                GPIO.output(pin, GPIO.HIGH)

