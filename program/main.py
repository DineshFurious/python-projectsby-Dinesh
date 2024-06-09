import PySimpleGUI  as sg
from   zip_compress  import make_archive


label1 = sg.Text("Select Files to compress")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination folder")
input2 = sg.Input()
button2 = sg.FolderBrowse("Compress", key="folders")

button3 = sg.Button("Complete")
textmssg = sg.Text()
window = sg.Window("FILE COMPRESSOR APPLICATION",[[label1,input1,button1], [label2,input2, button2], [button3, textmssg]])



while True:
    events, values = window.read()
    print(events, values)
    filepath = values["files"]
    dest_dir = values["folders"]
    make_archive(filepath, dest_dir)
    window["com"].update(values="Compressed successfully")





window.close()