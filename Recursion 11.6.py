##########FUNCTION############
#If the length of the text is less than the length
#of the string then return false and if
#the text starts with the string then return true
#else stop from reaching max recursion depth
def find(text, string):
    if (len(text) < len(string)):
        print(string, " does not match with ", text, " making it")
        return False
    if text.startswith(string):
        print(string, " does match with ", text, " making it")
        return True
    else:
        return find(text[1:], string)

print(find("Mississippi", "sis"))
print(find("Soviet",  "iet"))
print(find('Soviet', 'te'))
