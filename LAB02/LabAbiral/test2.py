import unittest
from function import generate_sorted_array,generate_unsorted_array,random
from function2 import QuickSorting,MergeSorting


class TestQuickSorting(unittest.TestCase):
    def test_QuickSorting_randomarray(self):
        unsorted_array =generate_unsorted_array(10)
        sorted_array=sorted(unsorted_array)
        self.assertListEqual(QuickSorting(unsorted_array)[0], sorted_array)
        
    def test_QuickSorting_empty(self):
        self.assertListEqual(QuickSorting([])[0], [])
        
    def test_QuickSorting_unitelement(self):
        self.assertListEqual(QuickSorting([0])[0], [0])

  

    def test_QuickSorting_repeatedelement(self):
        unsorted_array= [-1,2,2,2,-1,0,0,0,3,7,-7,3]
        sorted_array= [-7,-1,-1,0,0,0,2,2,2,3,3,7]
        self.assertListEqual(QuickSorting(unsorted_array)[0], sorted_array)
    
    def test_QuickSorting_reversearray(self):
        unsorted_array= [27, 18, 15, 12, 9,6,3,1]
        sorted_array= [1,3,6,9,12,15,18,27]
        self.assertListEqual(QuickSorting(unsorted_array)[0], sorted_array)
        
    def test_QuickSorting_negativeelement(self):
        unsorted_array=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        sorted_array=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
        self.assertListEqual(QuickSorting(unsorted_array)[0], sorted_array)


class TestMergeSorting(unittest.TestCase):
    def test_MergeSorting_randomarray(self):
        unsorted_array =generate_unsorted_array(10)
        sorted_array=sorted(unsorted_array)
        self.assertListEqual(MergeSorting(unsorted_array)[0], sorted_array)
        
    def test_MergeSorting_empty(self):
        self.assertListEqual(MergeSorting([])[0], [])
    
    def test_MergeSorting_reversearray(self):
        unsorted_array= [27, 18, 15, 12, 9,6,3,1]
        sorted_array= [1,3,6,9,12,15,18,27]
        self.assertListEqual(MergeSorting(unsorted_array)[0], sorted_array)

    def test_MergeSorting_unitelement(self):
        self.assertListEqual(MergeSorting([0])[0], [0])

    def test_MergeSorting_repeatedelement(self):
        unsorted_array= [-1,2,2,2,-1,0,0,0,3,7,-7,3]
        sorted_array= [-7,-1,-1,0,0,0,2,2,2,3,3,7]
        self.assertListEqual(MergeSorting(unsorted_array)[0], sorted_array)
    
    def test_MergeSorting_negativeelement(self):
        unsorted_array=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        sorted_array=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
        self.assertListEqual(MergeSorting(unsorted_array)[0], sorted_array)

if __name__ == "__main__":
    unittest.main()