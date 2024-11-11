from currencies.dollar import Dollar
from currencies.euro import Euro
from currencies.ytl import Ytl
from moneys.money import Money

dollar = Money(100, Dollar)
euro = Money(100, Euro)
ytl = Money(100, Ytl)

print("Toplama İşlemleri")
try:
    result = dollar + 1
    print(result)
except Exception as e:
    print('yapacağın işşe sokim')

result = dollar + ytl
print(result)

result = euro + dollar
print(result)
result = euro + ytl
print(result)

result = ytl + dollar
print(result)
result = ytl + euro
print(result)

print("Çıkartma İşlemleri")
result = dollar - euro
print(result)
result = dollar - ytl
print(result)

result = euro - dollar
print(result)
result = euro - ytl
print(result)

result = ytl - dollar
print(result)
result = ytl - euro
print(result)

print("Çarpma İşlemleri")
result = dollar * euro
print(result)
result = dollar * ytl
print(result)

result = euro * dollar
print(result)
result = euro * ytl
print(result)

result = ytl * dollar
print(result)
result = ytl * euro
print(result)

print("Bölme İşlemleri")
result = dollar / euro
print(result)
result = dollar / ytl
print(result)

result = euro / dollar
print(result)
result = euro / ytl
print(result)

result = ytl / dollar
print(result)
result = ytl / euro
print(result)
