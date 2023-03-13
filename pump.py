import RPi.GPIO as GPIO
import time
import spidev
A1A = 5 #모터 드라이브(l9110s)의 A1-A의 핀
A1B = 6 #모터 드라이브(l9110s)의 A1-B의 핀
hum_max=0 #물에 담궜을때 측정 값
#핀 초기세팅
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(A1A, GPIO.OUT)
GPIO.setup(A1B, GPIO.OUT)
GPIO.output(A1A,GPIO.LOW)
GPIO.output(A1B,GPIO.LOW)
spi = spidev.SpiDev() #spi객체 생성
spi.open(0,0) #spi 버스의 cs(chip select) 0신호선 사용
def waterpump(hum_threshold):
    def read_spi(adcChannel): #아날로그 값을 받는 함수
        adcvalue=0
        buff = spi.xfer2([1,(8+channel)<<4,0])
        adcvalue = ((buff[1]&3)<<8)+buff[2]
        return adcvalue
    def map(value,min_adc,max_adc,min_hum,max_hum): #측정된 토양습도센서의 값을 100분율로 변환
        adc_range = max_adc-min_adc
        hum_range = max_hum - min_hum
        scale_factor = float(adc_range)/float(hum_range)
        return min_hum+((value-min_adc)/scale_factor)
    try:
        adcChannel = 0
        while True:
            adcvalue=read_spi(adcChannel)
            hum = 100-int(map(adcvalue,hum_max,1023,0,100))
            if hum < hum_threshold: #기준값보다 적다면 모터 작동
                GPIO.output(A1A,GPIO.HIGH)
                GPIO.output(A1B,GPIO.LOW)
            else:
                GPIO.output(A1A,GPIO.LOW)
                GPIO.output(A1B,GPIO.LOW)
            time.sleep(0.5)
    finally:
        GPIO.cleanup()
        spi.close()