let fs = require("fs");

// public key
let public_key = fs.readFileSync("keys/public_key.pem", "utf8").toString();

// private key
let private_key = fs.readFileSync("keys/private_key.pem", "utf8").toString();
