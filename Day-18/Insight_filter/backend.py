import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

print("\nData Science interns with stipend > 5000:\n")

cursor.execute("""
SELECT name, stipend
FROM interns
WHERE track = 'Data Science' AND stipend > 5000
""")

for row in cursor.fetchall():
    print(row)

print("\nAverage stipend per track:\n")

cursor.execute("""
SELECT track, AVG(stipend)
FROM interns
GROUP BY track
""")

for row in cursor.fetchall():
    print(row)

print("\nIntern count per track:\n")

cursor.execute("""
SELECT track, COUNT(*)
FROM interns
GROUP BY track
""")

for row in cursor.fetchall():
    print(row)

conn.close()
