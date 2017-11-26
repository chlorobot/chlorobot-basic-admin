# chlorobot-basic-admin

A basic web interface to toggle chlorobot's relays - will be superseded by a complete management / monitoring app.

![chlorobot basic admin](/screenshot.png "chlorobot basic admin")

Install dependencies

    pip install flask

Edit app.py, edit PINS dictionary to map your device's to their GPIO pins.

    python app.py

Point a browser to http://{ip-of-pi}:8000/
