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

# Создаем таблицу accidents в базе данных Postgres
cur.execute("""
    CREATE TABLE accidents (
    ID VARCHAR(100),
  Severity VARCHAR(100),
  StartTime timestamp,
  EndTime timestamp,
  StartLat double precision,
  StartLng double precision,
  EndLat double precision,
  EndLng double precision,
  Distance double precision,
  Description text,
  Number double precision,
  Street VARCHAR(100),
  Side VARCHAR(100),
  City VARCHAR(100),
  County VARCHAR(100),
  State VARCHAR(100),
  ZipCode text,
  CountryUS VARCHAR(100),
  TimeZone VARCHAR(100),
  AirportCode VARCHAR(100),
  WeatherTimestamp timestamp,
  Temperature double precision,
  WindChill double precision,
  Humidity double precision,
  Pressure double precision,
  Visibility double precision,
  WindDirection VARCHAR(100),
  WindSpeed double precision,
  Precipitation double precision,
  WeatherCondition VARCHAR(100),
  Amenity boolean,
  Bump boolean,
  Crossing boolean,
  GiveWay boolean,
  Junction boolean,
  NoExit boolean,
  Railway boolean,
  Roundabout boolean,
  Station boolean,
  Stop boolean,
  TrafficCalming boolean,
  TrafficSignal boolean,
  TurningLoop boolean,
  SunriseSunset VARCHAR(100),
  CivilTwilight VARCHAR(100),
  NauticalTwilight VARCHAR(100),
  AstronomicalTwilight VARCHAR(100)
    );
""")

# Создаем таблицу construction в базе данных Postgres
cur.execute("""
    CREATE TABLE construction (
  ID VARCHAR(100),
  Severity VARCHAR(100),
  StartTime timestamp,
  EndTime timestamp,
  StartLat double precision,
  StartLng double precision,
  EndLat double precision,
  EndLng double precision,
  Distance double precision,
  Description text,
  Number double precision,
  Street VARCHAR(100),
  Side VARCHAR(100),
  City VARCHAR(100),
  County VARCHAR(100),
  State VARCHAR(100),
  ZipCode text,
  CountryUS VARCHAR(100),
  TimeZone VARCHAR(100),
  AirportCode VARCHAR(100),
  WeatherTimestamp timestamp,
  Temperature double precision,
  WindChill double precision,
  Humidity double precision,
  Pressure double precision,
  Visibility double precision,
  WindDirection VARCHAR(100),
  WindSpeed double precision,
  Precipitation double precision,
  WeatherCondition VARCHAR(100),
  Amenity boolean,
  Bump boolean,
  Crossing boolean,
  GiveWay boolean,
  Junction boolean,
  NoExit boolean,
  Railway boolean,
  Roundabout boolean,
  Station boolean,
  Stop boolean,
  TrafficCalming boolean,
  TrafficSignal boolean,
  TurningLoop boolean,
  SunriseSunset VARCHAR(100),
  CivilTwilight VARCHAR(100),
  NauticalTwilight VARCHAR(100),
  AstronomicalTwilight VARCHAR(100)
    );
""")

# Создаем таблицу weather в базе данных Postgres
cur.execute("""
    CREATE TABLE weather (
  EventId VARCHAR(100),
  Type VARCHAR(100),
  Severity VARCHAR(100),
  StartTime timestamp,
  EndTime timestamp,
  Precipitation double precision,
  TimeZone VARCHAR(100),
  AirportCode VARCHAR(100),
  LocationLat double precision,
  LocationLng double precision,
  City VARCHAR(100),
  County VARCHAR(100),
  State VARCHAR(100),
  ZipCode text);
""")

