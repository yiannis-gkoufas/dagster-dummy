FROM python:3.11

# Copy your Dagster project
COPY . /dagster_dummy

# This makes sure that logs show up immediately instead of being buffered
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

# Install dagster and any other dependencies your project requires
RUN pip install \
        dagster==1.12.12 \
        dagster-postgres==0.28.12 \
        dagster-k8s==0.28.12 \
        dagster-webserver==1.12.12

WORKDIR /dagster_dummy

# Install the project itself
RUN pip install -e .

# Expose the gRPC port for code location server
EXPOSE 3030
