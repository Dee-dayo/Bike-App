import unittest
import bikeApp


class MyTestCase(unittest.TestCase):
    def test_bike_turns_on(self):
        my_bike = bikeApp.Bike()
        self.assertFalse(my_bike.check_status())

        my_bike.start()
        self.assertTrue(my_bike.check_status())
