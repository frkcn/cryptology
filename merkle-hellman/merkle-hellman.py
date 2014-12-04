#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from fractions import gcd
import random

privateKey = [1, 2, 4, 8, 16, 32, 64, 128]
p = 263
r = 31

#check for super increasing list
def checkSuperInc(superList):
	sumSuperList = 0
	for i in range(len(superList)):
		if(i>0 and superList[i] < sumSuperList):
            		print "This list is not super increasing."
			sys.exit(0)
		sumSuperList += superList[i]
	print "This list is super increasing."

#check for modulo is right
def checkModulo(r,p):
	sumSuperList = sum(privateKey)
	if(p < sumSuperList):
	    	print "p integer must be bigger than sum of super increasing. p=" + `p` + " < " + `sumSuperList`
		sys.exit(0)
	while True:
		isGcd = gcd(r,p)
		if(isGcd != 1):
	    		print "r and p must be gcd each other."
			break
		else:
			break

#generate public key use private key
def generatePublicKey(privateKey):
	publicKey = []
	for i in range(len(privateKey)):
	    betaKey = privateKey[i] * r%p
	    publicKey.append(betaKey)
	return publicKey

#crypt to message use publick key
def crypt(message, publicKey):
	j = 0
	cryptedMessage = 0
	for i in range(len(message)):
	    j = i%len(publicKey)
	    cryptedMessage += int(message[i]) * publicKey[j]
	return cryptedMessage

#generate inverse modulo use r and p
def generateInverseModulo(r,p):
	inverseModulo = pow(r, p-2, p)
	return inverseModulo

#check for find first smaller number in list
def GetNextHighTemp(temp, templist):
    templist = (int(t) for t in templist if t != '')
    templist = [t for t in templist if t <= int(temp)]
    if templist: return max(templist)
    else: return temp

#decrypt message use inverse modulo and private key
def decrypt(cryptedMessage, inverseModulo, privateKey):
	dec=cryptedMessage*inverseModulo%p
	remaining = dec
	decList = []
	foo = 0
	while True:
	    foo = GetNextHighTemp(dec, privateKey)
	    decList.append(foo)
	    dec = dec - foo
	    if(dec == 0):
		break

	decrypt = []
	for i in range(len(privateKey)):
	    if(privateKey[i] in decList):
		decrypt.append(1)
	    else:
		decrypt.append(0)
	decryptedMessage = ''
	for i in decrypt:
	    decryptedMessage += `i`

	return decryptedMessage

#message reverse binary
def reverseBinary(message):
	messageList = []
	for i in range(len(message)):
		binaryCharacter = bin(ord(message[i]))[2:]
		if(len(binaryCharacter) == 6):
			messageList.append("00" + bin(ord(message[i]))[2:])
		else:
			messageList.append("0" + bin(ord(message[i]))[2:])
	return messageList

#binary reverse ascii
def reverseAscii(binaryList):
	asciiList = []
	for i in range(len(binaryList)):
		asciiList.append(chr(int(binaryList[i], 2)))
	asciiMessage = "".join(asciiList)
	return asciiMessage

#crypt all string
def cryptedFunc(messageList):
	cryptedMessageList = []
	checkSuperInc(privateKey)
	checkModulo(r,p)
	publicKey = generatePublicKey(privateKey)
	for i in range(len(messageList)):
		cryptedMessage = crypt(messageList[i], publicKey)
		cryptedMessageList.append(cryptedMessage)
	return cryptedMessageList

#decrypt all crypted numbers
def decryptedFunc(cryptedMessageList):
	decryptedMessageList = []
	for i in range(len(cryptedMessageList)):
		inverseModulo = generateInverseModulo(r,p)
		decryptedMessage = decrypt(cryptedMessageList[i], inverseModulo, privateKey)
		decryptedMessageList.append(decryptedMessage)
	return decryptedMessageList

message = "Hello World!"
print "message is : " + `message`
messageList = reverseBinary(message)
print "mesaj list is : " + `messageList`
cryptedMessage = cryptedFunc(messageList)
print "Crypted message : " + `cryptedMessage`
decryptedMessage = decryptedFunc(cryptedMessage)
print "Decrypted message : " + `decryptedMessage`
decryptedAscii = reverseAscii(decryptedMessage)
print decryptedAscii
