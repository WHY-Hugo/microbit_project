def on_forever():
    if mooncar.ultrasonic_sensor() < 30:
        mooncar.moon_car_go(mooncar.Direction.DIRECT1, 0)
    else:
        mooncar.moon_car_go(mooncar.Direction.DIRECT1, 30)
basic.forever(on_forever)
