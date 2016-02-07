import re
# Password validator ensures that password has
# at least 8 cahracters and1number


def password_validator(pw_to_check):
    regex_validation = re.compile("^(?=.*\d)(?=.*[a-z])[a-zA-Z0-9]{8,}$")

    if regex_validation.match(pw_to_check):
        return True
    else:
        return False


