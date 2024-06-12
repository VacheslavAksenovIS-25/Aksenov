# В соотвествии с вариантом перейти по ссылке на прототип.Реализовать его с применеием паркета tk

from tkinter import *

root = Tk()
root.title("Register")
root.geometry("500x600")
root.configure(bg="gray")

title_label = Label(root, text="Elegant login and Register forms", background="gray", fg="black", font=("Times New Roman", 16, 'italic'))
title_label.pack(pady=(20, 20))

main_frame = Frame(root, bg="black", pady=50)
main_frame.place(relx=0.5, rely=0.5, anchor="center")

# Надпись "Register"
label_main = Label(main_frame, text="Register", background="black",font='Arial 20', bd=2, pady=25, fg='gray').grid(row=0, column=0, columnspan=2)
# Поля ввода
entry_name = Entry(main_frame, bg="black", fg="gray")
entry_name.insert(0, "First Name")
entry_name.grid(row=1, column=0, columnspan=2, pady=5, padx=20, sticky="ew")

entry_surname = Entry(main_frame, bg="black", fg="gray")
entry_surname.insert(0, "Last Name")
entry_surname.grid(row=2, column=0, columnspan=2, pady=5,padx=20, sticky="ew")

entry_email = Entry(main_frame, bg="black", fg="gray")
entry_email.insert(0, "Email Address")
entry_email.grid(row=3, column=0, columnspan=2, pady=5,padx=20, sticky="ew")

entry_username = Entry(main_frame, bg="black", fg="gray")
entry_username.insert(0, "User Name")
entry_username.grid(row=4, column=0, columnspan=2, pady=5,padx=20, sticky="ew")

entry_password = Entry(main_frame, bg="black", fg="gray", show='•')
entry_password.insert(0, "Password")
entry_password.grid(row=5, column=0, columnspan=2, pady=5,padx=20, sticky="ew")

entry_repeat_password = Entry(main_frame, bg="black", fg="gray", show='•')
entry_repeat_password.insert(0, "Password")
entry_repeat_password.grid(row=6, column=0, columnspan=2, pady=5,padx=20, sticky="ew")


checkbutton = Checkbutton(main_frame,text="I agree to the Terms and Conditions",bg="black",fg="grey",)
checkbutton.grid(row=7, column=0, columnspan=2, padx=20)

button = Button(main_frame, text="Sign Me Up>", bg="lightgreen", fg="black")
button.grid(row=8, column=0, columnspan=2)

root.mainloop()
