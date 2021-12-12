from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVI,
)


def fund():
    acc = get_account()
    fund_me = FundMe[-1]
    entrance_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    print("Funding")
    fund_me.fund({"from": acc, "value": entrance_fee})


def withdraw():
    acc = get_account()
    fund_me = FundMe[-1]
    fund_me.withdraw({"from": acc})


def main():
    fund()
    withdraw()
