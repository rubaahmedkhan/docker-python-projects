FROM python:3.9


# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container's /app directory
COPY . .

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Run the application
CMD ["python", "app.py"]
