"""
Binary Search Tree implementation for storing players by score
Rider Gordon - Primary implementer
"""
from player import Player


class BSTNode:
    """
    Node in the Binary Search Tree.
    Each node stores a player and references to left/right children.
    """
    
    def __init__(self, player):
        """
        Initialize a BST node.
        
        Args:
            player (Player): The player object to store
        """
        self.player = player
        self.left = None
        self.right = None
        # Optional: Uncomment these for advanced features
        # self.height = 1  # For AVL balancing
        # self.subtree_size = 1  # For O(log n) rank queries


class BinarySearchTree:
    """
    Binary Search Tree for maintaining player rankings.
    Players are ordered by score (high to low), with player_id as tiebreaker.
    """
    
    def __init__(self):
        """Initialize an empty BST"""
        self.root = None
        self.size = 0
    
    def insert(self, player):
        """
        Insert a player into the BST.
        
        Args:
            player (Player): Player to insert
            
        Returns:
            BSTNode: The node that was inserted
        """
        # TODO: Implement insertion logic
        # - Handle empty tree case
        # - Recursively find correct position
        # - Create and return new node
        # - Update size
        pass
    
    def _insert_recursive(self, node, player):
        """
        Recursive helper for insertion.
        
        Args:
            node (BSTNode): Current node in recursion
            player (Player): Player to insert
            
        Returns:
            BSTNode: Root of the subtree after insertion
        """
        # TODO: Implement recursive insertion
        # - Base case: node is None, create new node
        # - Compare player with node.player
        # - Recursively insert in left or right subtree
        pass
    
    def delete(self, player_id):
        """
        Delete a player from the BST by player_id.
        
        Args:
            player_id (str): ID of player to delete
            
        Returns:
            bool: True if player was found and deleted, False otherwise
        """
        # TODO: Implement deletion logic
        # - Find the node with matching player_id
        # - Handle three cases:
        #   1. Node has no children (leaf)
        #   2. Node has one child
        #   3. Node has two children (find inorder successor/predecessor)
        # - Update size
        pass
    
    def _delete_recursive(self, node, player_id):
        """
        Recursive helper for deletion.
        
        Args:
            node (BSTNode): Current node in recursion
            player_id (str): ID of player to delete
            
        Returns:
            BSTNode: Root of the subtree after deletion
        """
        # TODO: Implement recursive deletion
        pass
    
    def _find_min(self, node):
        """
        Find the node with minimum value in a subtree.
        Used for finding inorder successor during deletion.
        
        Args:
            node (BSTNode): Root of subtree to search
            
        Returns:
            BSTNode: Node with minimum value
        """
        # TODO: Traverse left until you can't go further
        pass
    
    def search(self, player_id):
        """
        Search for a player by player_id.
        
        Args:
            player_id (str): ID of player to find
            
        Returns:
            Player: The player object if found, None otherwise
        """
        # TODO: Implement search
        # Note: This is O(n) worst case since we're searching by ID, not score
        # The integration layer will use a hash map for O(1) lookups
        pass
    
    def _search_recursive(self, node, player_id):
        """
        Recursive helper for search.
        
        Args:
            node (BSTNode): Current node in recursion
            player_id (str): ID of player to find
            
        Returns:
            Player: The player if found, None otherwise
        """
        # TODO: Check current node, then search both subtrees if needed
        pass
    
    def get_top_n(self, n):
        """
        Get the top N players (highest scores).
        
        Args:
            n (int): Number of top players to retrieve
            
        Returns:
            list[Player]: List of top N players, ordered by rank
        """
        # TODO: Use in-order traversal to get players in rank order
        # Since BST is ordered high-to-low, in-order gives ranked list
        pass
    
    def inorder_traversal(self):
        """
        Perform in-order traversal of the tree.
        Returns players in rank order (highest score first).
        
        Returns:
            list[Player]: All players in rank order
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        """
        Recursive helper for in-order traversal.
        
        Args:
            node (BSTNode): Current node
            result (list): List to accumulate players
        """
        # TODO: Implement in-order traversal
        # - Traverse left subtree
        # - Visit current node (append player to result)
        # - Traverse right subtree
        pass
    
    def get_rank(self, player_id):
        """
        Get the rank of a player (1-indexed, 1 = highest score).
        
        Args:
            player_id (str): ID of player
            
        Returns:
            int: Rank of the player, or -1 if not found
        """
        # TODO: Implement rank query
        # Simple approach: do in-order traversal and find position
        # Advanced approach: augment nodes with subtree_size for O(log n) queries
        pass
    
    def is_empty(self):
        """Check if tree is empty"""
        return self.root is None
    
    def get_size(self):
        """Get number of players in tree"""
        return self.size
    
    def clear(self):
        """Remove all players from the tree"""
        self.root = None
        self.size = 0


# Optional: AVL Tree implementation for self-balancing
class AVLTree(BinarySearchTree):
    """
    Self-balancing BST using AVL rotations.
    Only implement this if you have time after basic BST works.
    """
    
    def _get_height(self, node):
        """Get height of a node"""
        # TODO: Return node.height or 0 if node is None
        pass
    
    def _get_balance(self, node):
        """Get balance factor of a node"""
        # TODO: Return height(left) - height(right)
        pass
    
    def _rotate_left(self, z):
        """Perform left rotation"""
        # TODO: Implement left rotation
        pass
    
    def _rotate_right(self, z):
        """Perform right rotation"""
        # TODO: Implement right rotation
        pass
    
    def _rebalance(self, node):
        """Rebalance node if needed after insertion/deletion"""
        # TODO: Check balance factor and perform rotations
        pass
