# Use a minimal, modern Python base image
FROM python:3.12-slim-bookworm

# Set environment variables to ensure secure and optimized execution
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_USER=appuser \
    APP_HOME=/home/appuser/app

# Create a non-root user and group
RUN groupadd -r ${APP_USER} && useradd -r -g ${APP_USER} -d /home/${APP_USER} -s /sbin/nologin ${APP_USER}

# Set the working directory
WORKDIR ${APP_HOME}

# Install dependencies as root before switching users
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Change ownership of the application directory to the non-root user
RUN chown -R ${APP_USER}:${APP_USER} ${APP_HOME}

# Switch to the non-root user
USER ${APP_USER}

# Expose the application port
EXPOSE 8000

# Run the application securely using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "app.main:app"]