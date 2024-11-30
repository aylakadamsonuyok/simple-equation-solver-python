inputfnc = input("f>>>")
answerfnc = int(input("=>>>"))

fnclist = list(inputfnc)

int_var = None
for item in fnclist:
    if item.isdigit():
        int_var = int(item)
        break

if int_var is not None:
    for item in fnclist:
        if item == "-":
            answeroffnc = answerfnc + int_var
            print("x = " + str(answeroffnc))
            break
    for item in fnclist:
        if item == "+":
            answeroffnc = answerfnc - int_var
            print("x = " + str(answeroffnc))
            break
    for item in fnclist:
        if item == "/":
            answeroffnc = answerfnc * int_var
            print("x = " + str(answeroffnc))
            break
    for item in fnclist:
        if item == "*":
            answeroffnc = answerfnc / int_var
            print("x = " + str(answeroffnc))
            break
else:
    print("There is no digit in function.")
