
# todos = []

while True:
    userpromt = input("Enter show/add/exit : ")
    useraction = userpromt.strip()
    match useraction:
        case "add":
            tim = input("Enter a do list : ") +"\n"
            # todos.append(tim)
            file = open('editior.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(tim)
            # print(todos)

            file = open('editior.txt', 'w')
            file.writelines(todos)
            file.close()

        case "show" | "display":
            file = open('editior.txt', 'r')
            todos = file.readlines()
            for i,j in enumerate(todos):
                i += 1
                print(f"{i}-{j}")
        case "edit":
            number = int(input("enter a todo to edit:  "))
            number = number - 1
            new_todo = input("enter a new todo function to add:  ")
            todos[number] = new_todo
        case "exit":
            break

print("bye!!!")