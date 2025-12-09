#!/bin/bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
python worker/monitor.py
