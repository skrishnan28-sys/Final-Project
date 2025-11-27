"""
Real-Time Leaderboard System - Integration Layer
Srinivas Krishnan - Primary implementer
"""
from bst import BinarySearchTree
from priority_queue import PriorityQueue, UpdateRequest
from player import Player
from datetime import datetime


class LeaderboardSystem:
    """
    Main leaderboard system that integrates BST and Priority Queue.
    Manages real-time player ranking with efficient updates.
    """
    
    def __init__(self):
        """Initialize the leaderboard system"""
        self.bst = BinarySearchTree()
        self.priority_queue = PriorityQueue()
        # Hash map for O(1) player lookups by ID
        self.player_lookup = {}  # player_id -> BSTNode
        self.update_count = 0  # Statistics tracking
    
    def submit_score_update(self, player_id, new_score, username=None, priority=None):
        """
        Submit a score update request to be processed.
        
        Args:
            player_id (str): ID of player
            new_score (int): New score for the player
            username (str, optional): Player's username (for new players)
            priority (float, optional): Priority of this update
        """
        # TODO: Create UpdateRequest and enqueue it
        # - Create UpdateRequest object
        # - Enqueue to priority queue
        # - Store username in temporary map if provided (for new players)
        pass
    
    def process_next_update(self):
        """
        Process the next highest-priority update from the queue.
        Dequeues one update and applies it to the BST.
        
        Returns:
            bool: True if an update was processed, False if queue was empty
        """
        # TODO: Implement update processing
        # - Dequeue from priority queue
        # - If player exists in BST:
        #   - Remove old node from BST
        #   - Create updated player with new score
        #   - Insert updated player into BST
        # - If player is new:
        #   - Create new player object
        #   - Insert into BST
        # - Update player_lookup hash map
        # - Increment update_count
        pass
    
    def process_all_updates(self):
        """
        Process all pending updates in the queue.
        Useful for batch processing.
        
        Returns:
            int: Number of updates processed
        """
        # TODO: Process updates until queue is empty
        # - Keep calling process_next_update() while queue is not empty
        # - Return count of updates processed
        pass
    
    def add_player(self, player_id, username, initial_score=0):
        """
        Directly add a player to the leaderboard (bypassing queue).
        Useful for initialization.
        
        Args:
            player_id (str): Unique player ID
            username (str): Player's display name
            initial_score (int): Starting score
        """
        # TODO: Implement direct player addition
        # - Create Player object
        # - Insert into BST
        # - Add to player_lookup
        pass
    
    def remove_player(self, player_id):
        """
        Remove a player from the leaderboard.
        
        Args:
            player_id (str): ID of player to remove
            
        Returns:
            bool: True if player was removed, False if not found
        """
        # TODO: Implement player removal
        # - Check if player exists in player_lookup
        # - Delete from BST
        # - Remove from player_lookup
        pass
    
    def get_leaderboard(self, top_n=None):
        """
        Get the current leaderboard rankings.
        
        Args:
            top_n (int, optional): Number of top players to return. If None, return all.
            
        Returns:
            list[Player]: Ranked list of players
        """
        # TODO: Get ranked players from BST
        # - If top_n specified, use bst.get_top_n(top_n)
        # - Otherwise, use bst.inorder_traversal()
        pass
    
    def get_player_rank(self, player_id):
        """
        Get a player's current rank.
        
        Args:
            player_id (str): Player ID
            
        Returns:
            int: Player's rank (1-indexed), or -1 if not found
        """
        # TODO: Get rank from BST
        # - Use bst.get_rank(player_id)
        pass
    
    def get_player_score(self, player_id):
        """
        Get a player's current score.
        
        Args:
            player_id (str): Player ID
            
        Returns:
            int: Player's score, or None if not found
        """
        # TODO: Lookup player and return score
        # - Check player_lookup hash map
        # - Return player.score if found
        pass
    
    def get_player_info(self, player_id):
        """
        Get complete information about a player.
        
        Args:
            player_id (str): Player ID
            
        Returns:
            dict: Player information including rank, score, username, or None if not found
        """
        # TODO: Gather all player information
        # - Check if player exists
        # - Get rank, score, username
        # - Return as dictionary
        pass
    
    def get_stats(self):
        """
        Get system statistics.
        
        Returns:
            dict: Statistics about the leaderboard system
        """
        return {
            'total_players': self.bst.get_size(),
            'pending_updates': self.priority_queue.get_size(),
            'total_updates_processed': self.update_count
        }
    
    def clear(self):
        """Clear all data from the leaderboard"""
        self.bst.clear()
        self.priority_queue.clear()
        self.player_lookup.clear()
        self.update_count = 0
    
    # Advanced features
    
    def simulate_tournament(self, num_players, num_rounds):
        """
        Simulate a tournament with random score updates.
        Useful for testing and demonstration.
        
        Args:
            num_players (int): Number of players
            num_rounds (int): Number of scoring rounds
        """
        # TODO: Optional feature for demo
        # - Generate random players
        # - Generate random score updates
        # - Submit updates and process them
        # - Print leaderboard periodically
        pass
    
    def get_nearby_players(self, player_id, range_above=2, range_below=2):
        """
        Get players ranked near a specific player.
        
        Args:
            player_id (str): Target player ID
            range_above (int): Number of players to show above target
            range_below (int): Number of players to show below target
            
        Returns:
            list[Player]: Players near the target player
        """
        # TODO: Optional feature
        # - Get player's rank
        # - Get leaderboard slice around that rank
        pass
    
    def export_leaderboard(self, filename):
        """
        Export current leaderboard to a file.
        
        Args:
            filename (str): Output file path
        """
        # TODO: Optional feature
        # - Get full leaderboard
        # - Write to file (CSV or JSON format)
        pass
