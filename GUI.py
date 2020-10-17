import tkinter as tk

window = tk.Tk()
window.columnconfigure([0,1,2], weight=1, minsize=30)
# window.rowconfigure([0, 3], minsize=30)

frame_title = tk.Frame(master=window)
frame_title.grid(row=0, column=1)

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

btn_ok = tk.Button(
    master=frame_buttons,
    text="Submit",
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=2,
)
btn_ok.pack(side=tk.TOP)

btn_clear = tk.Button(
    master=frame_buttons,
    text="Clear",
    relief=tk.RAISED,
    borderwidth=5,
    width=20,
    height=2,
)
btn_clear.pack(side=tk.BOTTOM)

# email = ent_email.get()

#clear button - entry.delete(0, tk.END)

window.mainloop()
