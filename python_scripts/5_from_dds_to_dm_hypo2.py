import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    port="5432",
    user="savelovba",
    password="123")
cur = conn.cursor()

cur.execute("""
INSERT INTO dm_hypo2 (state, num_weather_events, num_construction)
SELECT 
    w.state AS state,
    COUNT(DISTINCT CASE WHEN w.type='Snow' OR w.type='Rain' THEN w.eventid END) AS weather_count,
    COUNT(DISTINCT c.ID) AS constructions_count
FROM 
    weather w LEFT JOIN construction c
ON w.state = c.state AND c.starttime >= '2021-01-01' AND c.starttime < '2021-02-01'
WHERE 
    w.starttime >= '2021-01-01' AND w.starttime < '2021-02-01'
GROUP BY 
    w.state
""")
conn.commit()
