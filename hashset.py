from linkedList import *

class Hashset:
  def __init__ (self,bucketCount):
    self.hashl = list()
    for i in range(bucketCount):
      self.hashl.append(LinkedList())

  def addItem (self, item):
    hashItem = hash(item)
    pos = hashItem % len(self.hashl)
    targetll = self.hashl[pos]
    if not targetll.contains(item):
      targetll.addToEnd(item)

  def containsHash(self,item):
    hashItem = hash(item)
    pos = hashItem % len(self.hashl)
    targetll = self.hashl[pos]
    return targetll.contains(item)

  def removeHash(self,item):
    hashItem = hash(item)
    pos = hashItem % len(self.hashl)
    targetll = self.hashl[pos]
    targetll.removeBox(item)

  def printHS (self):
    print("HASH SET")
    print("----------")
    for i in range(len(self.hashl)):
      print (str(i)+':')
      self.hashl[i].LLprint()
    print("----------")