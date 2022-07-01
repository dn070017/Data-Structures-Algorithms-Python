import unittest

from dsa.stack.LinkedStack import LinkedStack

class LinkedStackTestCase(unittest.TestCase):

  def test_init(self):
    stack = LinkedStack()
    
    self.assertEqual(
        0, len(stack),
        f"Stack size is incorrect, expected 0, get {len(stack)}.")

  def test_push(self):
    stack = LinkedStack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    
    self.assertEqual(
        3, len(stack),
        f"Stack size is incorrect, expected 3, get {len(stack)}.")
    
    expected_results = [2, 1, 0]
    for expected, elem in zip(expected_results, stack):
      self.assertEqual(
          expected, elem,
          f"Stack element is not correct, expected {expected}, get {elem}."
      )
  
  def test_pop(self):
    stack = LinkedStack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    
    expected_results = [2, 1, 0]
    for expected in expected_results:
      elem = stack.pop()
      self.assertEqual(
          expected, elem,
          f"Stack element is not correct, expected {expected}, get {elem}."
      )
    
    self.assertEqual(
        0, len(stack),
        f"Stack size is incorrect, expected 0, get {len(stack)}.")
    
  def test_push_after_pop(self):
    stack = LinkedStack()
    for i in range(0, 3):
      stack.push(i)
    for i in range(0, 3):
      stack.pop()
    for i in range(0, 3):
      stack.push(i)
    
    self.assertEqual(
        3, len(stack),
        f"Stack size is incorrect, expected 3, get {len(stack)}.")
    
    expected_results = [2, 1, 0]
    for expected, elem in zip(expected_results, stack):
      self.assertEqual(
          expected, elem,
          f"Stack element is not correct, expected {expected}, get {elem}."
      )
