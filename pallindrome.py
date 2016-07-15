str2=raw_input("enter the string")
start=raw_input("enter the start")
end=raw_input("enter the end")
start=int(start)
end=int(end)
str1=str2[(start+1):(end+2)]
print(str1)
list1=list(str1)
print(list1)
temp=list1
print(temp)
str3=str(temp)
list1.reverse()
print(list1)
str4=str(list1)
print(str4)
print(str3)
if str4==str3:
    print("pallindrome")
else:
    print("not a pallindrome")
