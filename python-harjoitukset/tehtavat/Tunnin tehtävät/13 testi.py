from flask import Flask, Response
import json

helloworldapp = Flask(__name__)


@helloworldapp.route('/helloworld/<kerrat>')
def helloworld(kerrat):
    try:
        kerrat = int(kerrat)
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "viesti": "Hello World! " * kerrat
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte, anna kokonaisluku"
        }

    jsonvast = json.dumps(vastaus, ensure_ascii=False)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")


@helloworldapp.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": 404,
        "teksti": "Virheellinen päätepiste, sivua ei löydy"
    }
    jsonvast = json.dumps(vastaus, ensure_ascii=False)
    return Response(response=jsonvast, status=404, mimetype="application/json")


if __name__ == '__main__':
    helloworldapp.run(use_reloader=False, host='127.0.0.1', port=3000)