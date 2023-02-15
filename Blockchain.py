from RC6Encryption import RC6Encryption
from Crypto.Cipher import DES
from hashlib import sha256
from aes import AESCipher
from Block import Block
import textwrap
import time

'''
Remember block structure :
    (previous_hash, data)
where 
    data is the encrypted data using one of the algo : AES, DES, or RC6
'''
class Blockchain():
    def __init__(self):
            block_0 = self.create_genesis_block()
            self.chain = [block_0]
   
    def create_genesis_block(self):
        data = ''
        genesis_block = Block('0', data)
        return genesis_block

    def create_new_block(self, encrypted_text):
        '''
        this will be called for storing new data - of a bigger length
        hardcoding the message and key
        '''
        
        previous_block = self.chain[-1]
        new_block = Block(previous_block.hash, encrypted_text)
        return new_block