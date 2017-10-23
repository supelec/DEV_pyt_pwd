#!/usr/bin/python
# coding utf-8

import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    return hashlib.md5(password.encode()).hexdigest()


'''def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
'''
'''new_pass = raw_input('Please enter a password: ')
hashed_password = hash_password(new_pass)
print('The string to store in the db is: ' + hashed_password)
old_pass = raw_input('Now please enter the password again to check: ')
if check_password(hashed_password, old_pass):
    print('You entered the right password')
else:
    print('I am sorry but the password does not match')

'''
print hash_password('brazil')
#hash_object = hashlib.md5(b"brazil")
#print(hash_object.hexdigest())



#def hash_password(password):
#    return hashlib.md5(salt.encode() + password.encode()).hexdigest() + ':' + salt
