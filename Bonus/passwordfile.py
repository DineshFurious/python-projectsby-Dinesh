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

print(type(window))