import spidev
import time

# SPI 인스턴스 생성
spi = spidev.SpiDev()

# SPI 통신 시작
spi.open(0, 0) #bus : 0, dev : 0

# SPI 통신 속도 설정
spi.max_speed_hz = 100000

# 채널에서 SPI 데이터 읽기 (0~1023)
def analog_read(channel):
    #[byte_1, byte_2, byte_3]
    #byte_2 : channel config (channel 0) (+8)-> 0000 1000
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8) + ret[2]
    return adc_out

try:
    while True:
        reading = analog_read(0) #reading(0~1023)
        voltage = reading * 3.3/1023
        print("Reading=%d, voltage=%f" % (reading,voltage))
        time.sleep(0.01)

finally:
    spi.close()