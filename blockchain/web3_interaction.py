import web3
from contract_meta import *


web3 = web3.Web3(web3.HTTPProvider(link))
contract = web3.eth.contract(abi=abi, address=web3.toChecksumAddress(address))

print(contract.functions.sum(2, 3).call())
