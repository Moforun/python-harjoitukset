import json
import os

import mysql.connector
from dotenv import load_dotenv
from flask import Flask, Response

load_dotenv()

app = Flask(__name__)


def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        autocommit=True,
    )


def json_response(data, status=200):
    return Response(
        json.dumps(data, ensure_ascii=False),
        status=status,
        mimetype="application/json",
    )


@app.route("/kenttä/<icao>")
def kentta(icao):
    icao = icao.upper()
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT ident, name, municipality FROM airport WHERE ident = %s",
            (icao,),
        )
        rivi = cursor.fetchone()
    finally:
        connection.close()

    if rivi is None:
        return json_response({"Status": 404, "Message": "Airport not found"}, 404)

    vastaus = {"ICAO": rivi[0], "Name": rivi[1], "Municipality": rivi[2]}
    return json_response(vastaus)


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)