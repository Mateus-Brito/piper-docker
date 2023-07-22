#!/usr/bin/env bash

echo "====================================================="

echo "start copying..."

GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/rhasspy/piper-voices /projects/piper-voices

echo "copy large files..."

cd /projects/piper-voices

git lfs pull --include "pt/*"

echo "Downloading the project, it may take a while..."

wget https://raw.githubusercontent.com/rhasspy/piper/31a7d269ffa3764392a4ecff7eae6f1b04e62c52/src/python_run/piper/__init__.py -O /projects/piper-api/piper_api/piper.py

chown -R dev:dev /projects

echo "Downloading completed"
