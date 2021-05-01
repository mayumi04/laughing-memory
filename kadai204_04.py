import re

x = input("文字を入力してください。")

if re.fullmatch('[0-9]+', x) :
    print("The character strings are all half-width numbers.")
elif re.fullmatch('[0-9a-zA-Z]+', x) :
    print("The character strings are all alphanumeric characters.")
elif re.fullmatch('[\w\s\.\']+', x) :
    print("The character strings are all half-width numbers.")
elif re.fullmatch('^0\d(-\d{4}|\d-\d{3}|\d\d-\d\d|\d{3}-\d)-\d{4}$', x) or re.fullmatch('^0[789]0-\d{4}-\d{4}$', x):
    print("The string is a phone number.")
else : 
    print("The string is neither.")