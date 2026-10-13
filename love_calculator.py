
name1=input("Enter his name: ").lower()
name2=input("Enter her name: ").lower()
name=name1+name2
t=name.count('t')
r=name.count('r')
u=name.count('u')
e=name.count('e')
true=t+r+u+e
l=name.count('l')
o=name.count('o')
v=name.count('v')
e=name.count('e')
love=l+o+v+e
true_love=str(true)+str(love)

print(f"your love percentage is {true_love}%")

