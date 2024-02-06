import unittest
from bikeApp import Bike


class MyTestCase(unittest.TestCase):

    def test_bike_turns_on(self):
        my_bike = Bike()
        self.assertFalse(my_bike.check_status())

        my_bike.start()
        self.assertTrue(my_bike.check_status())

    def test_turn_bike_off_bike_turn_off(self):
        my_bike = Bike()
        self.assertFalse(my_bike.check_status())
        my_bike.start()
        self.assertTrue(my_bike.check_status())

        my_bike.stop()
        self.assertFalse(my_bike.check_status())

    def test_accelerate_bike(self):
        my_bike = Bike()
        self.assertFalse(my_bike.check_status())
        my_bike.start()
        self.assertTrue(my_bike.check_status())

        my_bike.accelerate()
        self.assertEqual(1, my_bike.check_speedometer())

        my_bike.accelerate()
        my_bike.accelerate()
        self.assertEqual(3, my_bike.check_speedometer())

    def test_accelerate_when_bike_off(self):
        my_bike = Bike()
        self.assertFalse(my_bike.check_status())

        my_bike.accelerate()
        self.assertEqual(0, my_bike.check_speedometer())

    def test_accelerate_more_than_20_gear_becomes_two(self):
        my_bike = Bike()
        my_bike.start()
        for count in range(20):
            my_bike.accelerate()
        self.assertEqual(20, my_bike.check_speedometer())
        self.assertEqual(1, my_bike.check_gear())

        my_bike.accelerate()
        my_bike.accelerate()
        self.assertEqual(23, my_bike.check_speedometer())
        self.assertEqual(2, my_bike.check_gear())

    def test_gear_at_2_accelerate_goes_twice(self):
        my_bike = Bike()
        my_bike.start()
        for count in range(22):
            my_bike.accelerate()
        self.assertEqual(23, my_bike.check_speedometer())

        my_bike.accelerate()
        my_bike.accelerate()
        self.assertEqual(27, my_bike.check_speedometer())
        self.assertEqual(2, my_bike.check_gear())

    def test_accelerate_more_than_30_change_gear_3(self):
        my_bike = Bike()
        my_bike.start()
        for count in range(25):
            my_bike.accelerate()
        self.assertEqual(29, my_bike.check_speedometer())
        self.assertEqual(2, my_bike.check_gear())

        my_bike.accelerate()
        my_bike.accelerate()
        self.assertEqual(3, my_bike.check_gear())
        self.assertEqual(34, my_bike.check_speedometer())
