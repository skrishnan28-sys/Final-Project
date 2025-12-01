"""
Binary Search Tree implementation for storing players by score
Rider Gordon
"""
from player import Player


class BSTNode:
    """
    Node in the Binary Search Tree.
    Each node stores a player and references to left and right children.
    """
    
    def __init__(self, player):
        """
        Initialize a BST node.
        """
        self.player = player
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    Binary Search Tree for storing player rankings.
    Players are ordered by score (high to low), with player_id as tiebreaker.
    """
    
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, player):
        """
        Insert a player into the BST.
        """
        # Initial empty tree - new player becomes the root
        if self.root is None:
            self.root = BSTNode(player)
            self.size += 1
            return self.root

        # The tree has nodes - insert recursively
        new_node = self.insert_recursively(self.root, player)
        self.size += 1
        return new_node

    def insert_recursively(self, node, player):
        """
        Insert into the BST tree recursively
        """
        if node is None:
            return BSTNode(player)

        if player < node.player:
            # if the new player has lower score  go left
            if node.left is None:
                node.left = BSTNode(player)
                return node.left
            else:
                return self.insert_recursively(node.left, player)
        else:
            # if the new player has higher score, go right
            if node.right is None:
                node.right = BSTNode(player)
                return node.right
            else:
                return self.insert_recursively(node.right, player)

    def delete(self, player_id):
        """
        Delete a player from the BST by player_id.
        """
        # Check if player exists first
        if self.search(player_id) is None:
            return False

        # delete recursively
        self.root = self.delete_recursively(self.root, player_id)
        self.size -= 1
        return True

    def delete_recursively(self, node, player_id):
        #recursive deletion
        if node is None:
            return None

        # Found the node to delete
        if node.player.player_id == player_id:
            #Leaf node (no children)
            if node.left is None and node.right is None:
                return None

            #Only right child
            elif node.left is None:
                return node.right

            #Only left child
            elif node.right is None:
                return node.left

            # both left and right children
            else:
                # Find inorder successor
                successor = self.find_min(node.right)

                # Replace current node's player with successor's player
                node.player = successor.player

                # Delete the successor from the right subtree
                node.right = self.delete_recursively(node.right, successor.player.player_id)

                return node

        # Not found at this node, search both subtrees
        node.left = self.delete_recursively(node.left, player_id)
        node.right = self.delete_recursively(node.right, player_id)

        return node

    def find_min(self, node):
        """
        Find the node with minimum value in a subtree.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, player_id):
        """
        Search for a player by player_id.
        """
        return self.search_recursively(self.root, player_id)

    def search_recursively(self, node, player_id):
        """
        helper function for search
        """
        if node is None:
            return None

        if node.player.player_id == player_id:
            return node.player

        left_result = self.search_recursively(node.left, player_id)
        if left_result is not None:
            return left_result

        return self.search_recursively(node.right, player_id)

    def inorder_traversal(self):
        """
        Perform in-order traversal of the tree.
        this returns players in low to high score.
        """
        result = []
        self.inorder_recursively(self.root, result)
        return result

    def inorder_recursively(self, node, result):
        """
        helper function for in-order traversal.
        """
        if node is None:
            return

        self.inorder_recursively(node.left, result)
        result.append(node.player)
        self.inorder_recursively(node.right, result)

    def reverse_inorder_traversal(self):
        """
        This returns players in order  of high to low score.
        This is what we want for  our leaderboard
        """
        result = []
        self.reverse_inorder_recursively(self.root, result)
        return result

    def reverse_inorder_recursively(self, node, result):
        """
        helper function for reverse in-order traversal.
        """
        if node is None:
            return

        self.reverse_inorder_recursively(node.right, result)  # Higher scores first
        result.append(node.player)
        self.reverse_inorder_recursively(node.left, result)  # Lower scores last

    def get_leaderboard(self):
        """
        Get the leaderboard
        """
        return self.reverse_inorder_traversal()

    def get_top_n(self, n):
        """
        Get the top N players with highest scores.
        """
        ranked_players = self.get_leaderboard()

        # Return only the first N players
        return ranked_players[:n]

    def get_rank(self, player_id):
        """
        Get the rank of a player.
        """
        # Get all players in order of high to low
        ranked_players = self.get_leaderboard()

        # Find the player's position
        for rank, player in enumerate(ranked_players, 1):
            if player.player_id == player_id:
                return rank

        # Player not found
        return -1

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

