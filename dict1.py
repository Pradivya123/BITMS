'''def balaji():
    return "This is my bank balance"
test_dict={"fname": balaji, "age": 50,"address":"salem"}#here balaji is a function

print("The original dictionary is :"+str(test_dict))
res=test_dict['fname']()
print("The required call result:"+str(res))'''


def balaji(a,b):
    print("Result is =",a+b)
test_dict={"fname": balaji, "age": 50,"address":"salem"}#here balaji is a function

print("The original dictionary is :"+str(test_dict))
res=test_dict['fname'](10,20)
print("The required call result:"+str(res))