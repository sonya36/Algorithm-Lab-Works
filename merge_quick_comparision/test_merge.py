import unittest
from merge_sort import mergesort
class Testmerge(unittest.TestCase):
    
    def test_merge(self):
     input_data = [38, 27, 43, 3, 9, 82, 10]
     sorted_data = mergesort(input_data,0,len(input_data)-1)
     expected_data = [3, 9, 10, 27, 38, 43, 82]
     self.assertEqual(sorted_data, expected_data)

if __name__ == '__main__':
    unittest.main()