'''
name='Ayan Kumar Maji'
age=22
print(f"My name is {name} and I'm {age} years old")
n=6
f=1
for i in range(1,n+1):
    f=f*i

print(f"Factorial of {n} is {f}")

'''
'''
n=int(input("Enter a number: "))
i=1
while i <= 10:
    print(f"{n}X{i}={n*i}")
    i+=1

'''

'''
n=int(input("Enter the number : "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1

if c==2:
        print(f"{n} is a prime number")
else:
        print(f"{n} is not prime number")

'''
'''
num=int(input("Enter a number of user's choice : "))
s=0
for i in range(1,num+1):
    s=s+i

print(f"Sum of first {num} natural nos is {s}")

fact = lambda n: 1 if n==1 else n*fact(n-1)
print(fact(5))

'''

"""
    Decorators
"""

def func(sum):
    def func_1(a,b):
        print("Start adding")
        sum(a,b)
        print("Finished adding")
    return func_1

@func
def add(x,y):
    s=x+y
    print(f"Sum is {s}")

add(15,8)


