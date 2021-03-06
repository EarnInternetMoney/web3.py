from web3 import Web3
from web3._utils.rpc_abi import (
    RPC,
)
from web3.types import (
    TxParams,
    Wei,
)


def rpc_gas_price_strategy(web3: Web3, transaction_params: TxParams=None) -> Wei:
    """
    A simple gas price strategy deriving it's value from the eth_gasPrice JSON-RPC call.
    """
    return web3.manager.request_blocking(RPC.eth_gasPrice, [])
