'''try:
    even_numbers=[2,4,6,8]
    print(even_numbers)

except ZeroDivisionError:
    print('denominator cannot be zero')'''

#assertion error
'''try:
    num=int(input("Enter the number"))
    assert num%2==0
except:
    print("not an even number!")
else:
    reciprocal=1/num
    print(reciprocal)'''

#finally
file_path='divya.txt'
try:
    with open(file_path,"r")as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print('File not found!')
except Exception as e:
    print(f"An error occurred:{e}")
finally:
    print("Closing the file")
   