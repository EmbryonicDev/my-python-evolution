
while True:
    editor = input("Editor: ")
    editor = editor.lower()

    if editor == "visual studio code":
        break

    if editor == "emacs" or editor == "vim" or editor == "atom":
        print("not good")
    elif editor == "word" or editor == "notepad":
        print("awful")

print("an excellent choice!")
