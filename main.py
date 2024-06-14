from web3 import Web3
from web3.middleware import geth_poa_middleware
from contract_info import abi, contract_address


W3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
W3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract = W3.eth.contract(address=contract_address, abi=abi)
print(contract.address)

address1 = Web3.to_checksum_address('0x9023089c0DCA7ff694f36Adb64780F2516320f5d')
address2 = Web3.to_checksum_address('0x48aC3aE7829d099C9F933d71f01807a5156eD541')
address3 = Web3.to_checksum_address('0x37c58de69677005fF78b9AC8017b8B4b850DE9E5')
address4 = Web3.to_checksum_address('0x94C598AD3342c836A000086AE9151Eea902DaA06')
address5 = Web3.to_checksum_address('0x3D272B97f93E85E4e56A67393a205efea99d0D76')

balance1 = W3.eth.get_balance(address1)
balance2 = W3.eth.get_balance(address2)
balance3 = W3.eth.get_balance(address3)
balance4 = W3.eth.get_balance(address4)
balance5 = W3.eth.get_balance(address5)

print(balance1)
print(balance2)
print(balance3)
print(balance4)
print(balance5)