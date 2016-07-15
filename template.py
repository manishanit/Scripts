Python 2.7.10 (default, May 23 2015, 09:44:00) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> string1="manisha is a very good girl"
>>> string11.split(" ")

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    string11.split(" ")
NameError: name 'string11' is not defined
>>> split(string1,' ')

Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    split(string1,' ')
NameError: name 'split' is not defined
>>> string1.split()
['manisha', 'is', 'a', 'very', 'good', 'girl']
>>> string1.split(' ',1)
['manisha', 'is a very good girl']
>>> variable='15'
>>> print("the variable in float is%f"%variable)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print("the variable in float is%f"%variable)
TypeError: float argument required, not str
>>> print("the variable in float is=%f"%(variable))

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("the variable in float is=%f"%(variable))
TypeError: float argument required, not str
>>> variable=int(variable)
>>> print("the variable in float is=%f"%(variable))
the variable in float is=15.000000
>>> 
