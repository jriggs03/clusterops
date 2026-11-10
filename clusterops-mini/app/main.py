import os
from pathlib import Path

INPUT_FILE = os.environ.get("INPUT_FILE", "/data/gpu-error.txt")
OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def load_log(path: str) -> str:
    """Part 2 replaces this with an S3 download."""
    return Path(path).read_text()


def analyze_log(log_text: str) -> str:
    """Part 3 replaces this with a vLLM call."""
    if "nvidia.com/gpu" in log_text:
        return "Diagnosis (stub): workload requested GPUs the cluster could not provide."
    return "Diagnosis (stub): no known issue matched."


def save_result(text: str, out_dir: str) -> str:
    """Part 2 replaces this with an S3 upload."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    out_path = out / "diagnosis.txt"
    out_path.write_text(text)
    return str(out_path)


def main():
    log_text = load_log(INPUT_FILE)
    print(f"[processor] read {len(log_text)} chars from {INPUT_FILE}")

    diagnosis = analyze_log(log_text)

    path = save_result(diagnosis, OUTPUT_DIR)
    print(f"[processor] wrote result to {path}")
    print(diagnosis)


if __name__ == "__main__":
    main()