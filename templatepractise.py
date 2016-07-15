from string import Template

student=[("manisha",100),("shaunak",98),("rishabh",99)]

t=Template('Hi $name ,you have got $marks marks')
for i in student:
  print(t.substitute(name=i[0],marks=i[1]))
