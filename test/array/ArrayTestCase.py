import unittest

from dsa.array.Array import Array

class ArrayTestCase(unittest.TestCase):

  def test_init(self):
    size = 5
    array = Array(size)
    
    self.assertEqual(
        size, len(array),
        f"Array size is incorrect, expected {size}, get {len(array)}.")
    self.assertEqual(
        size, array.n,
        f"Array attribute (n) is incorrect, expected {size}, get {len(array)}.")

  def test_set(self):
    size = 3
    array = Array(size)
    array[0] = 0
    array[1] = 1
    array[2] = 2
    for i, elem in enumerate(array):
      self.assertEqual(
          elem, i,
          f"Array element at index {i} is not correct, expected {i}, get {elem}."
      )

  def test_resize(self):
    size = 3
    array = Array(size)
    array[0] = 0
    array[1] = 1
    array.resize(2 * size)
    for i, elem in enumerate(array[0:2]):
      self.assertEqual(
          elem, i,
          f"Array element after resize at index {i} is not correct, expected {i}, get {elem}."
      ) 
    
    self.assertEqual(
        2 * size, len(array),
        f"Array size is incorrect, expected {2 * size}, get {len(array)}.")

  def test_resize_with_start(self):
    size = 6
    array = Array(size)
    array[3] = 0
    array[4] = 1
    array.resize(size // 2, 3)
    for i, elem in enumerate(array[0:2]):
      self.assertEqual(
          elem, i,
          f"Array element after resize at index {i} is not correct, expected {i}, get {elem}."
      )
    
    self.assertEqual(
        size // 2, len(array),
        f"Array size is incorrect, expected {size // 2}, get {len(array)}.")

