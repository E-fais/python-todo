#start app 
start_prompt=['A) View Todo Lists',"B) New Todo"]
todos=[] 

def start_app():
    load_saved_file()
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
            print(f"{(todos.index(todo)+1)}.{todo}")

#Add new todo
def add_new_todo(todo):
    todos.append(todo)
    view_todo()
    save_todo()
    

# save to a file    
def save_todo():
    with open('Todos.txt','w') as file:
     for todo in todos:
        file.write(todo +"\n")

# load saved file
def load_saved_file():
    try:
     with open('Todos.txt','r') as file:
        for line in file:
            todos.append(line.strip()) 
    except FileNotFoundError:
       pass

start_app()