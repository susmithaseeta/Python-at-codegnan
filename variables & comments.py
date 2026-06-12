Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1,num2,num3=10,20,30
print(num1)
10
>>> print(num2)
20
>>> print(num3)
30
>>> print("num3")
num3
>>> num1=num2=num3=10
>>> print(num1)
10
>>> ptint(num2)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ptint(num2)
NameError: name 'ptint' is not defined. Did you mean: 'print'?
>>> print(num2)
10
>>> print(num3)
10
>>> print(num2,num3)
10 10
>>> print(id(num1))
140716990850248
>>> print(id(num2))
140716990850248
>>> a,b=10,20
>>> print(id(a),id(b))
140716990850248 140716990850568
>>> a,b=256,256
>>> print(id(a),id(b))
140716990858120 140716990858120
>>> a,b=257,257
>>> print(id(a),id(b))
2996797037680 2996797037680
>>> a,b=258,258
>>> print(id(a),id(b))
2996797037840 2996797037840
>>> a=10
>>> b=20
>>> a,b=b,a
>>> print(a)
20
>>> print(b)
10
>>> a,b=10,20
>>> print(id(a),id(b))
140716990850248 140716990850568
>>> a,b=b,a
>>> print(id(a),id(b))
140716990850568 140716990850248
>>> print(a,b)
20 10
