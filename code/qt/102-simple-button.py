"""
Signal and slots:

Signals and Slots is a Qt Feature that lets your graphical widgets communicate
with other graphcical widgets for your Python code.


Application creates a button that logs the "Button clicked, Hello!" message to the console each time you click it.
"""

import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot


@Slot()
def say_hello():
    print("Button clicked, Hello!")
    
# Create the Qt Application
app = QApplication([])
# Create a button, connect it and show it
button = QPushButton("Click me")
button.clicked.connect(say_hello)
button.show()
# Run the main Qt loop
app.exec()