# Use a Python base image (choose a specific version if needed)
FROM python:3.11.4-slim-buster

# Create a working directory inside the container
WORKDIR /app

# Copy requirements file (if you have one)
COPY requirements.txt .

# Install dependencies based on requirements.txt
RUN apt-get update && apt-get install -y git && apt-get clean
RUN pip install -r requirements.txt

# Copy the Python script into the working directory
COPY app.py .
COPY entrypoint.sh .

# Define the entry point (command to run)
ENTRYPOINT ["sh", "entrypoint.sh"]
