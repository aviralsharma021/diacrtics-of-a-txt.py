from random import randint
from time import *      #to use clock and sleep
def twistup(string):
            #defining twist function to diacriticize it randomly
    t1 = clock()
    new_string=""   #to store the new string
    ar1 = []        #to store the new string as a list
    dic = {}
    for i in string:
        new_string += i
        if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122): #or u could use.isalpha()
            new_string += chr(0x300 + randint(0,0x6F))
    ar1= list(new_string)
    t2 = clock()
    t= t2-t1        #to give the time taken
    print("\t {0} is the random diacriticezed line ".format(new_string))
    print("\t time taken in milli seconds ={0:.2f}\n\n".format(t*1000000))
    return ""
m = input("enter the text")
ar2 = list(m)  #to store the origina string as a list
l = len(m)
n = int(input("enter the number of times you want to diacriticize"))
print("\n\n")
for i in range(n):
    twistup(m)
    sleep(2)
print("original untwisted text=",m)
