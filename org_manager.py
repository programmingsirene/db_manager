#### ORGANIZATION/CLUB MANAGER - SQLITE AND PYTHON ####
### code framework based on tutorial from codemy ###
from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title('PSirene ~ Org Manager')
root.geometry("500x600")

#### DATABASE SETUP ####
# Create / Connect DB
conn = sqlite3.connect('org_mgr.db')

# Create cursor
c = conn.cursor()

# Create table
# only do it once so comment out for every run thereafter
#c.execute('CREATE TABLE org_mgr(first_name text, last_name text, address text, city text, state text, zipcode integer)')

#### FUNCTIONS ####
# Submit
def submit():
	conn = sqlite3.connect('org_mgr.db')
	c = conn.cursor()

	# insert to table
	c.execute("INSERT INTO org_mgr VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", {'f_name':f_name.get(), 'l_name':l_name.get(), 'address':address.get(), 'city':city.get(), 'state':state.get(), 'zipcode':zipcode.get()})

	conn.commit()
	conn.close()

	# clear text boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)

# Query
def query():
	conn = sqlite3.connect('org_mgr.db')
	c = conn.cursor()

	# query full database # oid is unique ID
	c.execute("SELECT *, oid FROM org_mgr")
	# fetchall, fetchone, fetchmany
	records = c.fetchall()
	# tkinter requires label for print
	# print(records) # print to console after app close for testing

	print_records = ''

	# loop through results
	for record in records:
		print_records += str(record[0]) + " " + str(record[1]) + "\t"  + str(record[4]) + "\t" + str(record[5]) + "\t" + str(record[6]) + "\n" 

	query_label = Label(root, text=print_records)
	query_label.grid(row=12, column=0, columnspan=2)

	conn.commit()
	conn.close()

# Delete
def delete():
	conn = sqlite3.connect('org_mgr.db')
	c = conn.cursor()


	# delete record
	c.execute("DELETE from org_mgr WHERE oid= " + delete_box.get())

	conn.commit()
	conn.close()

# Update
def update():
	conn = sqlite3.connect('org_mgr.db')
	c = conn.cursor()

	# update record - save edited text
	c.execute("UPDATE org_mgr SET first_name = :first, last_name = :last, address = :address, city = :city, state = :state, zipcode = :zipcode WHERE oid = :oid", {'first': f_name_editor.get(), 'last':l_name_editor.get(), 'address': address_editor.get(), 'city': city_editor.get(), 'state': state_editor.get(), 'zipcode': zipcode_editor.get(), 'oid':record_id})

	conn.commit()
	conn.close()

	editor.destroy()

# Edit
def edit():
	# create new window
	global editor
	editor = Tk()
	editor.title('Update Record')
	editor.geometry("500x600")

	conn = sqlite3.connect('org_mgr.db')
	c = conn.cursor()

	global record_id
	record_id = delete_box.get()

	# query database for info on given id
	c.execute("SELECT * FROM org_mgr WHERE oid = " + record_id)
	records = c.fetchall()

	# global vars
	global f_name_editor
	global l_name_editor
	global address_editor
	global city_editor
	global state_editor
	global zipcode_editor

	#### ENTRY BOXES ####
	# entry widgets - text boxes
	f_name_editor = Entry(editor, width=30)
	f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))

	l_name_editor = Entry(editor, width=30)
	l_name_editor.grid(row=1, column=1)

	address_editor = Entry(editor, width=30)
	address_editor.grid(row=2, column=1)

	city_editor = Entry(editor, width=30)
	city_editor.grid(row=3, column=1)

	state_editor = Entry(editor, width=30)
	state_editor.grid(row=4, column=1)

	zipcode_editor = Entry(editor, width=30)
	zipcode_editor.grid(row=5, column=1)

	#### LABELS ####
	# text box labels
	f_name_label_editor = Label(editor, text="First Name")
	f_name_label_editor.grid(row=0, column=0, padx=20, pady=(10,0))

	l_name_label_editor = Label(editor, text="Last Name")
	l_name_label_editor.grid(row=1, column=0)

	address_label_editor = Label(editor, text="Address")
	address_label_editor.grid(row=2, column=0)

	city_label_editor = Label(editor, text="City")
	city_label_editor.grid(row=3, column=0)

	state_label_editor = Label(editor, text="State")
	state_label_editor.grid(row=4, column=0)

	zipcode_label_editor = Label(editor, text="Zipcode")
	zipcode_label_editor.grid(row=5, column=0)

        # loop through results
	for record in records:
		f_name_editor.insert(0, record[0])
		l_name_editor.insert(0, record[1])
		address_editor.insert(0, record[2])
		city_editor.insert(0, record[3])
		state_editor.insert(0, record[4])
		zipcode_editor.insert(0, record[5])
			
	# update button
	edit_btn_editor = Button(editor, text="Save Record", command=update)
	edit_btn_editor.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

	conn.commit()
	conn.close()

#### ENTRY BOXES - ROOT ####
# entry widgets - text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=4, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

delete_box = Entry(root, width=25)
delete_box.grid(row=9, column=1, pady=5)

#### LABELS - ROOT ####
# text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10,0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=9, column=0, pady=5)


#### BUTTONS ####
## command calls functions ##
# submit button
submit_btn = Button(root, text="Add to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# update button
edit_btn = Button(root, text="Update Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=135)

# Commit changes to db
conn.commit()

# Close connection
conn.close()

root.mainloop()
