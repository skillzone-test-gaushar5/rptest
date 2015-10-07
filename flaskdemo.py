from flask import Flask, json, jsonify, request
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

@app.route("/led")
def led():
    return jsonify({"ledStatus": GPIO.input(LED_PIN)})

@app.route("/led/on")
def led_on():
    GPIO.output(LED_PIN, GPIO.HIGH)
    return jsonify({"ledStatus": GPIO.input(LED_PIN)})

@app.route("/led/off")
def led_off():
    GPIO.output(LED_PIN, GPIO.LOW)
    return jsonify({"ledStatus": GPIO.input(LED_PIN)})

@app.route("/test", methods=["POST"])
def test():
    return "received data: " + request.get_data()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
