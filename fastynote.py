#! /usr/bin/env python3.6

try:
    import tkinter
except ModuleNotFoundError:
    print("Your Python installation does not include tkinter.\nInstall it or this program will not work.")
    exit(1)
import os
import sys


app_name = "Fastynote"
app_data_dir = os.path.expanduser('~/.' + app_name)
data_file_path = os.path.join(app_data_dir, 'content')

try:
    if not os.path.isdir(app_data_dir):
        os.mkdir(app_data_dir)

    if not os.path.isfile(data_file_path):
        open(data_file_path, 'w').close()

    if len(sys.argv) > 1 and sys.argv[1] in ('-u', '--uninstall'):
        os.remove(data_file_path)
        os.rmdir(app_data_dir)
        os.remove(__file__)
        print('Pynote has been successfully uninstalled')
        sys.exit()

except PermissionError:
    print("Not enough right !")
    exit(1)
except Exception as e:
    print("Unknown error !", e)
    exit(1)


class PyNote(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title(app_name)
        self.text_area = tkinter.Text(self, width=35, height=15)
        self.text_area.focus_force()
        with open(data_file_path) as f:
            self.text_area.insert('1.0', f.read())
        self.text_area.pack()

    def destroy(self):
        with open(data_file_path, 'w') as f:
            f.write(self.text_area.get('1.0', 'end-1c'))
        exit()


if __name__ == '__main__':
    app = PyNote()
    app.mainloop()
