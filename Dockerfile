# Use the official Python image
FROM python:3.8-slim-buster

# Copy the application files
COPY . /app

# Set the working directory
WORKDIR /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which the application will run
EXPOSE $PORT

# Use uvicorn as the entry point to run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "${PORT}"]
