from brownie import SimpleStorage, accounts, config


# -1 last deployment
def read_contract():
    simple_storage = SimpleStorage[-1]
    # go take the index thats one less than the length
    # ABI - Address

    print(simple_storage.retrieve)
    pass


def main():
    read_contract()
    pass
