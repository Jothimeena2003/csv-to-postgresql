import pandas as pd
import psycopg2
import time

# Wait for PostgreSQL to start
time.sleep(5)

# Read CSV file
df = pd.read_csv("/data/sample.csv")

print("CSV data:")
print(df)

# Connect to PostgreSQL
connection = psycopg2.connect(
    host="db",
    database="mydatabase",
    user="admin",
    password="password",
    port="5432"
)

cursor = connection.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER,
        name VARCHAR(100),
        department VARCHAR(100),
        salary INTEGER
    )
""")

# Insert CSV data
for _, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO employees (id, name, department, salary)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
        """,
        (
            int(row["id"]),
            row["name"],
            row["department"],
            int(row["salary"])
        )
    )

connection.commit()

cursor.close()
connection.close()

print("CSV data successfully loaded into PostgreSQL!")