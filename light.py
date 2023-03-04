import spidev, time #sudo pip install spidev
import RPi.GPIO as GPIO
GPIO.setwarnings(False) #GPIO핀 초기화
GPIO.setmodme(GPIO.BCM) 
pin = 18
GPIO.setup(pin, GPIO.OUT)
spi = spidev.SpiDev() #spi객체 생성
spi.open(0,0) #spi의 버스의 cs(Chip Select) 0신호선을 사용
softpwm = GPIO.PWM(pin,1000) #18번 핀을 pwm핀으로 설정 hz = 1000
softpwm.start(0) #처음 DutyCycle을 0으로 설정
def analog_read(channel): #mcp3008에서 아날로그 센서값을 받는 코드
    r = spi.xfer2([1,(8+channel)<<4,0])
    adcout = ((r[1]&3)<<8)+r[2]
    return adcout

while True:
    reading = analog_read(2) #채널 2번의 아날로그 값을 받아옴
    print("read : %d"%(128-reading)) #밝기가 낮으면 값이 올라가기 때문에 밝기가 낮을때 불이 켜지도록 하기 위해 조도센서에서 측정된 최댓값에서 reading을 빼줌(128은 나의 조도센서가 즉정했던 최댓값)
    if reading > 100: #DutyCycle에 들어갈 최댓값 최솟값 설정
        reading = 100
    elif reading < 0:
        reading = 0
    softpwm.ChangeDutyCycle(reading) #DutyCycle을 reading으로 바꿔줌(reading은 조도센서의 값임)
    time.sleep(1)