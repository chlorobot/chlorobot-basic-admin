import RPi.GPIO as GPIO

# Named GPIO to physical pin mapping and mains plug with color of wire and default relay state (Normally Open, Normally Closed)

PINS = {
    'heat' : {
        "name" : "Heat Mat",
        "gpio" : 23,
        "color" : "grey",
        "plug" : 4,
        "pin" : 1,
        "default" : GPIO.LOW,
        "state" : None
    },
    'aerator' : {
        "name" : "Aerator",
        "gpio" : 24,
        "color" : "brown",
        "plug" : 3,
        "pin" : 2,
        "default" : GPIO.LOW,
        "state" : None
    },
    'light' : {
        "name" : "LED Light Array",
        "gpio" : 17,
        "color" : "red",
        "plug" : 2,
        "pin" : 3,
        "default" : GPIO.LOW,
        "state" : None
    },
    'psu' : {
        "name" : "Power Supply",
        "gpio" : 27,
        "color" : "orange",
        "plug" : 1,
        "pin" : 4,
        "default" : GPIO.LOW,
        "state" : None
    },
    'pump' : {
        "name" : "Water Pump",
        "gpio" : 20,
        "color" : "green",
        "plug" : None,
        "pin" : 1,
        "default" : GPIO.HIGH,
        "state" : None
    },
    'fan' : {
        "name" : "Exhaust Fan (Top)",
        "gpio" : 21,
        "color" : "yellow",
        "plug" : None,
        "pin" : 2,
        "default" : GPIO.HIGH,
        "state" : None
    }

}

