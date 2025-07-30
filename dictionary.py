from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PyDictionary import PyDictionary
from googletrans import Translator

def get_meaning():
    word = txt_input.get()
    format = laguage_format.get()
    if not word:
        messagebox.showerror("Error", "Please enter a word")
        return
    dictionary = PyDictionary()

    if format == 'English to English':
        meaning = dictionary.meaning(word)
        if meaning:
            outputbox.delete(1.0, END)
            for key, value in meaning.items():
                outputbox.insert(END, f"{key}: {', '.join(value)}\n")
        else:
            outputbox.delete(1.0, END)
            outputbox.insert(END, "No meaning found.")
    
    elif format == 'English to Hindi':
        translator = Translator()
        translation = translator.translate(word, src='en', dest='hi')
        outputbox.delete(1.0, END)
        outputbox.insert(END, translation.text)


# driver code
if __name__ == "__main__":
    # create root window
    root = Tk()
    # change the title
    root.title("Dictionary")
    # change the window size
    root.geometry("300x400")
    # no resizable for both directions
    root.resizable(False, False)

    # set gui widgets
    lbl_format = Label(root, text="select format:",font=("times new roman", 12,))
    lbl_word = Label(root, text="Enter word:", font=("times new roman", 12,))
    txt_input = Entry(root, width=20, bd="2", font="18", relief=RIDGE)
    btn_get_meaning = Button(root, text='search', width=6, command=get_meaning, font=("times new roman", 14), relief=RAISED)
    lbl_means = Label(root, text="meaning :", font=("verdana",14, 'bold' ))
    outputbox = Text(root, width=29, height=11, relief=RIDGE, bd=2, pady=5, padx=3,  spacing2=3, font=("times new roman", 13))

    # place geometry
    lbl_format.place(x=10, y=13)
    lbl_word.place(x=10, y=60)
    txt_input.place(x=100, y=60)
    btn_get_meaning.place(x=213, y=100)
    lbl_means.place(x=10, y=130)
    outputbox.place(x=13, y=165)


    # combobox creation
    n = StringVar()
    laguage_format = ttk.Combobox(root, width=25, textvariable=n,)

     # adding combobox drop down list
    laguage_format['values'] = ('English to English', 'English to Hindi')
    laguage_format.place(x=115, y=15)
    laguage_format.current(0)


    # start mainloop
    root.mainloop()  