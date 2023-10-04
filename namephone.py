import re

regexp = re.compile(r"(?P<last>[-a-zA-Z]+),"
                    r" (?P<first>[-a-z-A-Z]+)"
                    r"( (?P<middle>([-a-zA-Z]+)))?"
                    r": (?P<phone>(\+\d{1,3}-)?(\d{3}-)?\d{3}-\d{4})"
                    )

pattern = re.compile(r"(?P<country_code>\+\d{1,3}-)?"
                     r"(\d{3}-)?\d{3}-\d{4}")

def add_usa_code(phone):
    usa_code = "+1-"
    #print(phone)
    if phone.group("country_code") is None:
        return usa_code + phone.group()
    else:
        return phone.group()


file = open("name_phone.txt", "r")

for line in file.readlines():
    #print(line)
    result = regexp.search(line)
    if result is None:
        print("Oops, I don't think this is a record")
    else:
        
        lastname = result.group("last")
        firstname = result.group("first")
        middlename = result.group("middle")
        if middlename is None:
            middlename = ""
        phonenumber = pattern.sub(add_usa_code, result.group("phone"))

        print("Name:", firstname, middlename, lastname,
              " Number:", phonenumber)

file.close()
