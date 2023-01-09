from PyQt5.QtGui import QKeySequence


class KeyBindingManager:
    def __init__(self):
        self.bindings = {}  # map key sequences to actions

    def addBinding(self, keySequence: QKeySequence, action):
        """
        Add a key binding to the manager.
        """
        self.bindings[keySequence] = action

    def removeBinding(self, keySequence: QKeySequence):
        """
        Remove a key binding from the manager.
        """
        if keySequence in self.bindings:
            del self.bindings[keySequence]

    def executeBinding(self, keySequence: QKeySequence):
        """
        Execute the action associated with the given key sequence.
        """
        if keySequence in self.bindings:
            self.bindings[keySequence]()


# Example usage:
def greet():
    print("Hello!")


manager = KeyBindingManager()
manager.addBinding(QKeySequence("Ctrl+G"), greet)

# Execute the action when the key binding is detected
manager.executeBinding(QKeySequence("Ctrl+G"))  # prints "Hello!"
