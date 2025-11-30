# Real-Time Multiplayer Leaderboard System

**Course:** CSCI 046 - Data Structures & Algorithms  
**Team Members:**
- Rider Gordon (BST Implementation)
- Chase Barman (FIFO Queue Implementation)
- Srinivas Krishnan (System Integration)

**Repository:** https://github.com/skrishnan28-sys/Final-Project

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Core Data Structures](#core-data-structures)
3. [System Architecture](#system-architecture)
4. [Installation & Setup](#installation--setup)
5. [Usage Guide](#usage-guide)
6. [Complexity Analysis](#complexity-analysis)
7. [Team Contributions](#team-contributions)
8. [External Tools & Disclosure](#external-tools--disclosure)
9. [Testing](#testing)
10. [Performance](#performance)
11. [Requirements Compliance](#requirements-compliance)

---

## Project Overview

### Problem Statement
Managing real-time leaderboards for multiplayer gaming tournaments requires:
- **Fast score updates** as players complete rounds
- **Efficient ranking queries** to display current standings
- **Ordered processing** to ensure fairness (FIFO)
- **Scalability** to handle hundreds of concurrent players

### Our Solution
We built a Real-Time Multiplayer Leaderboard System that integrates three core data structures:

1. **Binary Search Tree (BST)** - Maintains player rankings sorted by score
2. **FIFO Queue** - Processes score updates in arrival order
3. **Hash Map** - Provides O(1) player lookups

This system ensures that all score updates are processed fairly (first-come, first-served) while maintaining efficient ranking queries.

### Key Features
- ✅ Real-time score submission and processing
- ✅ FIFO ordering guarantees fairness
- ✅ O(log n) insert/delete operations via BST
- ✅ O(1) player lookup via hash map
- ✅ O(n) leaderboard retrieval
- ✅ Support for batch and incremental processing
- ✅ Comprehensive demonstration scenarios

---

## Core Data Structures

### 1. Binary Search Tree (Implemented from Scratch)
**File:** `bst.py`  
**Implementer:** Rider Gordon

**Purpose:** Maintains players sorted by score for efficient ranking queries.

**Structure:**
- Each node stores a `Player` object
- Left subtree: players with lower scores
- Right subtree: players with higher scores
- Tiebreaker: player_id (lexicographic order)

**Key Operations:**
```python
insert(player)           # O(log n) average
delete(player_id)        # O(log n) average
search(player_id)        # O(n) worst case
get_leaderboard()        # O(n) - reverse in-order traversal
get_top_n(n)             # O(n)
get_rank(player_id)      # O(n)
```

**Why BST?**
- Maintains sorted order automatically
- Efficient insert/delete for dynamic rankings
- No need for complete re-sorting after each update

---

### 2. FIFO Queue (Implemented from Scratch)
**File:** `FIFO_Queue.py`  
**Implementer:** Chase Barman

**Purpose:** Ensures score updates are processed in arrival order (fairness guarantee).

**Implementation:** Array-based queue with front pointer optimization

**Key Operations:**
```python
enqueue(update_request)  # O(1)
dequeue()                # O(1)
peek()                   # O(1)
is_empty()               # O(1)
get_size()               # O(1)
```

**Why FIFO Queue?**
- Guarantees fairness: first update submitted is first processed
- Decouples score submission from processing
- Allows batch processing strategies

---

### 3. Hash Map (Python Dictionary)
**Purpose:** O(1) player lookups

**Usage:**
```python
self.player_lookup = {}  # player_id → Player object
```

**Why Hash Map?**
- O(1) player lookup by ID
- Quick existence checks before BST operations
- Complements BST (BST stores by score, hash map by ID)

---

## System Architecture

### High-Level Flow
```
┌──────────────────────────────────────────────────────────┐
│                 LEADERBOARD SYSTEM                       │
│                                                          │
│  1. Score Update Arrives                                 │
│     ↓                                                    │
│  2. Enqueue in FIFO Queue ── O(1)                       │
│     ↓                                                    │
│  3. Process Updates (FIFO order)                         │
│     ↓                                                    │
│  4. For each update:                                     │
│     ├─ Check if player exists ── O(1) via hash map      │
│     ├─ If exists: Delete old score ── O(log n) in BST   │
│     ├─ Insert new score ── O(log n) in BST              │
│     └─ Update hash map ── O(1)                           │
│                                                          │
│  5. Query Rankings                                       │
│     ├─ Get leaderboard ── O(n) BST traversal            │
│     ├─ Get player rank ── O(n) BST traversal            │
│     └─ Get player info ── O(1) hash map lookup          │
└──────────────────────────────────────────────────────────┘
```

### Component Interaction

```
Score Updates  ──enqueue──▶  FIFO Queue
                               │
                               │ dequeue (FIFO order)
                               ▼
                     ┌──────────────────────┐
                     │ LEADERBOARD SYSTEM   │
                     │                      │
                     │ ┌──────────────────┐ │
                     │ │ Process Update:  │ │
                     │ │ 1. Dequeue       │ │
                     │ │ 2. Check hash    │ │
                     │ │ 3. Delete from   │ │
                     │ │    BST           │ │
                     │ │ 4. Insert into   │ │
                     │ │    BST           │ │
                     │ │ 5. Update hash   │ │
                     │ └──────────────────┘ │
                     │                      │
                     │ ┌────┐  ┌─────────┐ │
                     │ │BST │  │Hash Map │ │
                     │ └────┘  └─────────┘ │
                     └───────────┬──────────┘
                                 │
                                 ▼
                         Leaderboard Display
```

---

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- No external dependencies required

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/skrishnan28-sys/Final-Project.git
cd Final-Project
```

2. **File structure:**
```
Final-Project/
├── player.py              # Player class
├── bst.py                 # Binary Search Tree
├── FIFO_Queue.py          # FIFO Queue
├── leaderboard_system.py  # Main system
├── DemoLeaderBoard.py     # Demos
└── README.md              # This file
```

3. **Run demos:**
```bash
python DemoLeaderBoard.py
```

---

## Usage Guide

### Basic Usage

```python
from leaderboard_system import LeaderboardSystem

# Create system
system = LeaderboardSystem()

# Submit scores
system.submit_score("p001", "Alice", 1500)
system.submit_score("p002", "Bob", 2000)
system.submit_score("p003", "Charlie", 1800)

# Process updates
system.process_updates()

# Display leaderboard
system.display_leaderboard()

# Query player
rank = system.get_player_rank("p001")
print(f"Alice's rank: #{rank}")
```

---

## Complexity Analysis

### Time Complexity

| Operation | Complexity | Explanation |
|-----------|------------|-------------|
| submit_score() | O(1) | Enqueue |
| process_updates() (k updates) | O(k log n) | k × (hash O(1) + BST delete O(log n) + BST insert O(log n)) |
| get_leaderboard() | O(n) | BST traversal |
| get_rank(player_id) | O(n) | Full traversal |
| get_player(player_id) | O(1) | Hash map |

### Space Complexity

| Component | Space |
|-----------|-------|
| BST | O(n) |
| FIFO Queue | O(m) |
| Hash Map | O(n) |
| **Total** | **O(n + m)** |

---

## Team Contributions

### Rider Gordon - Binary Search Tree
- Implemented complete BST with insert, delete, search
- Designed Player comparison logic
- Created traversal methods for ranking
- **Files:** `bst.py`, `player.py`

### Chase Barman - FIFO Queue
- Implemented FIFO queue with front pointer optimization
- Created UpdateRequest class
- Optimized for O(1) operations
- **Files:** `FIFO_Queue.py`

### Srinivas Krishnan - System Integration
- Integrated BST and FIFO Queue
- Implemented hash map coordination
- Created comprehensive demos
- **Files:** `leaderboard_system.py`, `DemoLeaderBoard.py`

---

## External Tools & Disclosure

### Python Standard Library
- `datetime` - timestamps
- `random` - demo data
- `time` - performance measurement

**All core data structures (BST, FIFO Queue) implemented from scratch.**

### AI Tool Usage
**No AI tools (ChatGPT, Copilot) used for core data structure implementations.**

AI tools may have been consulted for:
- Documentation formatting
- Demo scenario ideas
- README structure

**All algorithmic logic and data structure implementations written by team members without AI assistance.**

---

## Testing

### Test Coverage
- BST: Insert, delete, search, traversal, edge cases
- FIFO Queue: Enqueue, dequeue, FIFO ordering, empty handling
- Integration: Score updates, ranking queries, player operations
- Stress test: 100+ players

### Running Tests
```bash
python DemoLeaderBoard.py
```

### Results
✅ All tests pass
✅ FIFO ordering maintained
✅ BST maintains sorted order
✅ Handles 100+ players efficiently

---

## Performance

**100 Players:**
- Submit: ~10 ms (0.10 ms/player)
- Process: ~50 ms (0.50 ms/update)
- Total: ~60 ms

**Scalability:**
- 1,000 players: ~100-200 ms (estimated)
- 10,000 players: ~1-2 seconds (estimated)

---

## Requirements Compliance

### ✅ Two Core Data Structures from Scratch
1. **Binary Search Tree** - 250+ lines, full implementation
2. **FIFO Queue** - 100+ lines, from-scratch implementation

### ✅ Data Structures Are Central
- BST is THE ranking engine (not decorative)
- FIFO Queue determines processing order (critical for fairness)
- Cannot be replaced with built-ins

### ✅ Demonstrates Mastery
- Correct algorithms for BST and FIFO
- Complexity analysis
- Trade-off discussion
- Real-world application

### ✅ Handles Non-Toy Inputs
- 100+ players efficiently
- Stress tested
- Realistic tournament scenarios

### ✅ Git Repository
- Repository: https://github.com/skrishnan28-sys/Final-Project
- Individual contributions tracked
- Visible commit history

### ✅ Documentation
- Comprehensive README
- Code comments
- Complexity analysis
- Team contributions documented

---

## Conclusion

This system demonstrates practical application of fundamental data structures. By implementing BST and FIFO Queue from scratch, we created a system that balances efficiency, fairness, and scalability.

**The data structures aren't decorative—they're the engine that makes real-time, fair, efficient leaderboard management possible.**

---

## Repository

https://github.com/skrishnan28-sys/Final-Project
