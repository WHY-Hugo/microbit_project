basic.forever(function on_forever() {
    if (mooncar.UltrasonicSensor() < 30) {
        mooncar.MoonCarGo(mooncar.Direction.direct1, 0)
    } else {
        mooncar.MoonCarGo(mooncar.Direction.direct1, 30)
    }
    
})
