import os
import unittest

import sensors


class UnitTest(unittest.TestCase):
    def test_missing_chosen_lib(self):
        with self.assertRaises(OSError):
            sensors.SensorsReader(lib_path='/p/y/s/e/n/s/o/r/s/2/')

    def test_invalid_lib(self):
        with self.assertRaises(OSError):
            sensors.SensorsReader(lib_path=os.path.dirname(__file__) + '/sensors.py')


class CIIntegrationTest(unittest.TestCase):
    def test_get_data(self):
        reader = sensors.SensorsReader()
        reader.get_data()
        self.assertTrue(True)


class UserIntegrationTest(unittest.TestCase):
    def test_get_data(self):
        reader = sensors.SensorsReader()
        self.assertTrue(len(reader.get_data().keys()) > 0)

    def test_get_cpu_temp(self):
        reader = sensors.SensorsReader()
        self.assertIsNotNone(reader.get_cpu_temp())


if __name__ == '__main__':
    unittest.main()
