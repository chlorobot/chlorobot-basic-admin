#!/usr/bin/python
import RPi.GPIO as GPIO
from flask import Flask, request, render_template, redirect
import time, sys
from pprint import pprint

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

app = Flask(__name__)

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

[GPIO.setup(PINS.get(x).get('gpio'), GPIO.OUT) for x in PINS]

# Set the state of each pin after setup for toggling
[PINS.get(x).update({'state' : GPIO.input(PINS.get(x).get('gpio'))}) for x in PINS]

@app.route('/', methods=['GET'])
def index() :
    action = request.args.get('action')
    actions = [x for x in PINS]
    if action in actions :
        component = PINS.get(action)
        state = not component.get('state')
        GPIO.output(component.get('gpio'), state)
        PINS.get(action).update({'state' : state})
        return redirect('/')
    return render_template('index.html', data=PINS)


if __name__ == '__main__' :
    app.debug = True
    app.run(host="0.0.0.0", port=8000)

