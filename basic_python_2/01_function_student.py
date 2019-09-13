def input_student():
    L = []
    while True:
        name = input("please enter any student's name: ")
        if not name:
            break
        age = input("please enter this student's age: ")
        score = input("please enter this student's score: ")
        d={}
        d["name"] = name
        d["age"] = age
        d["score"] = score
        L.append(d)
    return L

def output_student(L):
    print("+------------+-----+-----+")
    print("|    name    | age |score|")
    print("+------------+-----+-----+")
    for d in L:
        t = (d["name"].center(12),
            str(d["age"]).center(5),
            str(d["age"]).center(5))
        line = "|%s|%s|%s|" % t
        print(line)
    print("+------------+-----+-----+")

L = input_student()
output_student(L)