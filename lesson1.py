# -*- coding: utf-8 -*-
print("hello world")

print("100 + 200 = " , 100 + 200)

# name = input()
# print(name)

# this is flag condition
a = 100
if a > 10:
    print(a)
else:
    print(-a)

print(10/3)
print(10//3)
print(10%3)

a = "123"
b = a
a = "234"
print(b)

a = 100
print(a)
a = "haha我是中文"
print(a)

# unicode

a = ord("A")
b = ord("是")
print(a,",",b)
a = chr(a)
b = chr(b)
print(a,",",b)

# bytes
x = b'ABC'
print(x.decode("ascii"))

x = "中文"
print(x.encode("UTF-8"))

len("aaaaa")

'Hello, %s' % 'world'