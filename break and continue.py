#use of break fo9r bunch of values
for rollno in range(1,101):
    if rollno>50:
        break
    else:
        print("allowed to symposium",rollno)
        
        
#use of continue to omit specified data
for rollno in range(1,101):
    if rollno==25 or rollno==50 or rollno==75:
        continue
    else:
        print("allowed to symposium",rollno)
        
        