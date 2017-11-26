#!/usr/bin/python
import RPi.GPIO as GPIO
from flask import Flask, request, render_template, redirect
from config import PINS

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

app = Flask(__name__)


# Setup GPIO for all relays listed above in PINS
[GPIO.setup(PINS.get(x).get('gpio'), GPIO.OUT) for x in PINS]

# Set the state of each GPIO after setup for toggling
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

