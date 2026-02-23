import sqlite3

conn = sqlite3.connect("internship.db")
cursor = conn.cursor()

print("Database connected successfully")

cursor.execute("""
CREATE TABLE IF NOT EXISTS interns (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    track TEXT NOT NULL,
    stipend INTEGER
)
""")

print("Table created successfully")

intern_data = [
    ("Rizwan", "Data Science", 15000),
    ("Ananya", "Web Development", 12000),
    ("Karthik", "AI/ML", 18000),
    ("Sneha", "Cyber Security", 14000),
    ("Rahul", "Cloud Computing", 16000)
]

cursor.executemany(
    "INSERT INTO interns (name, track, stipend) VALUES (?, ?, ?)",
    intern_data
)

conn.commit()
print("Sample data inserted")

cursor.execute("SELECT name, track FROM interns")

rows = cursor.fetchall()

print("\nIntern Names and Tracks:")
for row in rows:
    print(f"Name: {row[0]}, Track: {row[1]}")

conn.close()
print("\nDatabase connection closed")
