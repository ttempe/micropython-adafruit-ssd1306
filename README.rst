MicroPython driver for SSD1306 OLED displays
============================================

This library supports both I2C and SPI.

While this library is no longer supported by Adafruit (which prefers maintaining their own fork of Micropython), it is still
fully functional, and quite useful. It uses the native Micropython framebuf interface.

I've added screen mirroring & rotation support, and demo code.

Here's how to get started:

.. code:: python

    import ssd1306
    from machine import SPI, Pin
    d = ssd1306.SSD1306_SPI(128, 64, SPI(1), dc=Pin("B1", Pin.OUT), res=Pin("C9", Pin.OUT), cs=Pin("A8", Pin.OUT))
    d.text("Hello world!", 0, 0, 1)
    d.show()
