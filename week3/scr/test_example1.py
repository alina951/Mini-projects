# # test_additions.py
# def add_two_numbers(a, b):
#     print('The function started...')
#     return a + b

# def test_add_two_numbers():
#     expected = 5
#     actual = add_two_numbers(4, 1)
#     assert expected == actual

#import random 

#def mock_random_number_genernator():
 #   return 7
#def test_random_list_genertator():
 #   list_length =3 
  #  expected = [7,7,7]
   # result = random_list_geerator(list_length, mock_random_number_genernator)
    #assert expected == result 
import random
import unittest
def get_random_number():
    return  random.randint(1,10)

def random_list_geerator(n):
    result = []

    for _ in range(n):
        result.append(get_random_number())
        return result
    
def mock_random_number_genernator():
        return 7
class TestRandomListGenerator(unittest.TestCase):
    def test_random_list_genertator(self):
     list_length =3 
     expected = [7,7,7]
     result = random_list_geerator(list_length, mock_random_number_genernator)
     self.assertEqual(result, expected)

if __name__ == "_main_":
    unittest.main()     

#test_random_list_genertator()
