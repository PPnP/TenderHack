link = "https://ropsten.infura.io/v3/b35c450d1f3047a8a2799c7cabd174f7"

address = "0xdff18078D98d6ab796280F7e1D89f9AB29022d35"

abi = [
    {
        "constant": False,
        "inputs": [
            {"internalType": "int256", "name": "a", "type": "int256"}
        ],
        "name": "addNumber",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {"internalType": "int256", "name": "a", "type": "int256"},
            {"internalType": "int256", "name": "b", "type": "int256"}
        ],
        "name": "sum",
        "outputs": [
            {"internalType": "int256", "name": "b", "type": "int256"}
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "countOfData",
        "outputs": [
            {"internalType": "int256", "name": "", "type": "int256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {"internalType": "int256", "name": "", "type": "int256"}
        ],
        "name": "dataStorage",
        "outputs": [
            {"internalType": "int256", "name": "", "type": "int256"}
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]
