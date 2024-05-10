import unittest
from lab1 import insertionSort
class Testinsertion(unittest.TestCase):
    
    def test_insertion(self):
     input_data = [3,4,2]
     sorted_data = insertionSort(input_data)
     expected_data = [2,3,4]
     self.assertEqual(sorted_data, expected_data)

if __name__ == '__main__':
    unittest.main()