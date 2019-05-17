class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current < len(self.storage):
      self.storage[self.current] = item
      self.current += 1
      return self.storage
    else:
      self.current = 0
      return self.append(item)

  def get(self):
    result = []
    for i in range(len(self.storage)):
      if self.storage[i] is not None:
        result.append(self.storage[i])
    return result