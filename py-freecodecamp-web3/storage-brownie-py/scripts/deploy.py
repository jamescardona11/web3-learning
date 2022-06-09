from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})

    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(19, {"from": account})
    transaction.wait(1)

    updated_stored_value = simple_storage.retrieve()

    print(stored_value)
    print(updated_stored_value)

    pass


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    pass


def main():
    deploy_simple_storage()
    pass

