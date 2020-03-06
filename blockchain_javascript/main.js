const { Blockchain, Transaction } = require("./blockchain");

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
