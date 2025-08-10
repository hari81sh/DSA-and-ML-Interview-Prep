import unittest
import python_practice
print(unittest.__file__)

class test_arrays_unit(unittest.TestCase):

    
    def test_words_containing_one(self):  # Renamed to start with 'test_'
        words = python_practice.Words_Containing_Character
        self.assertEqual(words.findWordsContaining(words=["leet","code"], x='e'), [0,1])
        print("Test 'test_words_containing_one' passed successfully!")


    def test_build_array_from_permutation(self):
        arr = python_practice.Build_Array_from_permutation
        self.assertEqual(arr.build_array([0,2,1,5,3,4]),[0, 1, 2, 4, 5, 3])
        print("Test 'test_build_array_from_permutation' passed successfully!")

if __name__ =="__main__":
    unittest.main()