# chlorobot-basic-admin

A basic web interface to toggle chlorobot's relays - will be superseded by a complete management / monitoring app.

![chlorobot basic admin](/screenshot.png "chlorobot basic admin")


Physical layout and GPIO / pin / plug / strap / device mappings

    Mains Gang Layout

    1   3

    2   4


    Mains Relay

    GPIO        COLOR       MAINS PLUG      RELAY PIN       DEVICE
    23          grey        4               1               Heat Mat
    24          brown       3               2               Reservoir Aerator
    17          red         2               3               LED Matrix
    27          orange      1               4               PSU (12v rail)

    12V Relay

    GPIO        COLOR       RELAY PIN       DEVICE
    20          green       1               Water Pump
    21          yellow      2               Exhaust Fan (Top)


*Note all mains are in a default NC (normally closed) state meaning setting GPIO.LOW will turn OFF the attached device.*

*Additionally all 12 volt rail relays are wired for a NO (Normally Open) state meaning GPIO.LOW will turn ON the attached device.*


Install dependencies

    pip install flask
    sudo apt-get install supervisor

Copy supervisor configuration and start application

    sudo cp chlorobot-admin.conf /etc/supervisor/conf.d/
    sudo supervisorctl reread
    sudo supervisorctl reload

Edit app.py, edit PINS dictionary to map your device's to their GPIO pins.

    python app.py

Point a browser to http://{ip-of-pi}:8000/

Clicking the buttons along the 'State' table cells toggles GPIO


