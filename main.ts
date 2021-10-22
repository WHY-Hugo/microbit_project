basic.forever(function () {
    basic.showNumber(mooncar.LineFollowerSensor())
})
basic.forever(function () {
    if (mooncar.UltrasonicSensor() < 30) {
        mooncar.MoonCarGo(mooncar.Direction.direct1, 0)
    } else {
        mooncar.MoonCarGo(mooncar.Direction.direct1, 30)
    }
})
basic.forever(function () {
    mooncar.Filllight(mooncar.Switch.Open)
})
basic.forever(function () {
    if (mooncar.LineFollowerSensor() == 0) {
        mooncar.MoonCarGo(mooncar.Direction.direct1, 30)
    } else if (mooncar.LineFollowerSensor() == 1) {
        mooncar.MoonCarLR(0, 15)
    } else if (mooncar.LineFollowerSensor() == 2) {
        mooncar.MoonCarLR(15, 0)
    } else {
    	
    }
})
