import unittest
from lab1 import selectionSort
class Testinsertion(unittest.TestCase):
    
    def test_insertion(self):
     input_data = [3,4,2]
     sorted_data = selectionSort(input_data,3)
     expected_data = [2,3,4]
     self.assertEqual(sorted_data, expected_data)

if __name__ == '__main__':
    unittest.main()