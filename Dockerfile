# Use the official Python image
FROM python:3.8-slim-buster

# Copy the application files
COPY . /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Run the app
CMD ["python3", "app.py"]
