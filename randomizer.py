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

		DeleteNameVBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing=10)
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
		self.NameLabel = Gtk.Label("Name :")
		self.RandomLabel = Gtk.Label("Ready?")

		#Entry
		self.NameEntry = Gtk.Entry()

		#Buttons
		self.AddNameButton = Gtk.Button("Add Name")
		self.RandomButton = Gtk.Button("Select By Random")
		self.DeleteButton = Gtk.Button("Delete Name")

		#Combobox
		self.Names =["test","testsdtsdf","dsfsdf"]
		NameStore = Gtk.ListStore(str)
		self.Names.append("asdasd")

		self.NameCombo = Gtk.ComboBox.new_with_model(NameStore)
		self.NameCombo.set_entry_text_column(1)

		for Name in self.Names:
			NameStore.append([Name])

		RendererText = Gtk.CellRendererText()
		self.NameCombo.pack_start(RendererText,True)
		self.NameCombo.add_attribute(RendererText,"text",0)


		#Add H Boxes
		AddNameHBox.pack_start(self.NameLabel,True,True,0)
		AddNameHBox.pack_start(self.NameEntry,True,True,0)

		#Add Stacks
		Stack.add_titled(AddNameVBox,"Add","Add Name")
		Stack.add_titled(RandomNameVBox,"Random","Random Name")
		Stack.add_titled(DeleteNameVBox,"Delete","Delete Name")


		#Add V Boxes
		VBox.pack_start(StackSwitcher,True,True,0)
		VBox.pack_start(Stack,True,True,0)
		
		AddNameVBox.pack_start(AddNameHBox,True,True,0)
		AddNameVBox.pack_start(self.AddNameButton,True,True,0)

		RandomNameVBox.pack_start(self.RandomLabel,True,True,0)
		RandomNameVBox.pack_start(self.RandomButton,True,True,0)

		DeleteNameVBox.pack_start(self.NameCombo,True,True,0)
		DeleteNameVBox.pack_start(self.DeleteButton,True,True,0)
		

		
		

win = AppWindow()
win.connect("delete-event",Gtk.main_quit)
win.show_all()
Gtk.main()
