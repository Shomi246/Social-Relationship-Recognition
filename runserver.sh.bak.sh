#!/bin/bash
# for linux
kill -9 $(lsof -t -i:8000)

# for mac
# kill $(lsof -t -i:8000)

python3.8 app.py