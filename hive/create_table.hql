create database if not exists test;
use test;
create external table if not exists weather (
	EventId string,
	Type string,
	Severity string,
	StartTime timestamp,
	EndTime timestamp,
	Precipitation double,
	TimeZone string,
	AirportCode string,
	LocationLat double,
	LocationLng double,
	City string,
	County string,
	State string,
	ZipCode integer
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/test.db/weather';


create external table if not exists accidents (
	ID string,
	Severity integer,
	StartTime timestamp,
	EndTime timestamp,
	StartLat double,
	StartLng double,
	EndLat double,
	EndLng double,
	Distance double,
	Description string,
	Number double,
	Street string,
	Side string,
	City string,
	County string,
	State string,
	ZipCode string,
	CountryUS string,
	TimeZone string,
	AirportCode string,
	WeatherTimestamp timestamp,
	Temperature double,
	WindChill double,
	Humidity double,
	Pressure double,
	Visibility double,
	WindDirection string,
	WindSpeed double,
	Precipitation double,
	WeatherCondition string,
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
	SunriseSunset string,
	CivilTwilight string,
	NauticalTwilight string,
	AstronomicalTwilight string
	
	
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/test.db/accidents';


create external table if not exists construction (
	ID string,
	Severity integer,
	StartTime timestamp,
	EndTime timestamp,
	StartLat double,
	StartLng double,
	EndLat double,
	EndLng double,
	Distance double,
	Description string,
	Number double,
	Street string,
	Side string,
	City string,
	County string,
	State string,
	ZipCode string,
	CountryUS string,
	TimeZone string,
	AirportCode string,
	WeatherTimestamp timestamp,
	Temperature double,
	WindChill double,
	Humidity double,
	Pressure double,
	Visibility double,
	WindDirection string,
	WindSpeed double,
	Precipitation double,
	WeatherCondition string,
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
	SunriseSunset string,
	CivilTwilight string,
	NauticalTwilight string,
	AstronomicalTwilight string
	
	
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/test.db/construction';



































