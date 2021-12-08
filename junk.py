todo_list = [1,2,3,4,5]

check = todo_list.append(2)

print(type(check))
print(todo_list)


def validate_priority(value):
    if not value in [0,1,2]:
        print("u re very correct")
    
    print("foto")


validate_priority(0)