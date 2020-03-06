const EC = require("elliptic").ec;
const ec = new EC("secp256k1");
const { Blockchain, Transaction } = require("./blockchain");
const { KeyGenerator } = require("./keygenerator");

// Blockchain initialization
let rodrigoCoin = new Blockchain();

// Keys
pablo = new KeyGenerator();
renata = new KeyGenerator();
miner = new KeyGenerator();

// Transactions
const trans1 = new Transaction(
  miner.getWalletAddress(),
  pablo.getWalletAddress(),
  10
);
trans1.signTransaction(miner.key);
rodrigoCoin.addTransaction(trans1);

const trans2 = new Transaction(
  miner.getWalletAddress(),
  renata.getWalletAddress(),
  10
);
trans2.signTransaction(miner.key);
rodrigoCoin.addTransaction(trans2);

// Mining
console.log("Starting the miner...");
rodrigoCoin.miningPendingTransactions(miner.getWalletAddress());

// More transactions
const trans3 = new Transaction(
  pablo.getWalletAddress(),
  renata.getWalletAddress(),
  5
);
trans3.signTransaction(pablo.key);
rodrigoCoin.addTransaction(trans3);

// Mining
console.log("Starting the miner...");
rodrigoCoin.miningPendingTransactions(miner.getWalletAddress());

// Balance
console.log(
  "Pablo balance:\t",
  rodrigoCoin.getBalanceOfAddress(pablo.getWalletAddress())
);
console.log(
  "Renata balance:\t",
  rodrigoCoin.getBalanceOfAddress(renata.getWalletAddress())
);

// Mining
console.log("Starting the miner...");
rodrigoCoin.miningPendingTransactions(miner.getWalletAddress());

// Miner balance
console.log(
  "Miner balance:\t",
  rodrigoCoin.getBalanceOfAddress(miner.getWalletAddress())
);

// Tampering attemp
//rodrigoCoin.chain[1].transactions[0].amount = 12345;

// Test
console.log("Is chain valid?", rodrigoCoin.isChainValid());
