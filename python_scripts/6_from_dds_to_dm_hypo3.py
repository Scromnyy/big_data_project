import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    port="5432",
    user="savelovba",
    password="123")
cur = conn.cursor()

cur.execute("""
INSERT INTO dm_hypo3 (state, num_accidents, num_construction)
SELECT a.state as state, COUNT(DISTINCT a.id) AS num_accidents, COUNT(DISTINCT c.id) AS num_construction
FROM accidents a
LEFT JOIN construction c ON a.state = c.state AND a.starttime >= '2021-01-01' AND a.starttime < '2021-02-01' AND c.starttime >= '2021-01-01' AND c.starttime < '2021-02-01'
WHERE a.starttime >= '2021-01-01' AND a.starttime < '2021-02-01'
GROUP BY a.state;
""")
conn.commit()
