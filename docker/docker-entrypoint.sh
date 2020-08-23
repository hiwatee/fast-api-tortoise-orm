#!/bin/bash
set -eu

cd /code
uvicorn main:app --host 0.0.0.0 --reload