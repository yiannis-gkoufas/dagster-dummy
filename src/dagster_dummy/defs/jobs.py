from dagster import job, op, asset, AssetExecutionContext
import random
import time


# Simple ops and jobs
@op
def fetch_data():
    """Simulates fetching data from an external source."""
    data = [{"id": i, "value": random.randint(1, 100)} for i in range(10)]
    return data


@op
def process_data(data: list):
    """Processes the fetched data."""
    processed = [{"id": item["id"], "value": item["value"] * 2} for item in data]
    return processed


@op
def save_results(processed_data: list):
    """Simulates saving results."""
    return f"Saved {len(processed_data)} records"


@job
def data_pipeline_job():
    """A simple ETL-style job."""
    save_results(process_data(fetch_data()))


@op
def generate_report():
    """Generates a dummy report."""
    return {"report_id": random.randint(1000, 9999), "status": "complete"}


@job
def reporting_job():
    """A job that generates reports."""
    generate_report()


# Assets
@asset
def raw_numbers() -> list:
    """Generates a list of raw numbers."""
    return [random.randint(1, 100) for _ in range(20)]


@asset
def processed_numbers(raw_numbers: list) -> list:
    """Doubles all the raw numbers."""
    return [n * 2 for n in raw_numbers]


@asset
def summary_stats(processed_numbers: list) -> dict:
    """Computes summary statistics."""
    return {
        "count": len(processed_numbers),
        "sum": sum(processed_numbers),
        "avg": sum(processed_numbers) / len(processed_numbers),
        "min": min(processed_numbers),
        "max": max(processed_numbers),
    }
