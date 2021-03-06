"""New Confirmation Window

Window that pops up when user chooses to edit a contact.
"""
import tkinter as Tk

class ConfirmationWindow(object):
	
	def ok(self):
		self.top.destroy()
	

	def __init__(self, master):
		top = self.top = Tk.Toplevel(master)
		self.master = master
		top.title('Oops!')

		self.label = Tk.Label(top, text = 'An address book name is required.',font=('Helvetica',9,'bold'))
		self.label.grid(row = 0, column = 0, padx = 10, pady = 10)

		self.yes_button = Tk.Button(top, text = 'Ok', command = self.ok ,font=('Helvetica',9,'bold'))
		self.yes_button.grid(row = 1)