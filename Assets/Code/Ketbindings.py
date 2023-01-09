from PyQt5.QtCore import QTimer, Qt


def runActionOnHover(widget, action):
    """
    Run an action when the cursor hovers over a widget for 1 second.
    """

    def startTimer():
        timer.start(1000)  # run action after 1 second (1000 milliseconds)

    def stopTimer():
        timer.stop()

    timer = QTimer(widget)
    timer.setSingleShot(True)  # only run action once
    timer.timeout.connect(action)  # run action when timer times out

    widget.enterEvent = startTimer  # start timer when cursor enters widget
    widget.leaveEvent = stopTimer  # stop timer when cursor leaves widget


# Example usage:
def greet():
    print("Hello!")


runActionOnHover(widget, greet)

---------------------------------------------------------------------------------

class KeyBindingFilter(QObject):
    def __init__(self, keyBindingManager):
        self.keyBindingManager = keyBindingManager

    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.KeyPress:
            self.keyBindingManager.executeBinding(QKeySequence(event.key()))
            return True  # consume event
        return False  # pass event on to other event filters

# Set up key binding manager
keyBindingManager = KeyBindingManager()
keyBindingManager.addBinding(QKeySequence("Ctrl+G"), greet)

# Set up event filter to detect key press events
keyBindingFilter = KeyBindingFilter(keyBindingManager)
window.installEventFilter(keyBindingFilter)
