import psycopg2
import csv 
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    port="5432",
    user="savelovba",
    password="123")
cur = conn.cursor()

# Заполняем таблицу accidents в базе данных Postgres
with open('/home/bogdan/csvfiles/Accidents.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO accidents (ID, Severity, StartTime, EndTime, StartLat, StartLng, EndLat, EndLng, Distance, Description, Number, Street, Side, City, County, State, ZipCode, CountryUS, TimeZone, AirportCode, WeatherTimestamp, Temperature, WindChill, Humidity, Pressure, Visibility, WindDirection, WindSpeed, Precipitation, WeatherCondition, Amenity, Bump, Crossing, GiveWay, Junction, NoExit, Railway, Roundabout, Station, Stop, TrafficCalming, TrafficSignal, TurningLoop, SunriseSunset, CivilTwilight, NauticalTwilight, AstronomicalTwilight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46]))

# Заполняем таблицу construction в базе данных Postgres
with open('/home/bogdan/csvfiles/Constructions.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO accidents (ID, Severity, StartTime, EndTime, StartLat, StartLng, EndLat, EndLng, Distance, Description, Number, Street, Side, City, County, State, ZipCode, CountryUS, TimeZone, AirportCode, WeatherTimestamp, Temperature, WindChill, Humidity, Pressure, Visibility, WindDirection, WindSpeed, Precipitation, WeatherCondition, Amenity, Bump, Crossing, GiveWay, Junction, NoExit, Railway, Roundabout, Station, Stop, TrafficCalming, TrafficSignal, TurningLoop, SunriseSunset, CivilTwilight, NauticalTwilight, AstronomicalTwilight)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23], row[24], row[25], row[26], row[27], row[28], row[29], row[30], row[31], row[32], row[33], row[34], row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], row[43], row[44], row[45], row[46]))

# Заполняем таблицу weather в базе данных Postgres
with open('/home/bogdan/csvfiles/Weather.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        cur.execute("""
            INSERT INTO weather (EventId, Type, Severity, StartTime, EndTime, Precipitation, TimeZone, AirportCode, LocationLat, LocationLng, City, County, State, ZipCode)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13]))


