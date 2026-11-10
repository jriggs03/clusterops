import boto3

_s3 = boto3.client("s3")

def download_text(bucket: str, key: str) -> str:
    """Read an S3 object and return its contents as a string."""
    response = _s3.get_object(Bucket=bucket, Key=key)
    return response["Body"].read().decode("utf-8")


def upload_text(bucket: str, key: str, text: str) -> None:
    """Write a string to S3 as an object."""
    _s3.put_object(
        Bucket=bucket,
        Key=key,
        Body=text.encode("utf-8"),
        ContentType="text/plain",
    )