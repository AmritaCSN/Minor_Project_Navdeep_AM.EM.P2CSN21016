from Crypto.Cipher import DES
import time
import textwrap



key = '12345678'
key=key.encode('UTF-8')

des = DES.new(key, DES.MODE_ECB)

# message = 'a'*(2**20)
print("DES :")
print("Data Len\tEnc Time\tDec Time")
for i in range(20):
    message = 'a'*(2**i)
    message_chunks=textwrap.wrap(message, 8)
    if(len(message_chunks[-1])<8):
        padding = (16-len(message_chunks[-1]))*'0'
        message_chunks[-1] += padding

    enc_time = 0
    dec_time = 0
    full_cipher =''
    for chunk in message_chunks:
        chunk=chunk.encode('UTF-8')
        enc_start_time=time.time()
        cipher = des.encrypt(chunk)
        enc_stop_time=time.time()
        enc_time += enc_stop_time - enc_start_time
        full_cipher += str(cipher)

        dec_start_time=time.time()
        decipher = des.decrypt(cipher)
        dec_stop_time=time.time()
        dec_time += dec_stop_time - dec_start_time
        # full_plaintext += str(decipher)
    # print(full_cipher.split("'b'"))
    print(f"{len(message)}\t{enc_time}\t\t{dec_time}")