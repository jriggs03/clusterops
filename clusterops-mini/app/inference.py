#inference is essentially analyze_log

import os
from openai import OpenAI

MODEL_URL = os.environ.get("MODEL_URL", "http://localhost:11434/v1")
MODEL_NAME = os.environ.get("MODEL_NAME", "qwen2.5:1.5b")

_client = OpenAI(base_url=MODEL_URL, api_key="local-dev", timeout=60.0)

SYSTEM_PROMPT = """You are a Kubernetes cluster operations assistant.
Given a cluster log, reply in exactly this format:
Cause: <one sentence>
Evidence: <the log lines that show it>
Fix: <1-3 concrete steps>"""


def analyze_log(log_text: str) -> str:
    """Send a cluster log to the model server and return its diagnosis."""
    response = _client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": log_text},
        ],
        temperature=0.2,
        max_tokens=300,
    )
    return response.choices[0].message.content