import tkinter as tk



def submit():
    """
    When the user clicks submit button - gather field values, clear fields, set focus on first field
    """
    website = ent_website.get()
    username = ent_username.get()
    password = ent_password.get()
    print("Website: %s     Username: %s      Password: %s" % (website, username, password))
    clear()
    ent_website.focus_set()


def clear():
    """
    When the user clicks the clear button - clear field values and set focus on first field
    """
    ent_website.delete(0, tk.END)
    ent_username.delete(0, tk.END)
    ent_password.delete(0, tk.END)
    print("Fields are cleared")
    ent_website.focus_set()


window = tk.Tk()
window.title("Logins")
window.columnconfigure([0,1,2], weight=1, minsize=175)

frame_title = tk.Frame(master=window)
frame_title.grid(row=0, column=0, columnspan=3)

lbl_title = tk.Label(
    master=frame_title,
    text="Logins",
    fg="black",
    height=3
)
lbl_title.pack()

frame_website = tk.Frame(master=window)
frame_website.grid(row=1, column=0, padx=5, pady=5)

lbl_website = tk.Label(
    master=frame_website,
    text="Website:",
    fg="black"
)
lbl_website.pack(padx=5, pady=5)

ent_website = tk.Entry(
    master=frame_website,
    width=25,
    bg="white",
    fg="black"
)
ent_website.pack()

frame_username = tk.Frame(master=window)
frame_username.grid(row=1, column=1, padx=5, pady=5)

lbl_username = tk.Label(
    master=frame_username,
    text="Username:",
    fg="black"
)
lbl_username.pack(padx=5, pady=5)

ent_username = tk.Entry(
    master=frame_username,
    width=25,
    bg="white",
    fg="black"
)
ent_username.pack()

frame_password = tk.Frame(master=window)
frame_password.grid(row=1, column=2, padx=5, pady=5)

lbl_password = tk.Label(
    master=frame_password,
    text="Password:",
    fg="black"
)
lbl_password.pack(padx=5, pady=5)

ent_password = tk.Entry(
    master=frame_password,
    width=25,
    bg="white",
    fg="black"
)
ent_password.pack()

frame_buttons = tk.Frame(master=window, width=200)
frame_buttons.grid(row=2, column=1, padx=5, pady=5)

btn_submit = tk.Button(
    master=frame_buttons,
    text="Submit",
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=2,
    command=submit
)
btn_submit.pack(side=tk.TOP)

btn_clear = tk.Button(
    master=frame_buttons,
    text="Clear",
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=2,
    command=clear
)
btn_clear.pack(side=tk.BOTTOM)

# email = ent_email.get()

#clear button - entry.delete(0, tk.END)

window.mainloop()
