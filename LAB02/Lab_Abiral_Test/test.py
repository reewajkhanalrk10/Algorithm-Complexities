import unittest
from function import selectionsort,insertionsort,generate_sorted_array,generate_unsorted_array,random

class Testselectionsort(unittest.TestCase):
    def test_selectionsort_randomarray(self):
        unsorted_array =generate_unsorted_array(10)
        sorted_array=sorted(unsorted_array)
        self.assertListEqual(selectionsort(unsorted_array)[0], sorted_array)
        
    def test_selectionsort_empty(self):
        self.assertListEqual(selectionsort([])[0], [])
        
    def test_selectionsort_unitelement(self):
        self.assertListEqual(selectionsort([0])[0], [0])

  

    def test_selectionsort_repeatedelement(self):
        unsorted_array= [-1,2,2,2,-1,0,0,0,3,7,-7,3]
        sorted_array= [-7,-1,-1,0,0,0,2,2,2,3,3,7]
        self.assertListEqual(selectionsort(unsorted_array)[0], sorted_array)
    
    def test_selectionsort_reversearray(self):
        unsorted_array= [27, 18, 15, 12, 9,6,3,1]
        sorted_array= [1,3,6,9,12,15,18,27]
        self.assertListEqual(selectionsort(unsorted_array)[0], sorted_array)
        
    def test_selectionsort_negativeelement(self):
        unsorted_array=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        sorted_array=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
        self.assertListEqual(selectionsort(unsorted_array)[0], sorted_array)


class Testinsertionsort(unittest.TestCase):
    def test_insertionsort_randomarray(self):
        unsorted_array =generate_unsorted_array(10)
        sorted_array=sorted(unsorted_array)
        self.assertListEqual(insertionsort(unsorted_array)[0], sorted_array)
        
    def test_insertionsort_empty(self):
        self.assertListEqual(insertionsort([])[0], [])
    
    def test_insertionsort_reversearray(self):
        unsorted_array= [27, 18, 15, 12, 9,6,3,1]
        sorted_array= [1,3,6,9,12,15,18,27]
        self.assertListEqual(insertionsort(unsorted_array)[0], sorted_array)

    def test_insertionsort_unitelement(self):
        self.assertListEqual(insertionsort([0])[0], [0])

    def test_insertionsort_repeatedelement(self):
        unsorted_array= [-1,2,2,2,-1,0,0,0,3,7,-7,3]
        sorted_array= [-7,-1,-1,0,0,0,2,2,2,3,3,7]
        self.assertListEqual(insertionsort(unsorted_array)[0], sorted_array)
    
    def test_insertionsort_negativeelement(self):
        unsorted_array=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
        sorted_array=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1]
        self.assertListEqual(insertionsort(unsorted_array)[0], sorted_array)



if __name__ == "__main__":
    unittest.main()