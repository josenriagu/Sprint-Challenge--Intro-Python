# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # base class
    def __init__(self):
        pass

class FlightVehicle(Vehicle):
    # sub class 1
    def __init__(self):
        super().__init__()
        pass

class Starship(FlightVehicle):
    # sub sub class 1_1
    def __init__(self):
        super().__init__()
        pass

class Airplane(FlightVehicle):
    # sub sub class 1_2
    def __init__(self):
        super().__init__()
        pass

class GroundVehicle(Vehicle):
    # sub class 2
    def __init__(self):
        super().__init__()
        pass

class Car(GroundVehicle):
    # sub sub class 2_1
    def __init__(self):
        super().__init__()
        pass

class Motorcycle(GroundVehicle):
    # sub sub class 2_2
    def __init__(self):
        super().__init__()
        pass