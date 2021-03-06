import tkinter as tk
from csvutil import CSV_Util
import functools

login_data = CSV_Util()

def submit():
    """
    When the user clicks submit button - gather field values, clear fields, set focus on first field
    """
    website = ent_website.get()
    username = ent_username.get()
    password = ent_password.get()
    print("Website: %s     Username: %s      Password: %s -- \nNew login_data: " % (website, username, password))
    login_data.add_new_password(website, username, password)
    for x in login_data.login_data:
        print(x)
    login_data.update_csv()
    display_data_rows(login_data.login_data)
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
    display_data_rows(login_data.login_data)
    ent_website.focus_set()

def delete(row):
    """
    When the user clicks the delete button - clear corresponding row and re-render passwords
    """
    print("Running DELETE ***********")
    print(login_data.login_data[row-4])
    del login_data.login_data[row-4]
    login_data.update_csv()
    print("NEW LOGINDATA *******")
    for x in login_data.login_data:
        print(x)
    display_data_rows(login_data.login_data)

def display_data_rows(data):
    """
    Display rows of password data
    data is a list of password data in dictionary format
    """
    # delete_data_table()
    data_table = tk.Frame(master=window)
    data_table.grid(row=4, column=0, columnspan=3)
    r = 4
    for row in data:
        print(row)

        # Website
        frame_list_a = tk.Frame(master=window)
        frame_list_a.grid(row=r, column=0)

        lbl_website_data = tk.Label(
            master=frame_list_a,
            text=row["website"]
        )
        lbl_website_data.grid()

        # Username
        frame_list_b = tk.Frame(master=window)
        frame_list_b.grid(row=r, column=1)

        lbl_username_data = tk.Label(
            master=frame_list_b,
            text=row["username"]
        )
        lbl_username_data.grid()

        # Password
        frame_list_password = tk.Frame(master=window)
        frame_list_password.grid(row=r, column=2)

        lbl_password_data = tk.Label(
            master=frame_list_password,
            text=row["password"]
        )
        lbl_password_data.grid()

        # Delete button
        frame_delete_button = tk.Frame(master=window)
        frame_delete_button.grid(row=r, column=3)

        btn_delete = tk.Button(
            master=frame_delete_button,
            text="Delete",
            relief=tk.RAISED,
            borderwidth=5,
            width=15,
            height=1,
            command=functools.partial(delete, r)
        )
        # btn_delete.pack(side=tk.LEFT)
        btn_delete.grid()
        r = r + 1


def delete_data_table():
    """
    Destroys data table so that the new table can be built successfully
    """




window = tk.Tk()
window.title("Logins")
window.columnconfigure([0, 1, 2], weight=1, minsize=175)

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

# ---------- Data Table Headers ---------------------------------------------------

frame_website_header = tk.Frame(master=window)
frame_website_header.grid(row=3, column=0, padx=5, pady=5)

lbl_website_header = tk.Label(
    master=frame_website_header,
    text="Website",
)
lbl_website_header.pack(padx=5, pady=5)

frame_username_header = tk.Frame(master=window)
frame_username_header.grid(row=3, column=1, padx=5, pady=5)

lbl_username_header = tk.Label(
    master=frame_username_header,
    text="Username",
)
lbl_username_header.pack(padx=5, pady=5)

frame_password_header = tk.Frame(master=window)
frame_password_header.grid(row=3, column=2, padx=5, pady=5)

lbl_password_header = tk.Label(
    master=frame_password_header,
    text="Password",
)
lbl_password_header.pack(padx=5, pady=5)
#
# data_table = tk.Frame(master=window)
# data_table.grid(row=4, column=0, columnspan=4)

display_data_rows(login_data.login_data)
window.mainloop()
