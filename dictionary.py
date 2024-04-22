employee={"name":"divya","age":20,"salary":40000,"company":'EZTS'}
print(type(employee))
print("printing employee data")
print(employee)


Dict=dict({1:'mango',2:'apple',3:'banana'})
print(Dict)


Dict=dict([(4,'pragu'),(2,'sindh')])
print(Dict)
print(type(Dict))


#format specifier
employee={"name":"divya","age":20,"salary":40000,"company":'EZTS'}
print(type(employee))
print("printing employee data")
print("name:%s"%employee["name"])
print("age:%d"%employee["age"])
print("salary:%d"%employee["salary"])
print("company:%s"%employee["company"])


Dict[0]='pragu'
Dict[1]='sindhu'
Dict[2]='pavi'
print(Dict)

#adding extra key
Dict['Emp_ages']=20,34,53
print(Dict)
