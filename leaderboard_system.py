"""
Real-Time Multiplayer Leaderboard System
Srinivas Krishnan
"""
from bst import BinarySearchTree
from player import Player
from FIFO_Queue import FIFOQueueList, UpdateRequest
from datetime import datetime


class LeaderboardSystem:
    """
    Complete leaderboard system integrating all components.

    Design:
    1. Updates arrive → Enqueued in FIFO Queue
    2. Process queue → Apply to BST in order
    3. Rankings → Retrieved from BST

    Features:
    - Real-time score updates
    - FIFO processing order
    - O(1) player lookup via hash map
    - O(log n) BST operations
    """

    def __init__(self):
        """Initialize the leaderboard system"""
        # Core data structures
        self.bst = BinarySearchTree()  # Rankings storage
        self.update_queue = FIFOQueueList()  # Pending updates
        self.player_lookup = {}  # player_id → Player

        # Statistics
        self.total_updates = 0
        self.updates_processed = 0

    def submit_score(self, player_id, username, score):
        """
        Submit a score update for a player.
        The update is placed in the queued for processing.
        Time Complexity: O(1) - just enqueues
        """
        update = UpdateRequest(player_id, score)
        update.username = username  # Store username in update
        self.update_queue.enqueue(update)
        self.total_updates += 1

        print(f"Queued update: {username} ({player_id}) -> {score}")

    def process_updates(self):
        """
        Process pending updates from the queue.
        Updates are applied to BST in FIFO order.
        Time Complexity: O(log n) , where n = total players
        """
        processed = 0

        print(f"\nProcessing updates...")

        while not self.update_queue.is_empty():

            # Dequeue next update (FIFO order)
            update = self.update_queue.dequeue()

            # Check if player already exists
            if update.player_id in self.player_lookup:
                # Player exists - remove old score from BST
                old_player = self.player_lookup[update.player_id]
                self.bst.delete(update.player_id)
                print(f"  Updated: {old_player.username} {old_player.score} -> {update.new_score}")
            else:
                # New player
                print(f"  Added: {update.username} -> {update.new_score}")

            # Create new player object
            new_player = Player(update.player_id, update.username, update.new_score)

            # Insert into BST
            self.bst.insert(new_player)

            # Update lookup table
            self.player_lookup[update.player_id] = new_player

            processed += 1
            self.updates_processed += 1

        if processed > 0:
            print(f"Processed {processed} updates")
        else:
            print(f"No updates to process")

    def get_leaderboard(self, top_n=None):
        """
        Get current leaderboard rankings.
        Time Complexity: O(n) for full leaderboard, O(n) for top n
        """
        if top_n is None:
            return self.bst.get_leaderboard()
        else:
            return self.bst.get_top_n(top_n)

    def get_player_rank(self, player_id):
        """
        Get a specific player's rank.
        Time Complexity: O(n)
        """
        return self.bst.get_rank(player_id)

    def get_player(self, player_id):
        """
        Get a player's information.
        Time Complexity: O(1) via hash map
        """
        return self.player_lookup.get(player_id)

    def display_leaderboard(self, top_n=10):
        """
        Pretty-print the leaderboard.
        """
        leaderboard = self.get_leaderboard(top_n)

        print("\n-----------------------------------------------")
        print("LEADERBOARD")
        print("\n-----------------------------------------------")

        if not leaderboard:
            print("No players yet!")
        else:
            print(f"{'Rank'} {'Player'} {'Score'}")
            print("\n-----------------------------------------------")

            for rank, player in enumerate(leaderboard, 1):
                # Add medals for top 3
                if rank == 1:
                    medal = "[1st]"
                elif rank == 2:
                    medal = "[2nd]"
                elif rank == 3:
                    medal = "[3rd]"
                else:
                    medal = "     "

                print(f"{medal} {rank} {player.username} {player.score}")

        print("\n-----------------------------------------------")

    def display_player_info(self, player_id):
        """
        Display detailed information about a player.
        """
        player = self.get_player(player_id)

        if not player:
            print(f"Player {player_id} not found")
            return

        rank = self.get_player_rank(player_id)

        print("\n-----------------------------------------------")
        print(f"Player: {player.username}")
        print(f"ID: {player.player_id}")
        print(f"Score: {player.score}")
        print(f"Rank: #{rank}")
        print("\n-----------------------------------------------")

    def get_stats(self):
        """
        Get system statistics.
        """
        return {
            'total_players': self.bst.get_size(),
            'pending_updates': self.update_queue.get_size(),
            'total_updates_submitted': self.total_updates,
            'updates_processed': self.updates_processed,
            'bst_size': self.bst.get_size(),
        }

    def display_stats(self):
        """Display system statistics"""
        stats = self.get_stats()

        print("\n-----------------------------------------------")
        print(" SYSTEM STATISTICS ")
        print("\n-----------------------------------------------")
        print(f"  Total Players:{stats['total_players']}")
        print(f"  Pending Updates:{stats['pending_updates']}")
        print(f"  Updates Submitted:{stats['total_updates_submitted']}")
        print(f"  Updates Processed:{stats['updates_processed']}")
        print("\n-----------------------------------------------")

    def remove_player(self, player_id):
        """
        Remove a player from the leaderboard.
        """
        if player_id not in self.player_lookup:
            return False

        # Remove from BST
        self.bst.delete(player_id)

        # Remove from lookup
        player = self.player_lookup.pop(player_id)

        print(f"Removed player: {player.username}")
        return True

    def clear_leaderboard(self):
        """Clear all players and pending updates"""
        self.bst.clear()
        self.update_queue.clear()
        self.player_lookup.clear()
        self.total_updates = 0
        self.updates_processed = 0

        print("Leaderboard cleared")

