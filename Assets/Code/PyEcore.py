from pyecore.ecore import *

# Define the model
class MyModel(EClass):
    name = EAttribute(eType=EString)

# Create an instance of the model
model = MyModel(name='test')
model.name = "My Model"

# Print the model's name
print(model.name)
