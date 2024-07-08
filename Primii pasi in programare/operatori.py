'''
Operatori:
aritmetici: +, -, *=(inmultit), /=(impartit) , %=(modulo)
de comparare: < >, ==, !=, >=, <=
logici: and, or, !

'''

a = 3
b = 5

print(a+b) # 3+5 = 8
print(a ==b) # a este egal cu b? = false
print (a<b and a<4) # true si true
print(a < b or a < 2)

mama = True
tata = False
bunicu = False
bunica = False

print(mama or tata or (bunicu and bunica))