


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
            new_todos = [item.strip('\n') for item in todos]
            for index,item in enumerate(new_todos):
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("enter a todo to edit:  "))
            number = number - 1
            with open('todos') as file:
                new_todos = file.readlines()
            new_todo1 = input("enter a new todo function to add:  ")
            new_todos[number] = new_todo1 + '\n'
            with open('todos', 'w') as file:
                new_todos = file.writelines(new_todos)

        case "complete":
            num = int(input("Enter a todoindex to delete: "))
            with open('todos') as file:
                new_todos = file.readlines()
            index = num - 1
            todo_to_remove = new_todos[index].strip('\n')
            # todo_to_remove.pop(index)
            # print(todo_to_remove)
            new_todos.pop(index)
            with open('todos', 'w') as file:
                new_todos = file.writelines(new_todos)

        case "exit":
            break

print("bye!!!")