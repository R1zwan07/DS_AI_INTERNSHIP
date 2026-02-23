import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    track TEXT,
    stipend INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS mentors (
    mentor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mentor_name TEXT,
    track TEXT
)
""")

cursor.execute("DELETE FROM interns")
cursor.execute("DELETE FROM mentors")

interns_data = [
    ("Rizwan", "Data Science", 15000),
    ("Ananya", "Web Development", 8000),
    ("Karthik", "AI/ML", 18000),
    ("Sneha", "Data Science", 12000),
    ("Rahul", "Cloud", 9000),
    ("Megha", "AI/ML", 20000)
]

cursor.executemany(
    "INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)",
    interns_data
)

mentors_data = [
    ("Dr. Sharma", "Data Science"),
    ("Mr. Gupta", "Web Development"),
    ("Dr. Iyer", "AI/ML"),
    ("Mr. Khan", "Cloud")
]

cursor.executemany(
    "INSERT INTO mentors (mentor_name, track) VALUES (?, ?)",
    mentors_data
)

conn.commit()
conn.close()

print("Database setup complete")
