def insertComma(listValue):
    length = len(listValue)
    string = ""
    for i in range(length):
        if i != (length - 1):
            string += listValue[i] + ", "
        else:
            string += "and " + listValue[i]
    print(string)

spam = ["apples", "bananas", "tofu", "cats"]

insertComma(spam)
