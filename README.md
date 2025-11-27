# Real-Time Multiplayer Leaderboard System

**Team Members:** Rider Gordon, Chase Barman, and Srinivas Krishnan  
**Course:** CSCI 046 - Data Structures  
**Repository:** https://github.com/skrishnan28-sys/Final-Project

## Project Overview

This project implements a real-time tournament leaderboard system that efficiently manages and updates player rankings during competitive gameplay. The system uses custom-built data structures (Binary Search Tree and Priority Queue) to handle concurrent score updates while maintaining optimal query performance.

## Core Components

### 1. Player (`player.py`)
- Represents individual players with ID, username, score, and timestamp
- Implements comparison operators for BST ordering (high score = higher rank)

### 2. Binary Search Tree (`bst.py`) - Rider Gordon
- Custom BST implementation for storing players by score
- Supports O(log n) insertion, deletion, and search operations
- In-order traversal provides ranked player list
- Optional: Self-balancing AVL tree implementation

### 3. Priority Queue (`priority_queue.py`) - Chase Barman
- Min-heap based priority queue for managing update requests
- Custom implementation without using Python's heapq
- Handles concurrent updates in priority order
- Heapify operation for batch request processing

### 4. Leaderboard System (`leaderboard_system.py`) - Srinivas Krishnan
- Integration layer coordinating BST and Priority Queue
- Hash map for O(1) player lookups by ID
- Processes updates: dequeue from priority queue → update BST
- Provides leaderboard queries (top N, player rank, etc.)

### 5. Command-Line Interface (`cli.py`) - Demo & Testing
- Interactive CLI for testing and demonstration
- Automated demo scenario for presentations
- Real-time leaderboard visualization

## File Structure

```
Final-Project/
├── player.py                 # Player class definition
├── bst.py                    # Binary Search Tree implementation
├── priority_queue.py         # Priority Queue implementation
├── leaderboard_system.py     # Main integration layer
├── cli.py                    # Command-line interface
├── test_leaderboard.py       # Unit tests
└── README.md                 # This file
```

## Installation & Setup

No external dependencies required - uses only Python standard library.

```bash
# Clone the repository
git clone https://github.com/skrishnan28-sys/Final-Project.git
cd Final-Project

# Run the CLI
python cli.py

# Run tests
python -m unittest test_leaderboard.py
```

## Usage Examples

### Basic Usage

```python
from leaderboard_system import LeaderboardSystem

# Create leaderboard
system = LeaderboardSystem()

# Add players
system.add_player("p1", "Alice", 1000)
system.add_player("p2", "Bob", 1500)

# Submit score update
system.submit_score_update("p1", 2000)

# Process updates
system.process_all_updates()

# Get leaderboard
top_players = system.get_leaderboard(top_n=10)

# Get player rank
rank = system.get_player_rank("p1")
```

### Running the CLI

```bash
python cli.py
```

The CLI provides:
- Add/remove players
- Submit and process score updates
- View leaderboard (full or top N)
- Query player rank and info
- Tournament simulation
- System statistics

## Implementation Status

### ✅ Completed
- [x] Player class with comparison operators
- [x] BST class structure with all method signatures
- [x] Priority Queue class structure
- [x] Leaderboard System integration layer
- [x] CLI interface framework
- [x] Test file template

### 🚧 To Implement (Your Tasks)

#### Rider Gordon - BST Implementation
- [ ] Implement `_insert_recursive()`
- [ ] Implement `_delete_recursive()` and helper methods
- [ ] Implement `_search_recursive()`
- [ ] Implement `_inorder_recursive()`
- [ ] Implement `get_rank()` (basic O(n) or advanced O(log n))
- [ ] Write unit tests for BST
- [ ] Optional: AVL tree balancing

#### Chase Barman - Priority Queue Implementation
- [ ] Implement `enqueue()` and `_bubble_up()`
- [ ] Implement `dequeue()` and `_bubble_down()`
- [ ] Implement `heapify()`
- [ ] Write unit tests for priority queue
- [ ] Optional: Request merging for duplicate player updates

#### Srinivas Krishnan - Integration & Testing
- [ ] Implement `process_next_update()`
- [ ] Implement `process_all_updates()`
- [ ] Implement all query methods (get_leaderboard, get_rank, etc.)
- [ ] Implement tournament simulation
- [ ] Write integration tests
- [ ] Prepare presentation slides
- [ ] Write final report

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Insert player into BST | O(log n) avg, O(n) worst | O(1) |
| Delete player from BST | O(log n) avg, O(n) worst | O(1) |
| Enqueue update | O(log m) | O(1) |
| Dequeue update | O(log m) | O(1) |
| Get top K players | O(K) | O(K) |
| Get player rank | O(n) basic, O(log n) with augmentation | O(1) |
| Update player score | O(log n + log m) | O(1) |

*where n = number of players, m = number of pending updates*

## Testing Strategy

### Unit Tests
Each team member writes tests for their component:
- **BST Tests**: insertion, deletion, traversal, edge cases
- **Priority Queue Tests**: enqueue/dequeue order, heapify, empty queue
- **Integration Tests**: end-to-end update flow, leaderboard queries

### Performance Tests
- Measure insertion/deletion times for various tree sizes
- Verify O(log n) complexity empirically
- Stress test with 1000+ players and 10000+ updates

### Demo Scenarios
- Interactive CLI demonstration
- Automated demo with realistic tournament simulation
- Show real-time updates and leaderboard changes

## Design Decisions

### Why BST?
- O(log n) insertion/deletion for efficient updates
- In-order traversal naturally produces ranked list
- Flexible for future enhancements (range queries, etc.)

### Why Priority Queue?
- Handles bursts of concurrent updates systematically
- Allows prioritization of important updates
- Decouples update arrival from BST modification

### Why Hash Map?
- O(1) player lookup by ID (BST search by ID would be O(n))
- Essential for efficient score updates (find old node quickly)

## Future Enhancements

- [ ] Self-balancing BST (AVL or Red-Black tree) for guaranteed O(log n)
- [ ] Augmented BST nodes for O(log n) rank queries
- [ ] Request merging to avoid duplicate updates for same player
- [ ] Web-based visualization using Flask/JavaScript
- [ ] Persistence (save/load leaderboard from file)
- [ ] Multi-threaded update processing

## Team Responsibilities

### Rider Gordon
- BST implementation and balancing logic
- Unit tests for BST operations
- Presentation section: Data structure theory

### Chase Barman
- Priority Queue implementation
- Heap operations and stress testing
- Presentation section: Queue dynamics

### Srinivas Krishnan
- System integration and coordination
- CLI and demo development
- Final report and presentation lead
- GitHub repository management

## Presentation Outline

1. **Problem Statement** (2 min)
   - Why real-time leaderboards are challenging
   - Current solutions and limitations

2. **Our Solution** (3 min)
   - BST + Priority Queue architecture
   - Data flow diagram

3. **BST Implementation** (3 min) - Rider
   - How BST stores players
   - Insertion/deletion operations
   - Balancing considerations

4. **Priority Queue** (3 min) - Chase
   - Heap operations
   - Update request management
   - Concurrency handling

5. **Integration & Demo** (4 min) - Srinivas
   - How components work together
   - Live demonstration
   - Complexity analysis

6. **Q&A** (2 min)

## Resources & Citations

- [Binary Search Trees - CLRS Chapter 12](https://mitpress.mit.edu/9780262046305/)
- [Heaps and Priority Queues - CLRS Chapter 6](https://mitpress.mit.edu/9780262046305/)
- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)

## Contact

- Rider Gordon: [email]
- Chase Barman: [email]
- Srinivas Krishnan: [email]

## License

This project is for educational purposes as part of CSCI 046.
