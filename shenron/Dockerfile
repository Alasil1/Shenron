# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libmariadb-dev default-libmysqlclient-dev python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/
COPY DigiCertGlobalRootCA.crt.pem /app/DigiCertGlobalRootCA.crt.pem

EXPOSE 80

# Run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "shenron.wsgi:application"]

