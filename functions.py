FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        local_file = file.readlines()
        return local_file


def write_todos(todos, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos)