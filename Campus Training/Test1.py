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

num=int(input("Enter a number : "))
s=0
for i in range(1,num+1):
    s=s+i

print(f"Sum of first {num} natural nos is {s}")


