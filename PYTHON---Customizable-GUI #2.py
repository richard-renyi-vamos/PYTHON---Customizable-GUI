import tkinter as tk
from tkinter import simpledialog
import webbrowser
import subprocess

class CustomButton:
    def __init__(self, master, text, command=None, url=None, app_path=None):
        self.button = tk.Button(master, text=text, command=self.execute_command)
        self.command = command
        self.url = url
        self.app_path = app_path

    def execute_command(self):
        if self.command == 'open_website':
            webbrowser.open(self.url)
        elif self.command == 'open_app':
            subprocess.run([self.app_path])
        else:
            print(f"No valid command configured for button '{self.button.cget('text')}'.")

class GUIApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Customizable GUI")

        self.buttons = []

        add_button = tk.Button(master, text="Add Button", command=self.add_button)
        add_button.pack(pady=10)

    def add_button(self):
        button_text = simpledialog.askstring("Input", "Enter button text:")
        if button_text:
            command_choice = simpledialog.askstring("Input", "Enter command ('open_website' or 'open_app'):")
            if command_choice == 'open_website':
                url = simpledialog.askstring("Input", "Enter website URL:")
                new_button = CustomButton(self.master, button_text, command=command_choice, url=url)
            elif command_choice == 'open_app':
                app_path = simpledialog.askstring("Input", "Enter app path:")
                new_button = CustomButton(self.master, button_text, command=command_choice, app_path=app_path)
            else:
                new_button = CustomButton(self.master, button_text)

            new_button.button.pack(pady=5)
            self.buttons.append(new_button)

def main():
    root = tk.Tk()
    app = GUIApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
