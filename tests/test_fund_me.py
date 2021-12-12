from brownie import FundMe, network, accounts, exceptions
from scripts.helpful_scripts import (
    get_account,
    LOCAL_BLOCKCHAIN_ENVI,
)
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    acc = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    tx = fund_me.fund({"from": acc, "value": entrance_fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(acc.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": acc})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(acc.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVI:
        pytest.skip("only for local testing")
    acc = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    # we want this to happen -> VME error aaye jab bhi owner ke alava koi aur withdraw kare.
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
