#아날로그 신호를 전달하는 센서이므로 ADC를 연결해 줘야한다
#라즈베리파이는 아날로그 신호를 처리하지 못함
import RPi.GPIO as GPIO
import spidev #sudo pip install spidev
import time

GPIO.setwarnings(False)
GPIO.setmode(GPOI.BCM)
pin = 23
GPIO.setup(pin, GPIO.IN)
spi = spidev.SpiDev() #spi객체 생성
spi.open(0,0) #spi의 버스의 cs(Chip Select) 0신호선을 사용 
def read_spi_adc(channel): #mcp3008에서 아날로그 센서값을 받는 코드
    adcvalue = 0
    buff = spi.xfer2([1,(8+channel)<<4,0])
    adcvalue = ((buff[1]&3)<<8)+buff[2]
    return adcvalue
while True:
    adcvalue = read_spi_adc(1) #채널 1번의 아날로그 센서값을 받아옴
    print("수분 : %d"%(adcvalue))
    time.sleep(1)

#화분에 물을 뿌리면 값이 낮아진다.