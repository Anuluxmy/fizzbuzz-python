 import unittest
 from fizzbuzz import Fizzbuzz

 class FizzbuzzTestCase(unittest.TestCase):

  def test_15(self):
    self.assertEqual(unittest(15), 'FizzBuzz')

  def test_5(self):
    self.assertEqual(unittest(5), 'Buzz')

  def test_3(self):
    self.assertEqual(unittest(3), 'Fizz')
  def test_7(self):
    self.assertEqual(unittest(7), 7)


  if __name__ == '__main__':
    unittest.main()