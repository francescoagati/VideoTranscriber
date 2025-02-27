FROM mcr.microsoft.com/devcontainers/python:3.10-bullseye



# Install system dependencies for ffmpeg (needed for moviepy and whisper)
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    ffmpeg \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up a non-root user
ARG USERNAME=vscode

# Set the working directory
WORKDIR /workspace

# Install Python dependencies
COPY requirements.txt .
#RUN pip install --upgrade pip && pip install -r requirements.txt

# Switch to non-root user
USER $USERNAME