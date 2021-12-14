

def validate_age(age):
    status = False
    if (int(age) > 0) and (str(age).isnumeric()):
        if (age >= 18) and (age < 121):
            status = True
        return status
    else:
        raise ValueError("Invalid Age Value Provided")


def validation_zipcode(zipcode):
    if len(str(zipcode)) == 5:
        return True
    else:
        return False