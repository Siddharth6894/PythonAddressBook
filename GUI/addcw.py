"""Add Confirmation Window

Confirmation window that pops up when user fails to enter enough contact info.
"""
import tkinter as Tk

class ConfirmationWindow(object):
	
	def ok(self):
		self.top.destroy()
	

	def __init__(self, master):
		top = self.top = Tk.Toplevel(master)
		self.master = master
		top.title('Oops!')

		self.label = Tk.Label(top, text = 'A first name is required.',font=('Helvetica',9,'bold'))
		self.label.grid(row = 0, column = 0, padx = 20, pady = 20)

		self.yes_button = Tk.Button(top, text = 'Ok', command = self.ok,font=('Helvetica',9,'bold'))
		self.yes_button.grid(row = 1,padx = 20, pady = 20)