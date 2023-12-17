from tkinter import *
#from tkinter import *: This line imports the entire tkinter library, which is a standard Python library used for creating graphical user interfaces. The * symbol means that you are importing all classes and functions from the tkinter library.
from tkinter import ttk, messagebox
#ttk stands for "themed tkinter" and is a sub-module within the tkinter library. It provides a set of themed widgets that have a modern and platform-native appearance, which can make your GUI applications look more appealing and consistent on different platforms (Windows, macOS, Linux).



root = Tk()
#is used to create the main application window for a graphical user interface (GUI) using the tkinter library in Python.
root.title("Google Translator")
#make the title for the application
root.geometry("1080x400")
#is used to set the initial size of the main application window in a GUI created with the tkinter library in Python

def label_change():
    c = combo1.get()
    c1 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000, label_change)

def translate_now():
    try:
        text = text1.get(1.0, 'end-1c')
        translator = Translator()
        source_lang = combo1.get()
        target_lang = combo2.get()
        translated_text = translator.translate(text, src=source_lang, dest=target_lang)
        text2.delete(1.0, END)
        text2.insert(1.0, translated_text.text)
    except Exception as e:
        messagebox.showerror("Error", "An error occurred during translation. Please check your input.")

# Language codes and names
language = googletrans.LANGUAGES
languageV = ['English', 'Spanish', 'French', 'German', 'Persian', 'Italian', 'Portuguese','pashto']
languageK = list(language.keys())

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("English")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

Scrollbar1 = Scrollbar(f)
Scrollbar1.pack(side="right", fill="y")
Scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=Scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("Select Language")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

Scrollbar2 = Scrollbar(f1)
Scrollbar2.pack(side="right", fill="y")

Scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=Scrollbar2.set)

# Translator button
translate = Button(root, text="Translate", font="Roboto 15 bold italic",
                  activebackground="purple", cursor="hand2", bd=5,
                  bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.configure(bg="white")
root.mainloop()
