FROM python:3.9-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Install additional packages for Flask and CORS
RUN pip install --no-cache-dir flask flask-cors

# Copy application files
COPY . .

# Create data directory and initialize database
RUN mkdir -p data

# Expose necessary ports
EXPOSE 5000 8000 3000

# Command to run the C2 server, phishing server, and dashboard
CMD ["sh", "-c", "python3 c2_server.py & python3 dashboard.py & python3 -m http.server 8000"]
