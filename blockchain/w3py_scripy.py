import web3


link = "https://rinkeby.infura.io/v3/8d3fe5be9fbb49aea3b9c18ef5083b10"

abi = [{"constant": False,
        "inputs": [{"internalType": "string", "name": "_name", "type": "string"},
                   {"internalType": "string", "name": "_email", "type": "string"},
                   {"internalType": "string", "name": "_login", "type": "string"},
                   {"internalType": "string", "name": "_hashedPassword", "type": "string"}],
        "name": "addUser", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function"},
       {"inputs": [], "payable": False, "stateMutability": "nonpayable", "type": "constructor"},
       {"constant": True, "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}], "name": "Users",
        "outputs": [{"internalType": "string", "name": "name", "type": "string"},
                    {"internalType": "string", "name": "login", "type": "string"},
                    {"internalType": "string", "name": "email", "type": "string"},
                    {"internalType": "string", "name": "hashedPassword", "type": "string"}],
        "payable": False, "stateMutability": "view", "type": "function"}]

address = "0x4B30Ba20098F206b27bEA0884ff3e5026c473fB5"


web3 = web3.Web3(web3.HTTPProvider(link))
contract = web3.eth.contract(abi=abi, address=web3.toChecksumAddress(address))

contract.functions.addUser('testName', 'testEmail', 'testLogin', 'testPassword').call()
