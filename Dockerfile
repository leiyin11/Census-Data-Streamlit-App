# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create .streamlit directory and copy config files
RUN mkdir -p ~/.streamlit && \
    cp config.toml ~/.streamlit/config.toml && \
    cp credentials.toml ~/.streamlit/credentials.toml

# Expose port 80
EXPOSE 80

# Set environment variables
ENV STREAMLIT_SERVER_PORT=80
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl --fail http://localhost:80/_stcore/health || exit 1

# Run the application
ENTRYPOINT ["streamlit", "run"]
CMD ["census_app.py"]
