#start app 
start_prompt=['A) View Todo Lists',"B) New Todo"]
todos=['gym']

def start_app():
    print('Reply with A or B\n----------------\n')
    for prompt in start_prompt:
        print(prompt)
    user_inp=input()
    if user_inp.upper()=='A':
       view_todo()
    elif user_inp.upper()=='B':
        new_todo=input("Enter To Do : \n")
        add_new_todo(new_todo)
    else:
        start_app()

#view to do
def view_todo():
    if len(todos)==0:
        print('You have no todos!')
    else:
        print('----------------\nYour ToDo Lists : ')
        for todo in todos:
            print(f"{str(todos.index(todo)+1)}.{todo}")

#Add new todo
def add_new_todo(todo):
    todos.append(todo)
    view_todo()


start_app()