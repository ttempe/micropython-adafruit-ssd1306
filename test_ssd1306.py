import ssd1306
from machine import SPI, Pin
import time
import framebuf

def load_image(name):
    "takes a filename, returns a framebuffer"
    f = open(name, 'rb')
    if b'P4\n' != f.readline():                         # Magic number
        raise ImportError("Invalid file")
    f.readline()                                       # Creator comment
    width, height = list(int(j) for j in f.readline()[:-1].decode().split(" ")) # Dimensions
    data = bytearray(f.read())
    return framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)


d = ssd1306.SSD1306_SPI(128, 64, SPI(1),
        dc=Pin("B1", Pin.OUT),
        res=Pin("C9", Pin.OUT),
        cs=Pin("A8", Pin.OUT),
        external_vcc=False, mirror_v=True, mirror_h=True)



while 1:
    d.text("Hello world!", 0, 0, 1)
    d.framebuf.line(127, 0, 0, 63, 1)
    d.show()
    time.sleep(1)

    d.framebuf.blit(load_image("test.pbm"), 0, 0)
    d.show()
    time.sleep(1)

    d.fill(0) #erase the buffer
    d.show()
    time.sleep(1)
    
