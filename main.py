from Blockchain import Blockchain
from RC6Encryption import RC6Encryption
from Crypto.Cipher import AES
from Crypto.Cipher import DES
from hashlib import sha256
from Crypto import Random
from aes import AESCipher
import threading
import textwrap
import hashlib
import base64
import time


def main():
    new_chain = Blockchain()
    # key='12345678'
    # message = 'a'*(2**20)
    message=''
    enc_time=0.0
    for mode in ['AES', 'DES', 'RC6']:
        print(f"================== Using {mode} ==============================")
        for i in range(20):
            key='12345678'
            enc_time=0.0
            message='a'*(2**i)
            if mode=='AES':
                test_object=AESCipher(key)
                enc_start_time=time.time()
                # message = 'a'*(2**20)
                encrypted_data=test_object.encrypt(message)
                # enc_time=time.time()-s_time
            
            elif mode=='DES':
                key=key.encode('UTF-8')
                des = DES.new(key, DES.MODE_ECB)
                
                message_chunks=textwrap.wrap(message, 8)
                if(len(message_chunks[-1])<8):
                    padding = (16-len(message_chunks[-1]))*'0'
                    message_chunks[-1] += padding

                enc_time = 0.0
                encrypted_data=''

                enc_start_time=time.time()
                for chunk in message_chunks:
                    chunk=chunk.encode('UTF-8')
                    encrypted_data += str(des.encrypt(chunk))
                    # enc_stop_time=time.time()
                    # enc_time += enc_stop_time - enc_start_time

            elif mode=='RC6':
                if(len(key)%16 != 0):
                    padding = (16-len(key)%16) * '0'
                    key += padding
                key=key.encode('UTF-8')
                rc6 = RC6Encryption(sha256(key).digest())

                message_chunks=textwrap.wrap(message, 16)
                if(len(message_chunks[-1])<16):
                    padding = (16-len(message_chunks[-1]))*'0'
                    message_chunks[-1] += padding

                encrypted_data = ''

                enc_start_time=time.time()
                for chunk in message_chunks:
                    chunk=chunk.encode('UTF-8')
                    encrypted_data += str(rc6.blocks_to_data(rc6.encrypt(chunk)))
                    # enc_stop_time=time.time()
                    # enc_time += enc_stop_time - enc_start_time
            
            new_block=new_chain.create_new_block(encrypted_data)
            new_chain.chain.append(new_block)
            enc_time=time.time()-enc_start_time
            print(f"{len(message)}\t{enc_time}")

        # for block in new_chain.chain:
        #     if(block.hash!='0'):#i.e. not the genesis block!
        #         encrypted_data=block.data
                    
        #         if(mode=='AES'):
        #             s_time=time.time()
        #             decrypted_data=test_object.decrypt(encrypted_data)
        #             dec_time=time.time()-s_time()
        #             print(f"Decryption Time : {dec_time}")
                
                # elif(mode=='DES'):
                #     key = '12345678'
                #     key=key.encode('UTF-8')
                #     des = DES.new(key, DES.MODE_ECB)
                #     encrypted_data=block.data
                #     data = encrypted_data.split("'b'")
                #     dec_time=0.0
                #     for i in data:
                #         i=i.replace("'","").encode()
                #         s_time=time.time()
                #         decipher = des.decrypt(i)
                #         dec_time+= time.time()-s_time
                #     print(f"Decryption Time : {dec_time}")
                
                # elif(mode=='RC6'):
                #     rc6 = RC6Encryption(sha256(key).digest())
                #     encrypted_data=block.data
                #     data = encrypted_data.split("'b'")
                #     dec_time=0.0
                #     for i in data:
                #         i=i.replace("'","").encode()
                #         s_time=time.time()
                #         decipher = rc6.blocks_to_data(rc6.decrypt(i))
                #         dec_time+= time.time()-s_time
                #     print(f"Decryption Time : {dec_time}")

if __name__ == '__main__':
    main()
#7738383000