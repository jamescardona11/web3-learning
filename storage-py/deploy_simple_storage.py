import os
from solcx import compile_standard, install_solc
import json
from web3 import Web3
from dotenv import load_dotenv


install_solc("0.7.0")
load_dotenv("../.env")

with open("../storage-sol/SimpleStorage.sol") as file:
    simple_storage_file = file.read()

# compile our solidity

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "medatada", "evm.bytecode", "evm.sourceMap"],}
            }
        },
    },
    solc_version="0.7.0",
)

with open("compiled_sol.json", "w") as file:
    json.dump(compiled_sol, file)


# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# for connecting to ganache
w3 = Web3(Web3.HTTPProvider("http://0.0.0.0:7545"))
chain_id = 1337
my_address = "0x74392A5874ed63c48A1eCD6f40b3F3d3Cf356bf8"
private_key = os.getenv("PRIVATE_KEY")
print(private_key)


# create the contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)

# get the last transaction
nonce = w3.eth.getTransactionCount(my_address)
print("nonce", nonce)


# 1 - build a transaction
# 2 - sign
# 3 - send

# build
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)

# sign
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# send
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)


# working with contract, you send
# contract ABI
# contract Address
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

# call -> **simulate** making the call and getting the return value
# transact -> actually make a state change


# initial value for favorite number
print("call simulate", simple_storage.functions.retrieve().call())

store_transaction = simple_storage.functions.store(110).buildTransaction(
    {
        "gasPrice": w3.eth.gas_price,
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce + 1,
    }
)

signed_store_txn = w3.eth.account.sign_transaction(
    store_transaction, private_key=private_key
)

store_hash = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
store_tx_receipt = w3.eth.wait_for_transaction_receipt(store_hash)

w3.eth.contract(address=store_tx_receipt.contractAddress, abi=abi)


print("call simulate", simple_storage.functions.retrieve().call())
