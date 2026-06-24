# Use a slim Python image
FROM python:3.11-slim

# Install Nuclei (via Go) or download the binary
# A cleaner way is using the official binary release
RUN apt-get update && apt-get install -y wget unzip \
    && wget https://github.com/projectdiscovery/nuclei/releases/latest/download/nuclei_linux_amd64.zip \
    && unzip nuclei_linux_amd64.zip -d /usr/local/bin/

# Set up your app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 10000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
