#%%
from __future__ import annotations
from abc import ABCMeta, abstractmethod
from collections.abc import MutableMapping, Iterator
from typing import Any, TypeVar

class Comparable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

ComparableT = TypeVar('ComparableT', bound=Comparable)

class BinarySearchTreeIterator(Iterator):
  def __init__(self, bst: BinarySearchTree):
    self.bst = bst
    self.result = list()
    self.inorder(self.bst.root)
    self.iterator = iter(self.result)

  def __iter__(self) -> BinarySearchTreeIterator:
    return self

  def __next__(self) -> ComparableT:
    return next(self.iterator)

  def inorder(self, node: BinarySearchTreeNode):
    if node is not None:
      self.inorder(node.left)
      self.result.append(node.key)
      self.inorder(node.right)
    return

class BinarySearchTreeNode:
  def __init__(self, key: ComparableT, value: Any):
    self.key = key
    self.value = value
    self.left: BinarySearchTreeNode = None
    self.right: BinarySearchTreeNode = None

  def __repr__(self) -> str:
    return f"{self.__class__.__name__}({{{self.key}: {self.value}}})"

class BinarySearchTree(MutableMapping):
  def __init__(self):
    self.n: int = 0
    self.root: BinarySearchTreeNode = None

  def __setitem__(self, key: ComparableT, value: Any) -> None:
    if self.n == 0:
      self.root = BinarySearchTreeNode(key, value)
      self.n += 1
      return
    else:
      self.root = self.insert(self.root, key, value)
      return

  def __getitem__(self, key: ComparableT) -> Any:
    node = self.root
    while node is not None:
      if key > node.key:
        node = node.right
      elif key < node.key:
        node = node.left
      else:
        return node.value
    raise KeyError(f'{key}')

  def __delitem__(self, key: ComparableT) -> None:
    self.delete(self.root, key)
    self.n -= 1
    return

  def insert(
      self,
      node: BinarySearchTreeNode,
      key: ComparableT,
      value: Any) -> BinarySearchTreeNode:
    if node is None:
      self.n += 1
      return BinarySearchTreeNode(key, value)

    if key < node.key:
      node.left = self.insert(node.left, key, value)
    elif key > node.key:
      node.right = self.insert(node.right, key, value)
    else:
      node.value = value
    return node

  def delete(
      self,
      node: BinarySearchTreeNode,
      key: ComparableT) -> BinarySearchTreeNode:
    if node is None:
      raise KeyError(f'{key}')
    
    if key < node.key:
      node.left = self.delete(node.left, key)
    elif key > node.key:
      node.right = self.delete(node.right, key)
    else:
      if node.left is None:
        temp = node.right
        node = None
        return temp 
      elif node.right is None:
        node = node.left
        node = None
        return temp
      else:
        temp = self.min_of_subtree(node.right)
        node.key = temp.key
        node.value = temp.value
        node.right = self.delete(node.right, temp.key)

    return node

  def min_of_subtree(
      self,
      node: BinarySearchTreeNode) -> BinarySearchTreeNode:
    while node.left is not None:
      node = node.left
    return node

  def __iter__(self) -> BinarySearchTreeIterator:
    return BinarySearchTreeIterator(self)

  def __len__(self) -> int:
    return self.n