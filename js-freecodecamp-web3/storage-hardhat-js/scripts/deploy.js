//1. import
const { ethers } = require("hardhat")

//2. async
async function main() {
  const SimpleStorageFactory = await ethers.getContractFactory(
    'SimpleStorage'
  );
  console.log('Deploying contract...');
  const simpleStorage = await SimpleStorageFactory.deploy();
  await simpleStorage.deployed(1);


}

//3. main
main()
  .then(() => process.exit(0))
  .catch((e) => {
    console.log(error);
    process.exit(1);
  })