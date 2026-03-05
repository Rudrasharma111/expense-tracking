# Python base image
FROM python:3.10-slim

# set working directory
WORKDIR /app

# Copy requirement file and install libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project files
COPY . .

# Command to run the app
CMD ["python", "app/main.py", "all"]