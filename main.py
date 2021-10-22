def on_forever():
    if mooncar.ultrasonic_sensor() < 30:
        mooncar.moon_car_go(mooncar.Direction.DIRECT1, 0)
    else:
        mooncar.moon_car_go(mooncar.Direction.DIRECT1, 30)
basic.forever(on_forever)

def on_forever2():
    mooncar.filllight(mooncar.Switch.OPEN)
basic.forever(on_forever2)

def on_forever3():
    if mooncar.line_follower_sensor() == 0:
        mooncar.moon_car_go(mooncar.Direction.DIRECT1, 30)
    elif mooncar.line_follower_sensor() == 1:
        mooncar.moon_car_lr(0, 15)
    elif mooncar.line_follower_sensor() == 2:
        mooncar.moon_car_lr(15, 0)
    else:
        pass
basic.forever(on_forever3)

def on_forever4():
    basic.show_number(mooncar.line_follower_sensor())
basic.forever(on_forever4)
