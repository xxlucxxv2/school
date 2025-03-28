I2C_LCD1602.lcd_init(0)

def on_forever():
    if pins.analog_read_pin(AnalogPin.P0) < 200:
        pins.servo_write_pin(AnalogPin.P1, 180)
        I2C_LCD1602.show_string("180grad", 0, 0)
        I2C_LCD1602.show_number(pins.analog_read_pin(AnalogPin.P0), 0, 1)
    else:
        pins.servo_write_pin(AnalogPin.P1, 91)
        I2C_LCD1602.show_string("91 grad", 0, 0)
        I2C_LCD1602.show_number(pins.analog_read_pin(AnalogPin.P0), 0, 1)
basic.forever(on_forever)
