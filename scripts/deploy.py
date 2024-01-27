from brownie import FundMe, MockV3Aggregator, config, network
from scripts.helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENT
from web3 import Web3

def deploy_fund_me():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        price_feed_addres = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_addres = MockV3Aggregator[-1].address
        print(f"Mocks Deployed")

    account = get_account()
    fund_me = FundMe.deploy(price_feed_addres,
                            {"from":account},
                            publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()