import unittest
import bikeApp


class MyTestCase(unittest.TestCase):

    def test_bike_turns_on(self):
        my_bike = bikeApp.Bike()
        self.assertFalse(my_bike.check_status())

        my_bike.start()
        self.assertTrue(my_bike.check_status())

    def test_turn_bike_off_bike_turn_off(self):
        my_bike = bikeApp.Bike()
        self.assertFalse(my_bike.check_status())
        my_bike.start()
        self.assertTrue(my_bike.check_status())

        my_bike.stop()
        self.assertFalse(my_bike.check_status())

    def test_accelerate_bike(self):
        my_bike = bikeApp.Bike()
        self.assertFalse(my_bike.check_status())
        my_bike.start()
        self.assertTrue(my_bike.check_status())

        my_bike.accelerate()
        self.assertEqual(1, my_bike.check_speedometer())

        my_bike.accelerate()
        my_bike.accelerate()
        self.assertEqual(3, my_bike.check_speedometer())

    def test_accelerate_when_bike_off(self):
        my_bike = bikeApp.Bike()
        self.assertFalse(my_bike.check_status())

        my_bike.accelerate()
        self.assertEqual(0, my_bike.check_speedometer())