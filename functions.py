FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Gets a list of todos from txt file
    and returns list object
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """Gets a list as an argument and
       writes it into txt file
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == '__main__':
    print('Hello')