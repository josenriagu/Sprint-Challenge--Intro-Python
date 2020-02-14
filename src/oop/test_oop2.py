import unittest
from oop2 import GroundVehicle, Motorcycle


class Oop2Tests(unittest.TestCase):
    def setUp(self):
        self.ground_vehicle = GroundVehicle()
        self.motorcycle = Motorcycle()

    def test_motorcycle_inheritance(self):
        self.assertTrue(isinstance(self.motorcycle, GroundVehicle))

    def test_ground_vehicle_num_wheels(self):
        self.assertEqual(self.ground_vehicle.num_wheels, 4)

    def test_motocycle_num_wheels(self):
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_ground_vehicle_drive(self):
        self.assertEqual(self.ground_vehicle.drive(), "vroooom")
        self.assertEqual(self.ground_vehicle.drive_faster(), "vroom vrooooom vroooooooom!!")
        

    def test_motorcyle_drive(self):
        self.assertEqual(self.motorcycle.drive(), "BRAAAP!!")
        self.assertEqual(self.motorcycle.drive_faster(), "BRAAAAAP!! TATAAATTAATTTAA!!")


if __name__ == '__main__':
    unittest.main()
