from RC6Encryption import RC6Encryption
from hashlib import sha256
import textwrap
import time

key='12345678'
# message=''
if(len(key)%16 != 0):
	padding = (16-len(key)%16) * '0'
	key += padding
key=key.encode('UTF-8')

rc6 = RC6Encryption(sha256(key).digest())
print('RC6')
print("Message Len\tEncTime\tDecTime")
message = 'a'*(2**20)
for i in range(20):
	message = 'a'*(2**i)
	message_chunks=textwrap.wrap(message, 16)

	if(len(message_chunks[-1])<16):
		padding = (16-len(message_chunks[-1]))*'0'
		message_chunks[-1] += padding

	# print(message_chunks)

	# full_cipher=''
	# full_plaintext=''
	enc_time = 0
	dec_time = 0

	for chunk in message_chunks:
		chunk=chunk.encode('UTF-8')
		enc_start_time=time.time()
		cipher = rc6.blocks_to_data(rc6.encrypt(chunk))
		enc_stop_time=time.time()
		enc_time += enc_stop_time - enc_start_time
		# full_cipher += str(cipher)

		dec_start_time=time.time()
		decipher = rc6.blocks_to_data(rc6.decrypt(cipher))
		dec_stop_time=time.time()
		dec_time += dec_stop_time - dec_start_time
		# full_plaintext += str(decipher)

	print(f"{len(message)}\t{enc_time}\t\t{dec_time}")


# print(f"Encrypted Text for {message}\t{full_cipher}")
# print(f"Decrypted Text for {full_cipher}\t{full_plaintext}")