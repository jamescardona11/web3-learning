//1. import
const { ethers, run, network } = require("hardhat")

//2. async
async function main() {
  const SimpleStorageFactory = await ethers.getContractFactory(
    'SimpleStorage'
  )
  console.log('Deploying contract...')
  const simpleStorage = await SimpleStorageFactory.deploy()
  await simpleStorage.deployed()
  console.log(`Deployed contract to: ${simpleStorage.address}`);

  console.log(`network ${network.config}`)
  if (network.config.chainId === 4 && process.env.ETHERSCAN_API_KEY) {
    console.log('Start the verify');
    await simpleStorage.deployTransaction.wait(6)
    await verify(simpleStorage.address, [])
  }

  const currentValue = await simpleStorage.retrieve()
  console.log(`Current value is: ${currentValue}`);

  //Update
  const transactionResponse = await simpleStorage.store(91);
  await transactionResponse.wait(1)
  const updateValue = await simpleStorage.retrieve()
  console.log(`New Current value is: ${updateValue}`);

}




async function verify(contractAddress, args) {
  console.log('Verify contract etherscan')

  try {
    await run('verify:verify', {
      address: contractAddress,
      constructorArguments: args,
    })
  } catch (e) {
    if (e.message.toLowerCase().includes('Already verified'))
      console.log('Already verified')
    else
      console.log(e);
  }

}

//3. main
main()
  .then(() => process.exit(0))
  .catch((e) => {
    console.log(error)
    process.exit(1)
  })