import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    port="5432",
    user="savelovba",
    password="123")
cur = conn.cursor()
cur.execute("ALTER TABLE weather DROP COLUMN TimeZone, DROP COLUMN AirportCode, DROP COLUMN LocationLat, DROP COLUMN LocationLng, DROP COLUMN ZipCode;")
cur.execute("ALTER TABLE accidents DROP COLUMN StartLat, DROP COLUMN StartLng, DROP COLUMN EndLat, DROP COLUMN EndLng, DROP COLUMN Description, DROP COLUMN Number, DROP COLUMN Street, DROP COLUMN Side, DROP COLUMN County, DROP COLUMN Zipcode, DROP COLUMN CountryUS, DROP COLUMN Timezone, DROP COLUMN AirportCode, DROP COLUMN WeatherTimestamp, DROP COLUMN WindChill, DROP COLUMN Humidity, DROP COLUMN Pressure, DROP COLUMN WindDirection, DROP COLUMN WeatherCondition, DROP COLUMN Amenity, DROP COLUMN Bump, DROP COLUMN Crossing, DROP COLUMN GiveWay, DROP COLUMN Junction, DROP COLUMN NoExit, DROP COLUMN Railway, DROP COLUMN Roundabout, DROP COLUMN Station, DROP COLUMN Stop, DROP COLUMN TrafficCalming, DROP COLUMN TrafficSignal, DROP COLUMN TurningLoop, DROP COLUMN SunriseSunset, DROP COLUMN CivilTwilight, DROP COLUMN NauticalTwilight, DROP COLUMN AstronomicalTwilight")
cur.execute("ALTER TABLE construction DROP COLUMN StartLat, DROP COLUMN StartLng, DROP COLUMN EndLat, DROP COLUMN EndLng, DROP COLUMN Description, DROP COLUMN Number, DROP COLUMN Street, DROP COLUMN Side, DROP COLUMN County, DROP COLUMN Zipcode, DROP COLUMN CountryUS, DROP COLUMN Timezone, DROP COLUMN AirportCode, DROP COLUMN WeatherTimestamp, DROP COLUMN WindChill, DROP COLUMN Humidity, DROP COLUMN Pressure, DROP COLUMN WindDirection, DROP COLUMN WeatherCondition, DROP COLUMN Amenity, DROP COLUMN Bump, DROP COLUMN Crossing, DROP COLUMN GiveWay, DROP COLUMN Junction, DROP COLUMN NoExit, DROP COLUMN Railway, DROP COLUMN Roundabout, DROP COLUMN Station, DROP COLUMN Stop, DROP COLUMN TrafficCalming, DROP COLUMN TrafficSignal, DROP COLUMN TurningLoop, DROP COLUMN SunriseSunset, DROP COLUMN CivilTwilight, DROP COLUMN NauticalTwilight, DROP COLUMN AstronomicalTwilight")
cur.execute("""
DELETE FROM accidents 
WHERE date_trunc('year', starttime)::date <> '2021-01-01'::date;
DELETE FROM construction 
WHERE date_trunc('year', starttime)::date <> '2021-01-01'::date;
DELETE FROM weather 
WHERE date_trunc('year', starttime)::date <> '2021-01-01'::date;
""")
cur.execute("DELETE FROM accidents WHERE severity like '1'")
cur.execute("""
    DELETE FROM weather 
    WHERE EXTRACT(EPOCH FROM (endtime - starttime)) < 300
""")
conn.commit()
