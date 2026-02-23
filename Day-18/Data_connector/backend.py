import sqlite3
import pandas as pd

conn = sqlite3.connect("internship.db")

query = """
SELECT interns.name, interns.track, interns.stipend, mentors.mentor_name
FROM interns
INNER JOIN mentors
ON interns.track = mentors.track
"""

df = pd.read_sql_query(query, conn)

print("\nInterns with their Mentors:\n")
print(df)

conn.close()
