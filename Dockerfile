# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    pip install --upgrade pip

# expondo porta
EXPOSE 80

# Run main.py when the container launches
CMD ["python", "main.py", "--host", "0.0.0.0", "--port", "80"]
