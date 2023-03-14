import spidev, time #sudo pip install spidev

spi = spidev.SpiDev() #spi객체 생성

spi.open(0,0) #spi의 버스의 cs(Chip Select) 0신호선을 사용 

def analog_read(channel): #mcp3008에서 아날로그 센서값을 받는 코드
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out

def water():
    while True:
        reading = analog_read(0) #채널 0번의 아날로그 센서값을 받아옴
        voltage = reading * 3.3 / 1024
        print("Reading=%d\tVoltage=%f" % (reading, voltage))
        time.sleep(1)