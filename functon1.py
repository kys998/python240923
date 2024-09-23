# funciton.py

def setValue(newValue):
    x=newValue
    print("지역변수",x)

retValue=setValue(10)
print(retValue)

def swap(x,y):
    return y,x


print(swap(3,4))

def times(a=10, b=20):
    return a*b

print(times())
print(times(5))
print(times(5,6))

x=5
def func1(a):
    return a+x
print(func1(1))

print(func2(1))