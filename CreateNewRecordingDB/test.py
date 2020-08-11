import pickle
import os
'''
pubkey, prikey = rsa.newkeys(256)

message = b'Hello World'
enMessage = rsa.encrypt(message, pubkey)

print(enMessage)
print(pubkey, prikey)

message = rsa.decrypt(enMessage, prikey)
print(message)
'''





def readKey(pk):
	path = '/home/texet'
	if not os.path.exists(path):
		os.mkdir(path)
		os.chmod(path, 0o700)
	else:
		with open(path + '/key.dat', 'ab+') as file:
			pickle.dump(pk, file)


readKey('test')