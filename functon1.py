# funciton.py

def setValue(newValue):
    x=newValue
    print("지역변수",x)

retValue=setValue(10)
print(retValue)

def swap(x,y):
    return y,x

print(swap(3,4))