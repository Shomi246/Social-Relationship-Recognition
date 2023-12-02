#!/bin/bash
# for linux
# kill -9 $(lsof -t -i:8000)

# for mac
kill $(lsof -t -i:8000)

# Activate the conda virtual environment
conda activate /opt/anaconda3/envs/Vr1

python3 app.py