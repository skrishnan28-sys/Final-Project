"""
Command-line interface for the Real-Time Leaderboard System
Srinivas Krishnan - Integration and demo
"""
from leaderboard_system import LeaderboardSystem
from player import Player
import random
import time


class LeaderboardCLI:
    """Interactive command-line interface for the leaderboard system"""
    
    def __init__(self):
        """Initialize the CLI with a leaderboard system"""
        self.system = LeaderboardSystem()
        self.running = False
    
    def print_header(self):
        """Print the application header"""
        print("\n" + "="*60)
        print(" Real-Time Tournament Leaderboard System")
        print("="*60 + "\n")
    
    def print_menu(self):
        """Print the main menu"""
        print("\nMain Menu:")
        print("  1. Add a player")
        print("  2. Submit score update")
        print("  3. Process next update")
        print("  4. Process all updates")
        print("  5. View leaderboard")
        print("  6. View top N players")
        print("  7. Get player rank")
        print("  8. Get player info")
        print("  9. Remove player")
        print(" 10. View system stats")
        print(" 11. Run tournament simulation")
        print(" 12. Clear all data")
        print("  0. Exit")
        print()
    
    def display_leaderboard(self, players, title="Current Leaderboard"):
        """
        Display leaderboard in a formatted table.
        
        Args:
            players (list[Player]): List of players to display
            title (str): Title for the leaderboard display
        """
        print("\n" + "="*60)
        print(f" {title}")
        print("="*60)
        
        if not players:
            print("  (No players in leaderboard)")
        else:
            print(f"{'Rank':<6} {'Username':<20} {'Player ID':<15} {'Score':<10}")
            print("-"*60)
            for rank, player in enumerate(players, 1):
                print(f"{rank:<6} {player.username:<20} {player.player_id:<15} {player.score:<10}")
        
        print("="*60 + "\n")
    
    def add_player(self):
        """Handle adding a new player"""
        print("\n--- Add New Player ---")
        player_id = input("Enter player ID: ").strip()
        username = input("Enter username: ").strip()
        score_input = input("Enter initial score (default 0): ").strip()
        
        score = int(score_input) if score_input else 0
        
        self.system.add_player(player_id, username, score)
        print(f"✓ Added player: {username} (ID: {player_id}) with score {score}")
    
    def submit_update(self):
        """Handle submitting a score update"""
        print("\n--- Submit Score Update ---")
        player_id = input("Enter player ID: ").strip()
        new_score = int(input("Enter new score: ").strip())
        
        # Check if player exists, if not ask for username
        if player_id not in self.system.player_lookup:
            username = input("Player not found. Enter username for new player: ").strip()
            self.system.submit_score_update(player_id, new_score, username)
        else:
            self.system.submit_score_update(player_id, new_score)
        
        print(f"✓ Update submitted for player {player_id}")
    
    def process_next(self):
        """Process the next update"""
        print("\n--- Processing Next Update ---")
        success = self.system.process_next_update()
        
        if success:
            print("✓ Processed 1 update")
        else:
            print("No pending updates to process")
    
    def process_all(self):
        """Process all pending updates"""
        print("\n--- Processing All Updates ---")
        count = self.system.process_all_updates()
        print(f"✓ Processed {count} updates")
    
    def view_leaderboard(self):
        """Display the full leaderboard"""
        players = self.system.get_leaderboard()
        self.display_leaderboard(players)
    
    def view_top_n(self):
        """Display top N players"""
        n = int(input("How many top players to display? "))
        players = self.system.get_leaderboard(top_n=n)
        self.display_leaderboard(players, f"Top {n} Players")
    
    def get_player_rank(self):
        """Get and display a player's rank"""
        player_id = input("Enter player ID: ").strip()
        rank = self.system.get_player_rank(player_id)
        
        if rank == -1:
            print(f"Player {player_id} not found")
        else:
            print(f"Player {player_id} is rank #{rank}")
    
    def get_player_info(self):
        """Display complete player information"""
        player_id = input("Enter player ID: ").strip()
        info = self.system.get_player_info(player_id)
        
        if info is None:
            print(f"Player {player_id} not found")
        else:
            print("\nPlayer Information:")
            print(f"  Username: {info['username']}")
            print(f"  Player ID: {info['player_id']}")
            print(f"  Score: {info['score']}")
            print(f"  Rank: #{info['rank']}")
    
    def remove_player(self):
        """Remove a player from the leaderboard"""
        player_id = input("Enter player ID to remove: ").strip()
        success = self.system.remove_player(player_id)
        
        if success:
            print(f"✓ Removed player {player_id}")
        else:
            print(f"Player {player_id} not found")
    
    def view_stats(self):
        """Display system statistics"""
        stats = self.system.get_stats()
        
        print("\nSystem Statistics:")
        print(f"  Total players: {stats['total_players']}")
        print(f"  Pending updates: {stats['pending_updates']}")
        print(f"  Total updates processed: {stats['total_updates_processed']}")
    
    def simulate_tournament(self):
        """Run a tournament simulation"""
        print("\n--- Tournament Simulation ---")
        num_players = int(input("Number of players: "))
        num_rounds = int(input("Number of rounds: "))
        
        print(f"\nSimulating tournament with {num_players} players, {num_rounds} rounds...")
        
        # TODO: Implement simulation
        # - Generate random players
        # - Each round, random players get score updates
        # - Show leaderboard after each round
        # - Add delays for visual effect
        
        print("Simulation complete!")
    
    def clear_data(self):
        """Clear all leaderboard data"""
        confirm = input("Are you sure you want to clear all data? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            self.system.clear()
            print("✓ All data cleared")
        else:
            print("Cancelled")
    
    def run(self):
        """Main loop for the CLI"""
        self.running = True
        self.print_header()
        
        while self.running:
            self.print_menu()
            choice = input("Enter choice: ").strip()
            
            try:
                if choice == '1':
                    self.add_player()
                elif choice == '2':
                    self.submit_update()
                elif choice == '3':
                    self.process_next()
                elif choice == '4':
                    self.process_all()
                elif choice == '5':
                    self.view_leaderboard()
                elif choice == '6':
                    self.view_top_n()
                elif choice == '7':
                    self.get_player_rank()
                elif choice == '8':
                    self.get_player_info()
                elif choice == '9':
                    self.remove_player()
                elif choice == '10':
                    self.view_stats()
                elif choice == '11':
                    self.simulate_tournament()
                elif choice == '12':
                    self.clear_data()
                elif choice == '0':
                    print("\nExiting... Goodbye!")
                    self.running = False
                else:
                    print("Invalid choice. Please try again.")
            
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again.\n")


def demo_scenario():
    """
    Run a pre-programmed demo scenario for presentations.
    This shows off all the features without manual input.
    """
    print("\n" + "="*60)
    print(" AUTOMATED DEMO - Real-Time Leaderboard System")
    print("="*60 + "\n")
    
    system = LeaderboardSystem()
    
    # Step 1: Add initial players
    print("Step 1: Adding initial players...")
    players_data = [
        ("player1", "Alice", 1000),
        ("player2", "Bob", 1500),
        ("player3", "Charlie", 800),
        ("player4", "Diana", 1200),
        ("player5", "Eve", 1100),
    ]
    
    for pid, name, score in players_data:
        system.add_player(pid, name, score)
        print(f"  Added {name} with score {score}")
    
    time.sleep(1)
    
    # Step 2: Show initial leaderboard
    print("\nStep 2: Initial leaderboard:")
    cli = LeaderboardCLI()
    cli.system = system
    cli.display_leaderboard(system.get_leaderboard())
    
    time.sleep(2)
    
    # Step 3: Submit some score updates
    print("Step 3: Submitting score updates...")
    updates = [
        ("player1", 1800),  # Alice gets a big boost
        ("player3", 1600),  # Charlie improves
        ("player5", 900),   # Eve drops
    ]
    
    for pid, score in updates:
        system.submit_score_update(pid, score)
        print(f"  Submitted update: {pid} -> {score}")
    
    time.sleep(1)
    
    # Step 4: Show pending updates
    stats = system.get_stats()
    print(f"\nStep 4: Pending updates: {stats['pending_updates']}")
    
    time.sleep(1)
    
    # Step 5: Process updates
    print("\nStep 5: Processing all updates...")
    processed = system.process_all_updates()
    print(f"  Processed {processed} updates")
    
    time.sleep(1)
    
    # Step 6: Show updated leaderboard
    print("\nStep 6: Updated leaderboard:")
    cli.display_leaderboard(system.get_leaderboard())
    
    time.sleep(2)
    
    # Step 7: Show top 3
    print("Step 7: Top 3 players:")
    cli.display_leaderboard(system.get_leaderboard(top_n=3), "Top 3")
    
    time.sleep(1)
    
    print("\n" + "="*60)
    print(" Demo Complete!")
    print("="*60 + "\n")


if __name__ == "__main__":
    # Uncomment one of these:
    
    # Interactive mode
    cli = LeaderboardCLI()
    cli.run()
    
    # Or run the automated demo
    # demo_scenario()
