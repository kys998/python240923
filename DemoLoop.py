# DemoLoop.py

value=5
while value>0:
    print(value)
    value-=1

print("--- for in --- ")
lst=[100, 3.14, "demo"]
for ietm in lst:
    print(ietm)

print("--- range()함수 --- ")
years=list(range(2000,2025))
print(years)
days=list(range(1,32))
print(days)

print("리스트 컴프리헨션")
lst=list(range(1,11))
print(lst)

