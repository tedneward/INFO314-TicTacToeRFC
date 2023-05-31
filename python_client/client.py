from tkinter import *


# Create the main window
window = Tk(screenName="Tic-Tac-Toe Client")
window.title("Tic-Tac-Toe Client")

# Create a label
window_title_label = Label(window, text="Tic-Tac-Toe Client")

# Place the label where there is space
window_title_label.pack()

# Display the window
window.mainloop()
