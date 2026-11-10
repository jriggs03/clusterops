import os
from storage import download_text, upload_text

BUCKET = os.environ["DEMO_BUCKET"]
INPUT_KEY = os.environ.get("INPUT_KEY", "logs/gpu-error.txt")
OUTPUT_KEY = os.environ.get("OUTPUT_KEY", "results/gpu-error-diagnosis.txt")


def analyze_log(log_text: str) -> str:
    """Part 3 replaces this with a vLLM call."""
    if "nvidia.com/gpu" in log_text:
        return "Diagnosis (stub): workload requested GPUs the cluster could not provide."
    return "Diagnosis (stub): no known issue matched."


def main():
    log_text = download_text(BUCKET, INPUT_KEY)
    print(f"[processor] read {len(log_text)} chars from s3://{BUCKET}/{INPUT_KEY}")

    diagnosis = analyze_log(log_text)

    upload_text(BUCKET, OUTPUT_KEY, diagnosis)
    print(f"[processor] wrote result to s3://{BUCKET}/{OUTPUT_KEY}")
    print(diagnosis)


if __name__ == "__main__":
    main()