import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as message_box
import database


def selected_row(event):
    global selected_row_data
    global index
    index = database_list.curselection()[0]
    selected_row_data = database_list.get(index)
    # print(selected_row_data)
    # print(selected_row_data[0])
    name_entry.delete(0, tk.END)
    name_entry.insert(tk.END, selected_row_data[1])
    blood_entry.delete(0, tk.END)
    blood_entry.insert(tk.END, selected_row_data[2])
    city_entry.delete(0, tk.END)
    city_entry.insert(tk.END, selected_row_data[3])
    contact_entry.delete(0, tk.END)
    contact_entry.insert(tk.END, selected_row_data[4])


def view_all_data():
    database_list.delete(0, tk.END)
    for row in database.show():
        database_list.insert(tk.END, row)


def search_specific_data():
    database_list.delete(0, tk.END)
    for row in database.search(name.get(), blood_group.get(), city.get(), contact.get()):
        database_list.insert(tk.END, row)


def insert_new_data():
    database.insert_table(name1.get(), blood_group1.get(), city1.get(), contact1.get())
    database_list.delete(0, tk.END)
    database_list.insert(tk.END, (name1.get(), blood_group1.get(), city1.get(), contact1.get()))


def delete_any_entry():
    database.delete(selected_row_data[0])
    database_list.delete(0, tk.END)
    for row in database.show():
        database_list.insert(tk.END, row)


def update_any_entry():
    # print("X", selected_row_data[0], name.get(), blood_group.get(), city.get(), contact.get())
    database.update_table(selected_row_data[0], name.get(), blood_group.get(), city.get(), contact.get())
    database_list.delete(0, tk.END)
    for row in database.show():
        database_list.insert(tk.END, row)


# Main Window
window = tk.Tk()
window.title("Blood Donor Management System")


# Exit GUI cleanly
def _quit():
    window.quit()
    window.destroy()
    exit()


# Display a Message Box for halp menu
def _msgBox():
    message_box.showinfo('Blood Donor Management System', 'Blood Donor Management System GUI created in 2018 by \nMd. Sharwat Kabir & Biplab C. Debnath.')


# Menu Bar -------------------------------------------------------------
menuBar = Menu(window)
window.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=_msgBox)
menuBar.add_cascade(label="Help", menu=helpMenu)

# Tab Control ----------------------------------------------------------
tabControl = ttk.Notebook(window)

view = ttk.Frame(tabControl)
tabControl.add(view, text='View')

add = ttk.Frame(tabControl)
tabControl.add(add, text='Add')

tabControl.pack(expand=1, fill="both")

# ~ Under View Tab ------------------------------------------------------
# Input Label
frame = ttk.LabelFrame(view, text=' Result Window')
frame.grid(column=0, row=3, padx=8, pady=4, columnspan=4, rowspan=4, sticky='W')

name_label = ttk.Label(view, width=15, text="Name")
name_label.grid(row=0, column=0, sticky='W')

blood_label = ttk.Label(view, width=15, text="Blood Group")
blood_label.grid(row=0, column=1, sticky='W')

city_label = ttk.Label(view, width=15, text="City")
city_label.grid(row=0, column=2, sticky='W')

contact_label = ttk.Label(view, width=15, text="Contact")
contact_label.grid(row=0, column=3, sticky='W')

# Input Field
name = tk.StringVar()
name_entry = ttk.Entry(view, textvariable=name)
name_entry.grid(row=1, column=0, sticky='W')

blood_group = tk.StringVar()
blood_entry = ttk.Entry(view, textvariable=blood_group)
blood_entry.grid(row=1, column=1, sticky='W')

city = tk.StringVar()
city_entry = ttk.Entry(view, textvariable=city)
city_entry.grid(row=1, column=2, sticky='W')

contact = tk.StringVar()
contact_entry = ttk.Entry(view, textvariable=contact)
contact_entry.grid(row=1, column=3, sticky='W')

# Buttons
search_button = ttk.Button(view, width=15, text="Search Donor", command=search_specific_data)
search_button.grid(row=3, column=3, sticky='W')

view_button = ttk.Button(view, width=15, text="View Database", command=view_all_data)
view_button.grid(row=4, column=3, sticky='W')

update_button = ttk.Button(view, width=15, text="Update Donor", command=update_any_entry)
update_button.grid(row=5, column=3, sticky='W')

delete_button = ttk.Button(view, width=15, text="Delete Donor", command=delete_any_entry)
delete_button.grid(row=6, column=3, sticky='W')

# Output window
scrollbar = ttk.Scrollbar(frame, orient="vertical")
database_list = tk.Listbox(frame, width=55, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=database_list.yview)

scrollbar.grid(row=3, column=3, sticky='W', columnspan=3)
database_list.grid(row=3, sticky='W')

database_list.bind('<<ListboxSelect>>', selected_row)

# ~ Under Add Tab ------------------------------------------------------
# Input Label
name_label = ttk.Label(add, width=15, text="Name")
name_label.grid(row=0, column=0, sticky='W')

blood_label = ttk.Label(add, width=15, text="Blood Group")
blood_label.grid(row=0, column=1, sticky='W')

city_label = ttk.Label(add, width=15, text="City")
city_label.grid(row=0, column=2, sticky='W')

contact_label = ttk.Label(add, width=15, text="Contact")
contact_label.grid(row=0, column=3, sticky='W')

# Input Field
name1 = tk.StringVar()
name1_entry = ttk.Entry(add, textvariable=name1)
name1_entry.grid(row=1, column=0, sticky='W')

blood_group1 = tk.StringVar()
blood_entry1 = ttk.Entry(add, textvariable=blood_group1)
blood_entry1.grid(row=1, column=1, sticky='W')

city1 = tk.StringVar()
city_entry1 = ttk.Entry(add, textvariable=city1)
city_entry1.grid(row=1, column=2, sticky='W')

contact1 = tk.StringVar()
contact_entry1 = ttk.Entry(add, textvariable=contact1)
contact_entry1.grid(row=1, column=3, sticky='W')

add_button = ttk.Button(add, width=15, text="Add Donor", command=insert_new_data)
add_button.grid(row=2, column=0, sticky='W')


window.mainloop()
