FROM python:3.11

# Copy your Dagster project
COPY . /dagster_dummy

# This makes sure that logs show up immediately instead of being buffered
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Install dagster and any other dependencies your project requires
RUN pip install \
        dagster \
        dagster-postgres \
        dagster-k8s \
        dagster-webserver

WORKDIR /dagster_dummy

# Install the project itself
RUN pip install -e .

# Expose the port that your Dagster instance will run on
EXPOSE 80
