
def createButton(self, Button, text, command, highlightbackground, compound, x, y):
  self.nav_button = Button(self, text =text, command=command, highlightbackground=highlightbackground, compound=compound)
  self.nav_button.place(x = x, y = y)

def createLabel(self, Label, wraplength, text, backgroundColor, foreground, justify, x, y):
  self.label = Label(self, wraplength=wraplength, textvariable=text, background=backgroundColor, foreground=foreground, justify=justify)
  self.label.pack()
  self.label.place(x = x, y = y)