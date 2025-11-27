"""
Priority Queue implementation for managing score update requests
Chase Barman - Primary implementer
"""
from datetime import datetime


class UpdateRequest:
    """
    Represents a score update request in the priority queue.
    """
    
    def __init__(self, player_id, new_score, priority=None, timestamp=None):
        """
        Initialize an update request.
        
        Args:
            player_id (str): ID of player to update
            new_score (int): New score for the player
            priority (float, optional): Priority value (higher = more important)
            timestamp (datetime, optional): When request was created
        """
        self.player_id = player_id
        self.new_score = new_score
        self.timestamp = timestamp or datetime.now()
        # Use timestamp as priority if not specified (earlier = higher priority)
        self.priority = priority if priority is not None else self.timestamp.timestamp()
    
    def __lt__(self, other):
        """
        Compare requests by priority for heap ordering.
        Higher priority values should come first (max-heap behavior).
        """
        # For max-heap: return self.priority > other.priority
        # For min-heap (FIFO by timestamp): return self.priority < other.priority
        return self.priority < other.priority
    
    def __repr__(self):
        """String representation for debugging"""
        return f"UpdateRequest({self.player_id}, score={self.new_score}, priority={self.priority})"


class PriorityQueue:
    """
    Min-heap based priority queue for managing update requests.
    Implemented from scratch without using Python's heapq.
    """
    
    def __init__(self):
        """Initialize an empty priority queue"""
        self.heap = []
        self.size = 0
    
    def enqueue(self, update_request):
        """
        Add an update request to the priority queue.
        
        Args:
            update_request (UpdateRequest): The request to add
        """
        # TODO: Implement enqueue
        # - Append request to end of heap
        # - Bubble up to maintain heap property
        # - Increment size
        pass
    
    def _bubble_up(self, index):
        """
        Bubble up element at index to maintain heap property.
        
        Args:
            index (int): Index of element to bubble up
        """
        # TODO: Implement bubble up
        # - While element is smaller than parent (for min-heap):
        #   - Swap with parent
        #   - Move to parent's index
        # - Parent index = (index - 1) // 2
        pass
    
    def dequeue(self):
        """
        Remove and return the highest priority request.
        
        Returns:
            UpdateRequest: The highest priority request, or None if queue is empty
        """
        # TODO: Implement dequeue
        # - Handle empty queue case
        # - Save root element (heap[0])
        # - Move last element to root
        # - Bubble down to maintain heap property
        # - Decrement size
        # - Return saved root
        pass
    
    def _bubble_down(self, index):
        """
        Bubble down element at index to maintain heap property.
        
        Args:
            index (int): Index of element to bubble down
        """
        # TODO: Implement bubble down
        # - While element has children and is larger than smallest child (for min-heap):
        #   - Find smallest child
        #   - Swap with smallest child
        #   - Move to child's index
        # - Left child index = 2 * index + 1
        # - Right child index = 2 * index + 2
        pass
    
    def peek(self):
        """
        View the highest priority request without removing it.
        
        Returns:
            UpdateRequest: The highest priority request, or None if queue is empty
        """
        # TODO: Return heap[0] if not empty, else None
        pass
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            bool: True if queue is empty
        """
        return self.size == 0
    
    def get_size(self):
        """
        Get the number of requests in the queue.
        
        Returns:
            int: Number of requests
        """
        return self.size
    
    def clear(self):
        """Remove all requests from the queue"""
        self.heap = []
        self.size = 0
    
    def heapify(self, requests):
        """
        Build a heap from a list of update requests.
        More efficient than repeated insertions.
        
        Args:
            requests (list[UpdateRequest]): List of requests to heapify
        """
        # TODO: Implement heapify
        # - Set heap to the requests list
        # - Set size
        # - Start from last non-leaf node and bubble down each
        # - Last non-leaf node index = (size // 2) - 1
        pass
    
    # Optional: Advanced features
    
    def merge_requests(self, player_id):
        """
        Check if there are multiple pending requests for the same player
        and optionally merge them (keep only the most recent).
        
        Args:
            player_id (str): Player to check for duplicate requests
            
        Returns:
            int: Number of duplicate requests found
        """
        # TODO: Optional feature - scan heap for duplicate player_id entries
        # This is complex because removing from middle of heap requires re-heapifying
        pass
    
    def update_priority(self, player_id, new_priority):
        """
        Update the priority of a request for a given player.
        
        Args:
            player_id (str): Player whose request priority to update
            new_priority (float): New priority value
            
        Returns:
            bool: True if request was found and updated
        """
        # TODO: Optional feature - find request and update its priority
        # Then bubble up or down as needed
        pass
