🐳 Dockerized Python + PostgreSQL Project
Beginner-Friendly End-to-End Docker Assignment

This project demonstrates how to:

Pull images from Docker Hub

Build and run a Dockerized Python application

Create and use a Dockerfile

Set up a custom Docker network

Run PostgreSQL inside a Docker container

Connect a Python app to a PostgreSQL container

Create a table, insert a record, and retrieve it

This guide explains everything step-by-step with commands and screenshot placeholders.

📁 1. Project Structure
my-app/
│── app.py
└── Dockerfile

🧰 2. Prerequisites

Before starting, ensure you have:

Docker Desktop installed & running

Visual Studio Code (VS Code) installed

Docker extension for VS Code (optional but helpful)

Verify Docker installation:

docker version


📸 Screenshot: docker-version.png (output of docker version)

🧩 3. Setting Up VS Code With Docker
3.1 Install VS Code

https://code.visualstudio.com/

3.2 Install Required Extensions

Open VS Code → Extensions → install:

Docker (Microsoft)

Remote - Containers (optional)

📸 Screenshot: vscode-docker-extension.png

3.3 Verify Docker Panel

In VS Code sidebar → click Docker icon
You should see:

Containers

Images

Volumes

Networks

📸 Screenshot: vscode-docker-panel.png

🌐 4. Pulling Images From Docker Hub

Docker Hub: https://hub.docker.com/

Pull an image:
docker pull ubuntu

List downloaded images:
docker images


📸 Screenshot: docker-images.png

🐍 5. Creating a Simple Python App
5.1 Create a project folder:
mkdir my-app
cd my-app

5.2 Open folder in VS Code:
code .


📸 Screenshot: vscode-my-app-folder.png

5.3 Create app.py:
print("Hello from inside a Docker container!")


Save file.

📦 6. Writing a Dockerfile for the Python App

Create a file named Dockerfile:

FROM python:3.10-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]


📸 Screenshot: dockerfile-basic.png

▶️ 7. Building & Running Your First Docker Image
7.1 Build image:
docker build -t my-python-app .


📸 Screenshot: docker-build-basic.png

7.2 Run container:
docker run my-python-app


Expected output:

Hello from inside a Docker container!


📸 Screenshot: docker-run-hello.png

🧹 8. Cleaning Up Docker Resources
List containers:
docker ps
docker ps -a

Remove container:
docker rm <container_id>

Remove all stopped containers:
docker container prune

Remove image:
docker rmi my-python-app


📸 Screenshot: docker-ps-a.png

🌐 9. Creating a Custom Docker Network + PostgreSQL Container
9.1 Create a Docker network:
docker network create mynetwork

9.2 Run PostgreSQL container on the network:
docker run -d --name my-postgres --network mynetwork \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=mydb \
  postgres


(Windows one-line version):

docker run -d --name my-postgres --network mynetwork -e POSTGRES_USER=user -e POSTGRES_PASSWORD=pass -e POSTGRES_DB=mydb postgres

9.3 Verify container is running:
docker ps


Expected:

my-postgres   postgres   Up ...


📸 Screenshot: docker-ps-postgres.png

🔗 10. Connecting Python App to PostgreSQL

Modify app.py to test DB connection:

import psycopg2
import time

time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    print("Connected to the database!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)

📦 11. Update Dockerfile to Install psycopg2
FROM python:3.10-slim

WORKDIR /app

COPY app.py .

RUN pip install psycopg2-binary

CMD ["python", "app.py"]

Rebuild image:
docker build -t my-python-app .

Run container on network:
docker run --rm --network mynetwork my-python-app


Expected output:

Connected to the database!


📸 Screenshot: docker-run-connected.png

🧪 12. Beginner Task: Create, Insert, and Read From Database

Final app.py:

import psycopg2
import time

time.sleep(5)

try:
    conn = psycopg2.connect(
        host="my-postgres",
        database="mydb",
        user="user",
        password="pass"
    )
    print("✅ Connected to PostgreSQL!")

    cur = conn.cursor()

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

    insert_query = """
    INSERT INTO students (name, age)
    VALUES (%s, %s)
    RETURNING id;
    """
    cur.execute(insert_query, ("Sanjay", 22))
    inserted_id = cur.fetchone()[0]
    conn.commit()
    print(f"✅ Inserted id = {inserted_id}")

    select_query = "SELECT id, name, age FROM students WHERE id = %s;"
    cur.execute(select_query, (inserted_id,))
    row = cur.fetchone()
    print("✅ Fetched row:", row)

    cur.close()
    conn.close()
    print("✅ Connection closed.")

except Exception as e:
    print("❌ Error:", e)

Rebuild:
docker build -t my-python-app .

Run:
docker run --rm --network mynetwork my-python-app


Expected output:

✅ Connected to PostgreSQL!
✅ Table created or already exists.
✅ Inserted id = 1
✅ Fetched row: (1, 'Sanjay', 22)
✅ Connection closed.


📸 Screenshot: docker-run-full-app.png

🧾 13. What This Project Demonstrates

Docker image creation

Container execution

Python app containerization

Networking between containers

Running PostgreSQL in Docker

Python–Postgres communication via psycopg2

SQL operations: create table, insert, select

🐛 14. Troubleshooting
❌ Error: Docker API not found

Fix: Open Docker Desktop.

❌ SyntaxError in Python

Fix: Ensure quotes and indentation are correct.

❌ Connection failed

Fix:

Ensure my-postgres is running

Ensure both containers use --network mynetwork

🎉 15. Conclusion

You successfully:

Built a Dockerized Python app

Deployed PostgreSQL inside Docker

Connected containers using a custom network

Performed real database operations

Completed a full end-to-end Docker assignment 🎯