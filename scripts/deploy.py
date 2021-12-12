from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVI,
)
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    """ 
    we will have to pass the price feed address to the fundme contract
    If you are on a persistent network like rinkeby, use associated address. Otherwise, deploy mocks.
    """

    # if we are not on a development network, pull the price feed from the active network.
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVI:
        pricefeed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        # list me se most recent uthao aur uska address do
        pricefeed_address = MockV3Aggregator[-1].address
    fundme = FundMe.deploy(
        pricefeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fundme.address}")
    return fundme


def main():
    deploy_fund_me()
