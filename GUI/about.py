"""Address Book About page

Window to displays developer and application information.
"""
import tkinter as Tk

class About_Window(object):

	def __init__(self, master):
		top=self.top=Tk.Toplevel(master)
		self.master = master
		top.title("Information")

		# Team Cowsay logo
		self.photo = Tk.PhotoImage(master=top, file="GUI/dypatilimg.gif")
		self.photo_label = Tk.Label(top, image=self.photo)
		self.photo_label.grid(row=0, column=0)

		# Application information
		self.label = Tk.Label(top, text="\nAddress Book in Python \n By Group ID - 6 ", font=('Helvetica', 15, 'bold'))
		self.label.grid(row=2, column=0, padx=10, pady=30)


