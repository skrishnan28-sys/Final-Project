"""
Leaderboard System Demo Class
Demonstrates all features of the leaderboard system
"""
from leaderboard_system import LeaderboardSystem


class LeaderboardDemo:
    """
    Demo class for showcasing the leaderboard system.

    Features demonstrated:
    - Basic score submission and processing
    - Real-time updates
    - Leaderboard display
    - Player information lookup
    - Batch processing
    - Incremental processing
    """

    def __init__(self):
        """Initialize demo with a new leaderboard system"""
        self.system = LeaderboardSystem()

    def run_basic_demo(self):
        """
        Demonstrate basic leaderboard functionality.
        Shows: score submission, processing, and display.
        """
        print("\n-----------------------------------------------")
        print("DEMO 1: BASIC LEADERBOARD FUNCTIONALITY")
        print("\n-----------------------------------------------")

        print("\n--- Phase 1: Initial Score Submissions ---")

        # Players submit their scores
        self.system.submit_score("p001", "Allen", 1500)
        self.system.submit_score("p002", "Burrow", 2000)
        self.system.submit_score("p003", "Jackson", 1800)
        self.system.submit_score("p004", "Mahomes", 1200)
        self.system.submit_score("p005", "Rogers", 2200)

        # Process all updates
        self.system.process_updates()

        # Display leaderboard
        self.system.display_leaderboard()

        # Display stats
        self.system.display_stats()

        print("\n--- Phase 2: Score Updates ---")

        # Some players improve their scores
        self.system.submit_score("p001", "Allen", 2500)  # Allen improves!
        self.system.submit_score("p003", "Jackson", 1900)  # Jackson improves
        self.system.submit_score("p006", "Frank", 1700)  # New player

        # Process updates
        self.system.process_updates()

        # Display updated leaderboard
        self.system.display_leaderboard()

        print("\n--- Phase 3: Player Information ---")

        # Look up specific player
        self.system.display_player_info("p001")

        # Get rank for a player
        rank = self.system.get_player_rank("p002")
        print(f"\nBurrow's current rank: #{rank}")

        print("\n--- Phase 4: Top 3 Players ---")

        # Display only top 3
        self.system.display_leaderboard(top_n=3)

        # Final stats
        self.system.display_stats()

    def run_batch_processing_demo(self):
        """
        Demonstrate batch processing of updates.
        Shows: queuing multiple updates and processing them together.
        """
        print("\n-----------------------------------------------")
        print("DEMO 2: BATCH PROCESSING")
        print("\n-----------------------------------------------")

        # Create a fresh system for this demo
        self.system = LeaderboardSystem()

        print("\n--- Receiving Multiple Updates ---")

        # Simulate receiving many updates at once
        self.system.submit_score("p1", "Player1", 1000)
        self.system.submit_score("p2", "Player2", 1500)
        self.system.submit_score("p3", "Player3", 1200)
        self.system.submit_score("p1", "Player1", 1100)  # Update for p1
        self.system.submit_score("p4", "Player4", 1800)
        self.system.submit_score("p2", "Player2", 1600)  # Update for p2
        self.system.submit_score("p5", "Player5", 2000)

        print(f"\n{self.system.update_queue.get_size()} updates queued")

        print("\n--- Processing All Updates in FIFO Order ---")
        self.system.process_updates()

        self.system.display_leaderboard()

        print("\n--- Observation ---")
        print("Notice how Player1 and Player2 were updated to their latest scores.")
        print("The FIFO queue ensured updates were processed in the order received.")


    def run_tournament_simulation(self):
        """
        Simulate a tournament with multiple rounds.
        Shows: realistic tournament scenario with progressive scoring.
        """
        print("\n-----------------------------------------------")
        print("DEMO 4: TOURNAMENT SIMULATION")
        print("\n-----------------------------------------------")

        # Create a fresh system for this demo
        self.system = LeaderboardSystem()

        # Tournament players
        players = [
            ("p1", "Allen"),
            ("p2", "Burrow"),
            ("p3", "Jackson"),
            ("p4", "Mahomes"),
            ("p5", "Rogers"),
        ]

        # Round 1
        print("\n=== ROUND 1 ===")
        print("Players complete first round...")
        for player_id, username in players:
            import random
            score = random.randint(500, 1000)
            self.system.submit_score(player_id, username, score)

        self.system.process_updates()
        self.system.display_leaderboard()

        # Round 2
        print("\n=== ROUND 2 ===")
        print("Players complete second round (scores accumulate)...")
        for player_id, username in players:
            import random
            current_player = self.system.get_player(player_id)
            new_score = current_player.score + random.randint(300, 700)
            self.system.submit_score(player_id, username, new_score)

        self.system.process_updates()
        self.system.display_leaderboard()

        # Round 3 (Final)
        print("\n=== ROUND 3 (FINAL) ===")
        print("Players complete final round...")
        for player_id, username in players:
            import random
            current_player = self.system.get_player(player_id)
            new_score = current_player.score + random.randint(200, 500)
            self.system.submit_score(player_id, username, new_score)

        self.system.process_updates()

        print("\n=== FINAL RESULTS ===")
        self.system.display_leaderboard()

        # Show winner details
        leaderboard = self.system.get_leaderboard(top_n=1)
        if leaderboard:
            winner = leaderboard[0]
            print(f"\n*** WINNER: {winner.username} with {winner.score} points! ***")

        self.system.display_stats()

    def run_stress_test(self):
        """
        Stress test with many players.
        Shows: system performance with larger datasets.
        """
        print("\n-----------------------------------------------")
        print("DEMO 5: STRESS TEST (100 PLAYERS)")
        print("\n-----------------------------------------------")

        # Create a fresh system for this demo
        self.system = LeaderboardSystem()

        import time
        import random

        num_players = 100

        print(f"\n--- Submitting scores for {num_players} players ---")
        start_time = time.time()

        for i in range(num_players):
            player_id = f"p{i:03d}"
            username = f"Player{i:03d}"
            score = random.randint(1000, 10000)
            self.system.submit_score(player_id, username, score)

        submit_time = time.time() - start_time
        print(f"Submitted {num_players} scores in {submit_time * 1000:.2f} ms")

        print(f"\n--- Processing {num_players} updates ---")
        start_time = time.time()

        self.system.process_updates()

        process_time = time.time() - start_time
        print(f"Processed {num_players} updates in {process_time * 1000:.2f} ms")

        print(f"\n--- Displaying Top 10 ---")
        self.system.display_leaderboard(top_n=10)

        # Performance summary
        print("\n--- Performance Summary ---")
        print(f"  Total players: {num_players}")
        print(f"  Submit time: {submit_time * 1000:.2f} ms ({submit_time * 1000 / num_players:.3f} ms per player)")
        print(f"  Process time: {process_time * 1000:.2f} ms ({process_time * 1000 / num_players:.3f} ms per update)")
        print(f"  Total time: {(submit_time + process_time) * 1000:.2f} ms")

        self.system.display_stats()

    def run_player_operations_demo(self):
        """
        Demonstrate various player operations.
        Shows: lookup, rank queries, and player removal.
        """
        print("\n-----------------------------------------------")
        print("DEMO 6: PLAYER OPERATIONS")
        print("\n-----------------------------------------------")

        # Create a fresh system for this demo
        self.system = LeaderboardSystem()

        # Add some players
        print("\n--- Adding Players ---")
        self.system.submit_score("p1", "Allen", 2000)
        self.system.submit_score("p2", "Burrow", 1500)
        self.system.submit_score("p3", "Jackson", 2500)
        self.system.submit_score("p4", "Mahomes", 1800)
        self.system.submit_score("p5", "Rogers", 2200)
        self.system.process_updates()

        self.system.display_leaderboard()

        # Player lookup
        print("\n--- Player Lookup (O(1) via hash map) ---")
        player = self.system.get_player("p3")
        if player:
            print(f"Found: {player.username} with score {player.score}")

        # Rank query
        print("\n--- Rank Query ---")
        for player_id in ["p1", "p2", "p3", "p4", "p5"]:
            rank = self.system.get_player_rank(player_id)
            player = self.system.get_player(player_id)
            print(f"  {player.username}: Rank #{rank}")

        # Remove a player
        print("\n--- Removing Player ---")
        self.system.remove_player("p2")

        print("\n--- Updated Leaderboard ---")
        self.system.display_leaderboard()

        # Try to find removed player
        print("\n--- Trying to Find Removed Player ---")
        player = self.system.get_player("p2")
        if player is None:
            print("Player p2 (Burrow) not found - successfully removed!")

    def run_all_demos(self):
        """Run all demonstration scenarios"""
        print("\n-----------------------------------------------")
        print(" REAL-TIME MULTIPLAYER LEADERBOARD SYSTEM ")
        print(" COMPLETE DEMONSTRATION ")
        print("\n-----------------------------------------------")

        # Run all demos in sequence
        self.run_basic_demo()

        input("\n\nPress Enter to continue to Batch Processing Demo...")
        self.run_batch_processing_demo()

        input("\n\nPress Enter to continue to Tournament Simulation...")
        self.run_tournament_simulation()

        input("\n\nPress Enter to continue to Stress Test...")
        self.run_stress_test()

        input("\n\nPress Enter to continue to Player Operations Demo...")
        self.run_player_operations_demo()

        print("\n-----------------------------------------------")
        print(" ALL DEMOS COMPLETE! ".center(70, "="))
        print("\n-----------------------------------------------")


# ============================================================================
# MAIN EXECUTION - Run individual demos or all at once
# ============================================================================

if __name__ == "__main__":
    demo = LeaderboardDemo()

    # Option 1: Run all demos interactively
    demo.run_all_demos()
    """
    # Option 2: Run individual demos
    demo.run_basic_demo()

    print("\n\n")
    demo.run_batch_processing_demo()

    print("\n\n")
    demo.run_tournament_simulation()

    print("\n\n")
    demo.run_stress_test()

    print("\n\n")
    demo.run_player_operations_demo()
    """
    print("\n-----------------------------------------------")
    print(" ALL DEMOS COMPLETE! ")
    print("\n-----------------------------------------------")