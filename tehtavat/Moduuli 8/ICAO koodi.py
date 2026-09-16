import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='ihmiset',
    user='dbuser',
    password='sAL_a3ana',
    autocommit=True
)

icao = input("Anna lentoaseman ICAO-koodi: ")

sql = """
    SELECT name, municipality
    FROM airport
    WHERE ident = %s
"""

kursori = yhteys.cursor()
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print("Lentokentän nimi:", tulos[0])
    print("Sijaintikunta:", tulos[1])
else:
    print("Lentokenttää ei löytynyt.")

kursori.close()
yhteys.close()