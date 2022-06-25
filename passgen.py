import random
passwordlen = int(input("Enter the length of password you require: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

#  Random sampling by joining the length of the password and the variable s
p = "".join(random.sample(s,passwordlen ))
print(p)