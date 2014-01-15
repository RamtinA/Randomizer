#!user/bin/env Python

from gi.repository import Gtk

class AppWindow(Gtk.Window):
	def __init__(self):
		#Window
		Gtk.Window.__init__(self,title = "Randomizer")
		self.set_border_width(10)
		self.set_position(Gtk.WindowPosition.CENTER)
		
		#V Boxes
		VBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(VBox)

		AddNameVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=6)
		RandomNameVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=18)

		#H Boxes
		AddNameHBox = Gtk.Box (spacing = 10)

		#Stack
		Stack = Gtk.Stack()
		Stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
		Stack.set_transition_duration(500)


		#Stack Switcher
		StackSwitcher = Gtk.StackSwitcher()
		StackSwitcher.set_stack(Stack)

		#Lables
		NameLabel = Gtk.Label("Name :")
		RandomLabel = Gtk.Label("Ready?")

		#Entry
		NameEntry = Gtk.Entry()

		#Buttons
		AddNameButton = Gtk.Button("Add Name")
		RandomButton = Gtk.Button("Select By Random")

		#Add H Boxes
		AddNameHBox.pack_start(NameLabel,True,True,0)
		AddNameHBox.pack_start(NameEntry,True,True,0)

		#Add Stacks
		Stack.add_titled(AddNameVBox,"Add","Add Name")
		Stack.add_titled(RandomNameVBox,"Random","Random Name")


		#Add V Boxes
		VBox.pack_start(StackSwitcher,True,True,0)
		VBox.pack_start(Stack,True,True,0)
		
		AddNameVBox.pack_start(AddNameHBox,True,True,0)
		AddNameVBox.pack_start(AddNameButton,True,True,0)

		RandomNameVBox.pack_start(RandomLabel,True,True,0)
		RandomNameVBox.pack_start(RandomButton,True,True,0)

		

		
		

win = AppWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
