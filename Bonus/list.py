
todos = []

while True:
    userpromt = input("Enter show/add/exit : ")
    useraction = userpromt.strip()
    match useraction:
        case "add":
            tim = input("Enter a do list : ")
            todos.append(tim)
        case "show" | "display":
            for i in todos:
                print(i)
        case "edit":
            number = int(input("enter a todo to edit:  "))
            number = number - 1
            new_todo = input("enter a new todo function to add:  ")
            todos[number] = new_todo
        case "exit":
            break

print("bye!!!")