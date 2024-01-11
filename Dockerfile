# Use the official Python 3.9 image as the base image
FROM python:3.9

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the local directory (containing source code) into the /app directory of the container
COPY . /app

# Upgrade pip and setuptools to their latest versions
RUN pip install --upgrade pip setuptools

# Install dependencies listed in the requirements.txt file
RUN pip install -r requirements.txt

# Expose port 800 to allow communication with the application running inside the container
EXPOSE 800

# Set the default command to run when the container starts
# Use uvicorn to run the FastAPI application defined in src/main.py on host 0.0.0.0 and port 800
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "800"]
