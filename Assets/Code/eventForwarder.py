class EventForwarder(QObject):
    def __init__(self, widget, receiver):
        super().__init__(widget)
        self.receiver = receiver

        # Install event filter to intercept events
        widget.installEventFilter(self)

    def eventFilter(self, object, event):
        # Forward event to receiver
        self.receiver.event(event)
        return False  # pass event on to other event filters

# Set up event forwarder
forwarder = EventForwarder(widget, receiver)

-----------------------------------------------------------------------------------

class EventReceiver:
    def event(self, event):
        if event.type() == QtCore.QEvent.MouseMove:
            print("Mouse move event received")
        elif event.type() == QtCore.QEvent.KeyPress:
            print("Key press event received")

# Set up event receiver
receiver = EventReceiver()
