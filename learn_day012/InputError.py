from learn_day012.BusinessExceptions import AgeValidationError

list_check = [1,2,3,4]
age = 2
initial = 10
'''
try:
    risk_code - which might throw an error
except:
    code which executes when error occurred

1. Any number of except blocks
2. Specific first , generic later (Child Exception first, Parent Exception Later)
3. You can combine errors in except block with ,
4. Alias as will give exception object in except block

'''
def age_validation(age):
    if age > 18:
        print("Age is Valid")
    else:
        raise AgeValidationError("Age Validation Failed")

print("Length of List ", len(list_check))
try:
    # risky code 1
    print(list_check[2])
    # risky code 2
    print("Age Value post addition")
    new_age = age + 10
    age_validation(new_age)
    print(new_age)
    # risky code 3
    percentile = new_age / initial
    print(percentile)
except (IndexError, TypeError) as ex:
    print("Error cannot be avoided here", ex, type(ex))
except Exception as ex:
    print("Unknown Error Occurred", ex, type(ex))
else:
    print("Try block completes successfully")
    print("Email will be sent")
finally:
    print("Block of code which executes regardless of error")





