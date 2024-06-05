


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
            for index,item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("enter a todo to edit:  "))
            number = number - 1
            new_todo = input("enter a new todo function to add:  ")
            todos[number] = new_todo
        case "exit":
            break

print("bye!!!")