class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # we found it and we have used it so we add to the end of the cache (aka most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # if existing update value and move it to the most recently used
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            #remove least recently used (aka beggining of list)
            self.cache.popitem(last = False)
