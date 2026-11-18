from flask import Flask, Response
import json

app = Flask(__name__)


def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    i = 3
    while i * i <= number:
        if number % i == 0:
            return False
        i += 2
    return True


@app.route("/alkuluku/<int:number>")
def alkuluku(number):
    vastaus = {"Number": number, "isPrime": is_prime(number)}
    return Response(json.dumps(vastaus), mimetype="application/json")


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)