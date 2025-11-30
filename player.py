"""
Player class - represents a player in the leaderboard system
"""
from datetime import datetime


class Player:
    """
    Represents a player with a score and other information.
    Players are compared by score (and player_id as tiebreaker).
    """
    
    def __init__(self, player_id, username, score, timestamp=None):
        """
        Initialize a player.
        """
        self.player_id = player_id
        self.username = username
        self.score = score
        self.timestamp = timestamp or datetime.now()
    
    def __lt__(self, other):
        """
        Compare players for ordering in BST.
        Primary: by score (ascending - lower scores first)
        Secondary: by player_id (ascending - for consistent tiebreaking)
        """
        if self.score != other.score:
            return self.score < other.score  # Standard comparison: lower < higher
        return self.player_id < other.player_id
    
    def __eq__(self, other):
        """Check if two players are the same (by player_id)"""
        return self.player_id == other.player_id


    def __str__(self):
        """Human-readable string"""
        return f"{self.username}: {self.score}"
