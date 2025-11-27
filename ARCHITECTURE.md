# System Architecture Diagram

## High-Level Component View

```
┌─────────────────────────────────────────────────────────────────┐
│                     Leaderboard System                          │
│                  (leaderboard_system.py)                        │
│                                                                 │
│  ┌──────────────┐        ┌──────────────┐                     │
│  │ Priority     │        │   Binary     │                     │
│  │ Queue        │───────▶│   Search     │                     │
│  │              │dequeue │   Tree       │                     │
│  │ (Updates)    │        │ (Rankings)   │                     │
│  └──────────────┘        └──────────────┘                     │
│         ▲                        │                             │
│         │enqueue                 │query                        │
│         │                        ▼                             │
│  ┌──────────────────────────────────────┐                     │
│  │     player_lookup (Hash Map)         │                     │
│  │   player_id → BSTNode reference      │                     │
│  └──────────────────────────────────────┘                     │
└─────────────────────────────────────────────────────────────────┘
         ▲                                   │
         │                                   │
         │ submit_update()          get_leaderboard()
         │                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                      CLI / User Interface                        │
│                         (cli.py)                                │
└─────────────────────────────────────────────────────────────────┘
```

## Data Flow - Score Update

```
1. User Input
   "Update player p1 to score 2000"
          │
          ▼
2. Submit to Queue
   LeaderboardSystem.submit_score_update("p1", 2000)
          │
          ▼
3. Create UpdateRequest
   UpdateRequest(player_id="p1", new_score=2000, priority=timestamp)
          │
          ▼
4. Enqueue (O(log m))
   PriorityQueue.enqueue(request)
   [Heap: maintains priority order]
          │
          ▼
5. Process Update
   LeaderboardSystem.process_next_update()
          │
          ▼
6. Dequeue (O(log m))
   request = PriorityQueue.dequeue()
          │
          ▼
7. Lookup Player (O(1))
   old_node = player_lookup["p1"]
          │
          ▼
8. Delete from BST (O(log n))
   BST.delete("p1")  [removes old score]
          │
          ▼
9. Insert into BST (O(log n))
   new_node = BST.insert(updated_player)
          │
          ▼
10. Update Hash Map (O(1))
    player_lookup["p1"] = new_node
          │
          ▼
11. Done! Leaderboard updated
```

## Class Relationships

```
Player
  │
  ├──▶ BSTNode
  │      │
  │      └──▶ BinarySearchTree
  │              │
  │              └──▶ LeaderboardSystem
  │                      │
  └──▶ UpdateRequest     │
           │              │
           └──▶ PriorityQueue
                   │
                   └──▶ LeaderboardSystem
```

## BST Structure Example

```
After inserting players with scores: 2000, 1500, 1800, 1000, 1200

                 Bob(2000)
                /         \
           Alice(1500)   Charlie(1800)
           /         \
       Eve(1000)   Diana(1200)

In-order traversal gives ranked list:
1. Bob (2000)
2. Charlie (1800)  
3. Alice (1500)
4. Diana (1200)
5. Eve (1000)
```

## Priority Queue Structure Example

```
After enqueueing 5 update requests with timestamps:

Array representation (min-heap by timestamp):
[Update(t=1), Update(t=3), Update(t=2), Update(t=7), Update(t=5)]

Tree visualization:
           Update(t=1)
          /           \
     Update(t=3)    Update(t=2)
     /         \
Update(t=7)  Update(t=5)

Dequeue order: t=1, t=2, t=3, t=5, t=7 (FIFO by timestamp)
```

## Team Responsibilities Map

```
┌─────────────────────┐
│   player.py         │  ← Everyone uses this
│   (Player class)    │
└─────────────────────┘

┌─────────────────────┐
│   bst.py            │  ← Rider Gordon
│   - BSTNode         │     - Insert/Delete
│   - BST             │     - Traversal
│   - Optional: AVL   │     - Rank queries
└─────────────────────┘

┌─────────────────────┐
│  priority_queue.py  │  ← Chase Barman
│  - UpdateRequest    │     - Enqueue/Dequeue
│  - PriorityQueue    │     - Heapify
│                     │     - Heap operations
└─────────────────────┘

┌─────────────────────┐
│ leaderboard_sys.py  │  ← Srinivas Krishnan
│ - Integration       │     - Connect BST + PQ
│ - Hash map          │     - Process updates
│ - Queries           │     - All query methods
└─────────────────────┘

┌─────────────────────┐
│   cli.py            │  ← Srinivas (with all)
│   - User interface  │     - Demo
│   - Simulation      │     - Testing
└─────────────────────┘

┌─────────────────────┐
│ test_leaderboard.py │  ← All team members
│   - Unit tests      │     - Each tests their part
│   - Integration     │     - Work together
└─────────────────────┘
```

## Complexity Summary Table

```
┌──────────────────────────┬──────────────────┬──────────────────┐
│ Operation                │ Time Complexity  │ Who Implements   │
├──────────────────────────┼──────────────────┼──────────────────┤
│ BST Insert               │ O(log n) avg     │ Rider            │
│ BST Delete               │ O(log n) avg     │ Rider            │
│ BST Search by ID         │ O(n) worst       │ Rider            │
│ BST In-order Traversal   │ O(n)             │ Rider            │
│ BST Get Rank (basic)     │ O(n)             │ Rider            │
│ BST Get Rank (advanced)  │ O(log n)         │ Rider (optional) │
├──────────────────────────┼──────────────────┼──────────────────┤
│ PQ Enqueue               │ O(log m)         │ Chase            │
│ PQ Dequeue               │ O(log m)         │ Chase            │
│ PQ Peek                  │ O(1)             │ Chase            │
│ PQ Heapify               │ O(m)             │ Chase            │
├──────────────────────────┼──────────────────┼──────────────────┤
│ Hash Map Lookup          │ O(1)             │ Srinivas         │
│ Submit Update            │ O(log m)         │ Srinivas         │
│ Process Update           │ O(log n + log m) │ Srinivas         │
│ Get Leaderboard (all)    │ O(n)             │ Srinivas         │
│ Get Top K                │ O(K)             │ Srinivas         │
│ Get Player Rank          │ O(n)             │ Srinivas         │
└──────────────────────────┴──────────────────┴──────────────────┘

where:
  n = number of players in BST
  m = number of updates in priority queue
```

## Implementation Timeline

```
Week 1: Foundation
┌────────────┬────────────┬────────────┐
│   Rider    │   Chase    │  Srinivas  │
├────────────┼────────────┼────────────┤
│ BST Insert │ PQ Enqueue │ Player     │
│ BST Delete │ PQ Dequeue │ Test data  │
│ Traversal  │ Bubble ops │ Interfaces │
└────────────┴────────────┴────────────┘

Week 2: Integration
┌────────────┬────────────┬────────────┐
│   Rider    │   Chase    │  Srinivas  │
├────────────┼────────────┼────────────┤
│ Get Rank   │ Heapify    │ Process    │
│ Unit tests │ Unit tests │ Queries    │
│ BST docs   │ PQ docs    │ CLI basic  │
└────────────┴────────────┴────────────┘

Week 3: Polish
┌────────────────────────────────────┐
│         All Team Members           │
├────────────────────────────────────┤
│ Integration testing                │
│ Performance benchmarks             │
│ Demo preparation                   │
│ Presentation slides                │
│ Final report                       │
└────────────────────────────────────┘
```

## Key Design Decisions

```
┌──────────────────────────────────────────────────────────┐
│ Why use both BST and Priority Queue?                     │
├──────────────────────────────────────────────────────────┤
│ BST:  Maintains rankings, fast queries                   │
│ PQ:   Buffers updates, handles bursts gracefully         │
│ Both: Separates "storage" from "processing"              │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Why add a Hash Map?                                      │
├──────────────────────────────────────────────────────────┤
│ Problem: BST search by player_id is O(n)                 │
│ Solution: Hash map gives O(1) lookup                     │
│ Trade-off: Extra O(n) space for O(n) → O(1) improvement  │
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ Why sort players by (score, player_id)?                  │
├──────────────────────────────────────────────────────────┤
│ Primary: Score (high to low) for ranking                 │
│ Secondary: Player ID for deterministic tie-breaking      │
│ Result: Every player has unique position in tree         │
└──────────────────────────────────────────────────────────┘
```
