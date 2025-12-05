FROM python:3.10-slim

WORKDIR /app

# Copy the Python app into the image
COPY app.py .

# Install PostgreSQL driver for Python
RUN pip install psycopg2-binary

# Run the app
CMD ["python", "app.py"]
