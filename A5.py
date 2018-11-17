#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 21:11:50 2018
@author: HP
"""
 
import time
import base64
import codecs
 
class A5(object):
    
    def __init__(self, key=None):
        if not key:
            self.kList = self.String_to_BitList('helloyou')
        self.kList = self.String_to_BitList(key)
        self.A = list(self.kList[:19])
        self.B = list(self.kList[19:41])
        self.C = list(self.kList[41:64])
        
    #字符串转二进制列表
    def String_to_BitList(self, data):
        data = [ord(c) for c in data]
        result = []
        for num in data:
            i = 7
            while i>=0:
                if num & (1<<i) !=0:
                    result.append(1)
                else:
                    result.append(0)
                i -= 1
        return result
    #移位并产生密钥
    def create_key(self):
        result = []     
        for i in range(8):
            result.append(str(self.A[18]^self.B[21]^self.C[22]))
            alist = [self.A[9], self.B[11], self.C[11]]
            alist.sort()
            s = alist[1]
            if self.A[9]==s:
                self.A.insert(0, self.A[13]^self.A[16]^self.A[17]^self.A[18])
                self.A.pop()
            if self.B[11]==s:
                self.B.insert(0, self.B[12]^self.B[16]^self.B[20]^self.B[20]^self.B[21])
                self.B.pop()
            if self.C[11]==s:
                self.C.insert(0, self.C[17]^self.C[18]^self.C[21]^self.C[22])
                self.C.pop()
        result.reverse()
        return int(''.join(result), 2)
                
    def do_crypt(self, string):
        result = []
        for s in string:
            k = self.create_key()
            result.append(chr(ord(s)^k))
        return ''.join(result)
        
#读取文本字符串
def getPlainText(route):
	with codecs.open(route,'r') as f:
		plainText=f.read()
	return plainText
        
if __name__=='__main__':
    prompt = """
(e)ncrypt
(d)ecrypt
(q)uit
plesae enter your choice:"""
    while True:
        choice = input(prompt)
        
        if choice == 'q':
            break
        elif choice == 'e':
            print("***************开始加密******************")
            fname = input("enter file name: ")
            key = input("enter the key: ")
            start = time.time()
            plaintext = getPlainText(fname)
            a5 = A5(key)
            ciphertext = a5.do_crypt(plaintext)
            ciphertext = base64.b64encode(ciphertext.encode(encoding='utf-8')).decode()
            f = open(fname, 'w')
            f.write(ciphertext)
            f.close()
            end = time.time()
            print("加密时长 %.2f s" %(end-start))
        elif choice == 'd':
            print("****************开始解密***************")
            fname = input("enter file name: ")
            key = input("enter the key: ")
            start = time.time()
            base64_str = getPlainText(fname)
            ciphertext = base64.b64decode(base64_str.encode(encoding="utf-8")).decode()
            a5 = A5(key)
            plaintext = a5.do_crypt(ciphertext)
            f = open(fname, 'w')
            f.write(plaintext)
            f.close()
            end = time.time()
            print("解密时长 %.2f s" %(end-start))
        else:
            print("valid input, please try again")
            
            
    
        
