


while True:
    userpromt = input("Enter show/add/exit : ")
    useraction = userpromt.strip()
    match useraction:
        case "add":

            tim = input("Enter a do list : ") + '\n'
            file = open("todos", 'r')
            todos = file.readlines()
            file.close()
            todos.append(tim)

            file = open('todos', 'w')
            todos = file.writelines(todos)
            file.close()
        case "show" | "display":
            file = open('todos', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # print(todos)  u will see \n in output if you print
            new_todos = [item.strip('\n') for item in todos]
            for index,item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("enter a todo to edit:  "))
            number = number - 1
            new_todo1 = input("enter a new todo function to add:  ")
            new_todos[number] = new_todo1
        case "exit":
            break

print("bye!!!")