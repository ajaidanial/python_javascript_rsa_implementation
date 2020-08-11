const fs = require("fs");
const JSEncrypt = require("node-jsencrypt");

// public key & private key
let public_key = fs.readFileSync("keys/public_key.pem", "utf8").toString();
let private_key = fs.readFileSync("keys/private_key.pem", "utf8").toString();

// encryption function
let encrypt = (string_to_encrypt) => {
    let encrypt = new JSEncrypt();
    encrypt.setPublicKey(public_key);
    return encrypt.encrypt(string_to_encrypt);
};

// decryption function
let decrypt = (string_to_decrypt) => {
    let decrypt = new JSEncrypt();
    decrypt.setPrivateKey(private_key);
    return decrypt.decrypt(string_to_decrypt);
};

// dummy test
let dummy_data = "Hey, I am working";
let encrypted_data = encrypt(dummy_data);
let decrypted_data = decrypt(encrypted_data);
console.log("Encrypted Data: ", encrypted_data);
console.log("Decrypted Data: ", decrypted_data);
