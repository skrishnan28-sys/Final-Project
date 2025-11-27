"""
Player class - represents a player in the leaderboard system
"""
from datetime import datetime


class Player:
    """
    Represents a player with a score and other metadata.
    Players are compared by score (and player_id as tiebreaker).
    """
    
    def __init__(self, player_id, username, score, timestamp=None):
        """
        Initialize a player.
        
        Args:
            player_id (str): Unique identifier for the player
            username (str): Display name for the player
            score (int): Current score
            timestamp (datetime, optional): When score was last updated
        """
        self.player_id = player_id
        self.username = username
        self.score = score
        self.timestamp = timestamp or datetime.now()
    
    def __lt__(self, other):
        """
        Compare players for ordering in BST.
        Primary: by score (descending - higher scores first)
        Secondary: by player_id (ascending - for consistent tiebreaking)
        """
        if self.score != other.score:
            return self.score > other.score  # Higher scores come "first" (left in tree)
        return self.player_id < other.player_id
    
    def __eq__(self, other):
        """Check if two players are the same (by player_id)"""
        return self.player_id == other.player_id
    
    def __repr__(self):
        """String representation for debugging"""
        return f"Player({self.player_id}, {self.username}, score={self.score})"
    
    def __str__(self):
        """Human-readable string"""
        return f"{self.username}: {self.score}"
