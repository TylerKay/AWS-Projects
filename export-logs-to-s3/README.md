# Export Log to S3 Lab

This project uses CloudWatch, Lambda, and S3 to design a simple logging mechanism that saves logs into a s3 bucket.

1. When logexportlambda.py is executed in lambda services, it will trigger a export response from cloudwatch and save the logs into a s3 bucket.

![./export-logs-to-s3.svg](./export-logs-to-s3.svg)

---
