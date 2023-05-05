import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    port="5432",
    user="savelovba",
    password="123")
cur = conn.cursor()

cur.execute("""
insert into dm_hypo1 (month, num_accidents)
SELECT TO_CHAR(DATE_TRUNC('month', starttime), 'Month') AS month, COUNT(*) AS num_accidents
FROM accidents
WHERE EXTRACT(YEAR FROM starttime) = 2021 AND severity like '4'
GROUP BY DATE_TRUNC('month', starttime), month
ORDER BY DATE_TRUNC('month', starttime);
""")
conn.commit()
