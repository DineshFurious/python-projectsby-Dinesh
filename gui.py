import FreeSimpleGUI as sg

import functions
from  functions import get_todos


text = sg.Text("mytodo app")
input_box = sg.InputText("enter ", key="todo")
button1 = sg.Button("Add")
button2 = sg.Button("Edit")
list_box = sg.Listbox(get_todos(), key="todos", enable_events=True, size=[45, 10])

window = sg.Window('TODO APPLICATION LIST',
                   layout=[[text], [input_box, button1],
                           [list_box, button2]],
                   font=['Helvetica', 15])

while True:

    events, values = window.read()
    print(events)
    print(values)

    match events:
        case 'Add':
            current_todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            current_todos.append(new_todo)
            functions.write_todos(current_todos)
            window['todos'].update(values=current_todos)
            window['todo'].update(value='')
        case 'Edit':
            ins = values['todo']
            in_box_sel = values['todos'][0]
            present = functions.get_todos()
            index_value = present.index(in_box_sel)
            present[index_value] = ins
            live = functions.write_todos(present)
            window['todos'].update(values=live)
            # window['todo'].update(value="")
        # case WIN_CLOSED:
        #      break


window.close()