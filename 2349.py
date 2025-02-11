class NumberContainers(object):

    def __init__(self):
        self.number_to_index = defaultdict(list)
        self.index_to_number = {}

    def change(self, index, number):
        if self.index_to_number.get(index) == number:
            return

        self.index_to_number[index] = number
        heapq.heappush(self.number_to_index[number], index)

    def find(self, number):
        heap = self.number_to_index[number]
        while len(heap) != 0:
            if self.index_to_number[heap[0]] == number:
                return heap[0]
            heapq.heappop(heap)
        return -1
