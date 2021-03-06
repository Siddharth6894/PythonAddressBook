"""New Address Book Window

Requests users for the name of their address book.
"""
import sys
import tkinter as Tk
from logging import root

import db
import gui
import newcw

class New_AddBookWindow(object):

	def ok(self):
		"""Open the user specified address book."""
		book_name = self.book_name.get()

		if len(book_name) > 1:
			db.db_init(book_name)
			root = Tk.Tk()
			self.master.withdraw()
			root.protocol("WM_DELETE_WINDOW", exit)
			gui.mainWindow(root)
			root.mainloop()
			sys.exit()

		else: 
			self.c=newcw.ConfirmationWindow(self.master)


	def exit(self):
		root.destroy()


	def close_window(self):
		self.master.destroy()


	def __init__(self, master):
		self.new = master
		self.master = master
		self.master.title('New Address Book')

		self.instruction_message = Tk.Label(self.master, text = 'Please Enter the Name of your Address Book or Enter new one',font=('Helvetica',12,'bold'))
		self.instruction_message.grid(columnspan = 2, pady = 30,padx=30)

		self.book_name_label = Tk.Label(self.master, text = 'Address Book Name :-',font=('Helvetica',13,'bold'))
		self.book_name_label.grid(row = 1, padx = 10,ipadx =15 )

		# Entry is for user's desired Address Book Name
		self.book_name = Tk.Entry(self.master,font=('Helvetica',13,'bold'))
		self.book_name.grid(row = 1 , column = 1, padx = 10,pady=18)

		self.ok_button = Tk.Button(self.master, text='Ok', command=self.ok,font=('Helvetica',10,'bold'))
		self.ok_button.grid(row=2, column=1,ipadx =5, padx = 10)

		self.cancel_button = Tk.Button(self.master, text = 'Cancel', command = self.close_window,font=('Helvetica',10,'bold') )
		self.cancel_button.grid(row = 2, column = 1, sticky = Tk.E, padx = 10, pady = 10 )