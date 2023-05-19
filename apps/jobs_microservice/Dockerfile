# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the code files into the container
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY init_db.py .
COPY jobs.py .
COPY schema.sql .

# Create the database and load the schema
RUN python init_db.py

# Make port 5001 available to the world outside this container
EXPOSE 5001

# Run the application when the container launches
CMD ["python", "jobs.py"]
