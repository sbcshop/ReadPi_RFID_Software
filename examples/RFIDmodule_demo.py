#Demo code to Test RFID module of ReadPi
#import libraries for serial, spi and PWM methods
from machine import UART, Pin,SPI,PWM
import time,utime
import st7789 #library of TFT display controller uses SPI interface
import vga1_bold_16x32 as font

buzzer = PWM(Pin(15))	#define buzzer pin connection
  
def playtone(frequency): # to play tone on buzzer 
    buzzer.duty_u16(5000)
    buzzer.freq(frequency)

def bequiet(): # switch off buzzer
    buzzer.duty_u16(0)
    

spi = SPI(1, baudrate=40000000, sck=Pin(10), mosi=Pin(11))
tft = st7789.ST7789(spi,240,240,reset=Pin(12, Pin.OUT),cs=Pin(9, Pin.OUT),dc=Pin(8, Pin.OUT),backlight=Pin(13, Pin.OUT),rotation=1)#SPI interface for tft screen

uart = UART(1, baudrate=9600,bits=8, parity=None, stop=1)

bequiet()

def main():
    tft.init()
   
    tft.text(font,"SB COMPONENTS", 10,40,st7789.YELLOW)# print on tft screen
    tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen
    
    tft.text(font,"ReadPi", 10,120,st7789.GREEN)
    tft.fill_rect(0, 152, 240,10, st7789.RED)
    time.sleep(0.8)
    tft.fill(0)
main()


tft.text(font,"SCAN CARDS", 30,40,st7789.YELLOW)# print on tft screen
tft.fill_rect(0, 72, 240,10, st7789.RED)#display red line on tft screen


while 1:
    command= uart.read(12) #read for card, 12 bytes for our card maybe different for other
    if command:
        print(command.decode("utf-8"))
        #tft.text(font,command.decode("utf-8"), 10,120,st7789.GREEN)
        tft.text(font,command.decode("utf-8"), 0,120,st7789.YELLOW)# print on tft screen
        playtone(1865)
        utime.sleep(0.2)
        bequiet()

        
