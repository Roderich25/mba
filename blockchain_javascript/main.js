const SHA256 = require("crypto-js/sha256");

class Transaction {
  constructor(fromAddress, toAddress, amount) {
    this.fromAddress = fromAddress;
    this.toAddress = toAddress;
    this.amount = amount;
  }
}

class Block {
  constructor(timestamp, transactions, previousHash = "") {
    this.nonce = -1;
    this.timestamp = timestamp;
    this.transactions = transactions;
    this.previousHash = previousHash;
    this.hash = this.calculateHash();
  }

  calculateHash() {
    return SHA256(
      this.nonce +
        this.previousHash +
        this.timestamp +
        JSON.stringify(this.data)
    ).toString();
  }

  mineBlock(difficulty) {
    while (
      this.hash.substring(0, difficulty) !== Array(difficulty + 1).join("0")
    ) {
      this.nonce++;
      this.hash = this.calculateHash();
    }
    console.log("Block mined @ " + this.nonce + " : " + this.hash);
  }
}

class Blockchain {
  constructor() {
    this.chain = [this.createGenesisBlock()];
    this.difficulty = 6;
    this.pendingTransactions = [];
    this.miningReward = 10;
  }

  createGenesisBlock() {
    return new Block("01/01/2020", "Genesis block", "0");
  }

  getLatestBlock() {
    return this.chain[this.chain.length - 1];
  }

  miningPendingTransactions(miningRewardAddress) {
    let block = new Block(Date.now(), this.pendingTransactions);
    block.mineBlock(this.difficulty);

    console.log("Block sucessfully mined!");
    this.chain.push(block);

    this.pendingTransactions = [
      new Transaction(null, miningRewardAddress, this.miningReward)
    ];
  }

  createTransaction(transaction) {
    this.pendingTransactions.push(transaction);
  }

  getBalanceOfAddress(address) {
    let balance = 0;
    for (const block of this.chain) {
      for (const trans of block.transactions) {
        if (trans.fromAddress === address) {
          balance -= trans.amount;
        }
        if (trans.toAddress === address) {
          balance += trans.amount;
        }
      }
    }
    return balance;
  }

  addBlock(newBlock) {
    newBlock.previousHash = this.getLatestBlock().hash;
    //newBlock.hash = newBlock.calculateHash();
    newBlock.mineBlock(this.difficulty);
    this.chain.push(newBlock);
  }

  isChainValid() {
    for (let i = 1; i < this.chain.length; i++) {
      const currentBlock = this.chain[i];
      const previousBlock = this.chain[i - 1];
      if (currentBlock.hash !== currentBlock.calculateHash()) {
        return false;
      }
      if (currentBlock.previousHash !== previousBlock.calculateHash()) {
        return false;
      }
      return true;
    }
  }
}

let rodrigoCoin = new Blockchain();
rodrigoCoin.createTransaction(new Transaction(null, "address1", 100));
rodrigoCoin.createTransaction(new Transaction(null, "address3", 100));
rodrigoCoin.createTransaction(new Transaction("address1", "address2", 100));
rodrigoCoin.createTransaction(new Transaction("address2", "address1", 10));

console.log("\nStarting the miner...\n");
rodrigoCoin.miningPendingTransactions("miner-address");

console.log(
  "\nMiner balance:\t",
  rodrigoCoin.getBalanceOfAddress("miner-address")
);

rodrigoCoin.createTransaction(new Transaction("address3", "address1", 50));
rodrigoCoin.createTransaction(new Transaction("address3", "address2", 25));

console.log("\nStarting the miner again ...\n");
rodrigoCoin.miningPendingTransactions("miner-address");

console.log(
  "\nMiner balance:\t",
  rodrigoCoin.getBalanceOfAddress("miner-address")
);
console.log(
  "\nAddress1 balance:\t",
  rodrigoCoin.getBalanceOfAddress("address1")
);
console.log(
  "\nAddress2 balance:\t",
  rodrigoCoin.getBalanceOfAddress("address2")
);
//RodrigoCoin.addBlock(new Block(1, "2/1/2020", { amount: 5 }));
//RodrigoCoin.addBlock(new Block(2, "3/1/2020", { amount: 7 }));
//console.log(JSON.stringify(RodrigoCoin, null, 4));
//console.log("\nIs this blockchain valid? " + RodrigoCoin.isChainValid() + "\n");
