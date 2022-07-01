import unittest

from dsa.queue.LinkedQueue import LinkedQueue

class LinkedQueueTestCase(unittest.TestCase):

  def test_init(self):
    queue = LinkedQueue()
    
    self.assertEqual(
        0, len(queue),
        f"Queue size is incorrect, expected 0, get {len(queue)}.")

  def test_enqueue(self):
    queue = LinkedQueue()
    for i in range(0, 3):
      queue.enqueue(i)
    
    self.assertEqual(
        3, len(queue),
        f"Queue size is incorrect, expected 3, get {len(queue)}.")
    
    expected_results = [0, 1, 2]
    for expected, elem in zip(expected_results, queue):
      self.assertEqual(
          expected, elem,
          f"Queue element is not correct, expected {expected}, get {elem}."
      )
  
  def test_dequeue(self):
    queue = LinkedQueue()
    for i in range(0, 3):
      queue.enqueue(i)
    
    expected_results = [0, 1, 2]
    for expected in expected_results:
      elem = queue.dequeue()
      self.assertEqual(
          expected, elem,
          f"Queue element is not correct, expected {expected}, get {elem}."
      )
    
    self.assertEqual(
        0, len(queue),
        f"Queue size is incorrect, expected 0, get {len(queue)}.")
    
  def test_queue_after_enqueue(self):
    queue = LinkedQueue()
    for i in range(0, 3):
      queue.enqueue(i)
    for i in range(0, 3):
      queue.dequeue()
    for i in range(0, 3):
      queue.enqueue(i)

    self.assertEqual(
        3, len(queue),
        f"Queue size is incorrect, expected 3, get {len(queue)}.")
    
    expected_results = [0, 1, 2]
    for expected, elem in zip(expected_results, queue):
      self.assertEqual(
          expected, elem,
          f"Queue element is not correct, expected {expected}, get {elem}."
      )
