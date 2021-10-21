def on_forever():
    basic.show_number(mooncar.line_follower_sensor())
basic.forever(on_forever)
