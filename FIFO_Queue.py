"""
FIFO Queue Implementation. Ensures scores are enqueued and dequeued in the order of arrival
Chase Barman
"""
from datetime import datetime


class UpdateRequest:
    """
    Represents a score update request.
    """

    def __init__(self, player_id, new_score, timestamp=None):
        """
        Initialize an update request.
        """
        self.player_id = player_id
        self.new_score = new_score
        self.timestamp = timestamp or datetime.now()


class FIFOQueueList:

    def __init__(self, compact_threshold=100):
        """
        Initialize an empty FIFO queue.
        """
        self.items = []  # The actual storage
        self.front = 0  # Index of front element

    def enqueue(self, update_request):
        """
        Add an update request to the end of the queue.
        Time Complexity: O(1)
        """
        self.items.append(update_request)

    def dequeue(self):
        """
        Remove and return the oldest update request (FIFO).
        Time Complexity: O(1), unlike the pop() method which is O(n)
        Potential Problem: Since no items are actually removed from the queue, the queue size can grow by a lot.
        """
        if self.is_empty():
            return None

        # Get the element at front
        item = self.items[self.front]

        # Move the front pointer forward
        self.front += 1

        return item


    def peek(self):
        """
        View the next element without removing it.
        Time Complexity: O(1)
        """
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        """
        Check if the queue is empty.
        """
        return self.front >= len(self.items)

    def get_size(self):
        """
        Get the number of requests in the queue.
        """
        return len(self.items) - self.front

    def clear(self):
        """Remove all requests from the queue"""
        self.items = []
        self.front = 0


