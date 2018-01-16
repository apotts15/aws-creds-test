#!/bin/bash

export TEST_KEY=$(python -c 'import os; import base64; print(base64.b64encode(os.urandom(40)).strip())')
echo "Testing python..."
python pycreds.py
echo "Testing javasript..."
node jscreds.js
