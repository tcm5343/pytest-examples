# pytest-examples

Collection of Pytest examples. Each file is designed to demonstrate something specific.

`s3.py` - How to mock a module-level imported constant (boto3 client).

## Getting Started

This project uses Docker to simplify setup. If you are familiar with Python, you can set it up manually. 

*. `docker compose build app --no-cache` - builds docker image from scratch
*. `docker compose run --rm app bash` - opens a terminal in the container
*. `docker compose run --rm app ruff format --check .` - check lint
*. `docker compose run --rm app ruff format .` - format project
*. `docker compose run --rm app pytest` - runs all tests
