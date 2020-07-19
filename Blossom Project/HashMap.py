from linked_list import Node, LinkedList
class HashMap:
  def __init__(self,size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]

  def hash(self,key):
    hash_code = sum(key.encode())
    return hash_code

  def compression(self,hash_code):
    return hash_code%self.array_size
  
  def assign(self,key,value):
    array_index = self.compression(self.hash(key))
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for List in list_at_array:
      if List[0] == key:
        List[1] = value
    list_at_array.insert(payload)

  def retrieve(self,key):
    array_index = self.compression(self.hash(key))
    list_at_index = self.array[array_index]

    payload = self.array[array_index]
    for List in list_at_index:
      if List[0] != None:
        if List[0] == key:
          return List[1]
    else:
      return None
  
from blossom_lib import flower_definitions
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0],flower[1])
print(blossom.retrieve('daisy'))
  

