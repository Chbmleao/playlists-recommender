# Use a Python base image (choose a specific version if needed)
FROM python:3.11.4-slim-buster

# Create a working directory inside the container
WORKDIR /app

# Copy requirements file (if you have one)
COPY requirements.txt .

# Install dependencies based on requirements.txt
RUN pip install -r requirements.txt

# Copy the Python script and data file (modify if needed)
COPY app.py .

# Define the entry point (command to run)
ENTRYPOINT ["python3", "app.py"]