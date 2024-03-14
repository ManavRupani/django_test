FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /blog_dock
WORKDIR /blog_dock

ADD . /blog_dock/

# Install dependencies
RUN pip install -r requirements.txt

# Copy project