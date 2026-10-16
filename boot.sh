#!/usr/bin/env bash
set -euo pipefail

exec gunicorn -b 0.0.0.0:5450 \
  --access-logfile - \
  --error-logfile - \
  --chdir /app \
  trackerr.backend.trackerr:app