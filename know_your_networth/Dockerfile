# Use official Python image
FROM python:3.10.12

# Set the working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Django runs on
EXPOSE 8000

# Start the application
CMD ["gunicorn", "know_your_networth.wsgi:application", "--bind", "0.0.0.0:8000"]
