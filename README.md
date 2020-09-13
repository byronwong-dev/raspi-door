# Raspi-door
A simple script to pass command HIGH (true) or LOW (false) for running a 5VDC relay

### Prerequisites

 - Python (with pip)

### Getting Started
1. install dependencies `pip install -r requirements.txt`

2. run `cp .env.example .env` to create a copy of the env file

2. edit `.env` file and set the value for `GPIO_PIN` for the GPIO pin number you will be using. If the `DOOR_ENV` value is set to `testing`, no actual command will be sent to the GPIO pin
