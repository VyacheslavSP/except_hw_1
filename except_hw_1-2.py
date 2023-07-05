a=[1,5,7,9,10,5]
b=[2,7,15,4,0]
result=[]
if len(a)!=len(b):
    raise RuntimeError("Разная длина") 
for i in range(len(a)):
    if b[i]==0:
        raise RuntimeError ("Попытка совершить деление на 0")## для выполнения условия что ловится только Runtime
    result.append(a[i]/b[i])
print (result)