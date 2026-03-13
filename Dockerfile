# Use a slim Python 3.10 image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set the default command (expects an environment variable for query)
CMD ["python", "main.py", "--query", "Describe the current state of AI Platform Engineering."]