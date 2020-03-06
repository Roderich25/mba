const EC = require("elliptic").ec;
const ec = new EC("secp256k1");

class KeyGenerator {
  constructor() {
    this.key = ec.genKeyPair();
  }

  getWalletAddress() {
    return this.key.getPublic("hex");
  }

  getPrivateKey() {
    return this.key.getPrivate("hex");
  }
}

module.exports.KeyGenerator = KeyGenerator;
