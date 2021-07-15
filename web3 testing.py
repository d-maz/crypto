from web3 import Web3
from hexbytes import HexBytes as hb

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/490ea888f340447996f0e0be3112abbf'))

latest_block = w3.eth.get_block('latest')

print(hb.hex(latest_block['transactions'][0]))