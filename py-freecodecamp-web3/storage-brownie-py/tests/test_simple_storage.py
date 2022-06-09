from brownie import SimpleStorage, accounts


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    # assert
    assert starting_value == 0


def test_update_storage():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(19, {"from": account})
    value = simple_storage.retrieve()
    # assert
    assert value == 19

