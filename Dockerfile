# Dockerfile

# 1. Base Image: Use an official, slim Python image.
FROM python:3.9-slim

# 2. Set Environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Install dependencies
# Copy only the requirements file first to leverage Docker's caching mechanism.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the entire project code into the working directory
COPY . .

# 6. Expose the port Gunicorn will run on
EXPOSE 8000

# 7. Define the command to run the application using Gunicorn
# This is the command that starts your application in production.
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "test1.wsgi:application"]