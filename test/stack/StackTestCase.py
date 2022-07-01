import unittest

from dsa.stack.Stack import Stack

class StackTestCase(unittest.TestCase):

  def test_init(self):
    stack = Stack()
    
    self.assertEqual(
        0, len(stack),
        f"Stack size is incorrect, expected 0, get {len(stack)}.")

  def test_push(self):
    stack = Stack()
    stack.push(0)
    stack.push(1)
    stack.push(2)
    
    self.assertEqual(
        3, len(stack),
        f"Stack size is incorrect, expected 3, get {len(stack)}.")
    
    self.assertEqual(
        4, len(stack.data),
        f"Stack array size is incorrect, expected 4, get {len(stack.data)}.")

    expected_results = [2, 1, 0]
    for expected, elem in zip(expected_results, stack):
      self.assertEqual(
          expected, elem,
          f"Stack element is not correct, expected {expected}, get {elem}."
      )
  
  def test_pop(self):
    stack = Stack()
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
    
    self.assertEqual(
        2, len(stack.data),
        f"Stack array size is incorrect, expected 2, get {len(stack.data)}.")

  def test_push_after_pop(self):
    stack = Stack()
    for i in range(0, 3):
      stack.push(i)
    for i in range(0, 3):
      stack.pop()
    for i in range(0, 3):
      stack.push(i)
    
    self.assertEqual(
        3, len(stack),
        f"Stack size is incorrect, expected 3, get {len(stack)}.")
    
    self.assertEqual(
        4, len(stack.data),
        f"Stack array size is incorrect, expected 4, get {len(stack.data)}.")

    expected_results = [2, 1, 0]
    for expected, elem in zip(expected_results, stack):
      self.assertEqual(
          expected, elem,
          f"Stack element is not correct, expected {expected}, get {elem}."
      )
