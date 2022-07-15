import unittest

from dsa.hash_table.SeparateChainingHashTable import LinearProbingHashTable

class SeparateChainingHashTableTestCase(unittest.TestCase):

  def test_setitem(self):
    hash_table = LinearProbingHashTable()
    for i in range(0, 5):
      for j in range(0, 5):
        hash_table[f'{i}/{j}'] = 10 * i + j

    for i in range(0, 5):
      for j in range(0, 5):
        self.assertEqual(
            hash_table[f'{i}/{j}'], 10 * i + j,
            ''.join((
                f"Incorrect value in {self.__class__.__name__}",
                f"expected {10 * i + j}, get {hash_table[f'{i}/{j}']}." 
            )))
  
  def test_delitem(self):
    hash_table = LinearProbingHashTable()
    for i in range(0, 5):
      for j in range(0, 5):
        hash_table[f'{i}/{j}'] = 10 * i + j

    for i in range(0, 4):
      for j in range(0, 4):
        del hash_table[f'{i}/{j}']

    for i in range(4, 5):
      for j in range(4, 5):
        self.assertEqual(
            hash_table[f'{i}/{j}'], 10 * i + j,
            ''.join((
                f"Incorrect value in {self.__class__.__name__}",
                f"expected {10 * i + j}, get {hash_table[f'{i}/{j}']}." 
            )))