from tkinter import *
root = Tk()
root.title("Encryption Software")
root.minsize(400,200)
root.maxsize(800,400)
root.configure(bg = "red1")

name = Entry(root)
ascii_form = Label(root, font = ("Comic Sans MS", 12, "bold"))
encrypted_form = Label(root, font = ("Comic Sans MS", 12, "bold"))


def encrypt() :
    value = name.get()
    ascii_value = ""
    encrypted_code = ""
    for x in value:
        if(value.index(x) == len(value)-1):
            ascii_value += str((ord(x)))
            encryption = ord(x) - 1
            encrypted_code += str(chr(encryption))
            
        else:
            ascii_value += str((ord(x))) + ", "
            encryption = ord(x) - 1
            encrypted_code += str(chr(encryption))
    
        
    ascii_form["text"] = ascii_value
    encrypted_form["text"] = encrypted_code
        

encrypt_button = Button(root, font = ("Comic Sans MS", 12, "bold"), command = encrypt, bg = "red1", text = "Encrypt", fg  ="black")

ascii_form.place(relx = 0.5, rely = 0.6, anchor = CENTER)
encrypted_form.place(relx = 0.5, rely = 0.8, anchor = CENTER)
encrypt_button.place(relx = 0.5, rely = 0.4, anchor = CENTER)
name.place(relx = 0.5, rely = 0.2, anchor = CENTER)



root.mainloop()