#!/bin/bash

# generates private key
openssl genrsa -out keys/private_key.pem 1024

# generates public key
openssl rsa -pubout -in keys/private_key.pem -out keys/public_key.pem

# install the necessary packages | python3
rm -r venv/
virtualenv -p python3 venv
. venv/bin/activate
pip install -r requirements.txt

# install the necessary packages | node
npm install

echo All Done...
