import psycopg2
import time

# Wait a bit for Postgres to be ready
time.sleep(5)

try:
    # 1. Connect to PostgreSQL
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    print("✅ Connected to PostgreSQL!")

    cur = conn.cursor()

    # 2. Create table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        age INT
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    print("✅ Table created or already exists.")

    # 3. Insert one row
    insert_query = """
    INSERT INTO students (name, age)
    VALUES (%s, %s)
    RETURNING id;
    """
    cur.execute(insert_query, ("Sanjay", 22))
    inserted_id = cur.fetchone()[0]
    conn.commit()
    print(f"✅ Inserted id = {inserted_id}")

    # 4. Read and print the row
    select_query = "SELECT id, name, age FROM students WHERE id = %s;"
    cur.execute(select_query, (inserted_id,))
    row = cur.fetchone()
    print("✅ Fetched row:", row)

    # 5. Close everything
    cur.close()
    conn.close()
    print("✅ Connection closed.")

except Exception as e:
    print("❌ Error:", e)
