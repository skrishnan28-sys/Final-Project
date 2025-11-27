# Quick Start Guide

## Setup Checklist

### For All Team Members

1. **Clone the repository**
   ```bash
   git clone https://github.com/skrishnan28-sys/Final-Project.git
   cd Final-Project
   ```

2. **Understand the Player class**
   - Read `player.py` - this is the foundation everyone uses
   - Key: Players are compared by score (high to low), then ID (for ties)

3. **Read the interfaces**
   - Look at method signatures in your assigned file
   - Understand inputs/outputs for each method
   - Note which methods call which (dependencies)

### For Rider (BST Implementation)

**Your files:**
- Primary: `bst.py`
- Tests: `test_leaderboard.py` (TestBST class)

**Implementation order:**
1. Start with `_insert_recursive()` - easiest to understand
2. Then `_inorder_recursive()` - needed to verify insertions
3. Then `_search_recursive()` - useful for debugging
4. Then `_delete_recursive()` - most complex
5. Finally `get_rank()` - can be simple (O(n)) or advanced (O(log n))

**Key questions to answer:**
- How do you handle duplicate scores? (Use player_id as secondary sort)
- Will you balance the tree? (Start without, add AVL if time permits)
- How will you calculate rank? (Simple: traverse and count. Advanced: augment nodes)

**Testing approach:**
- Test insertion with 1, 3, 5, 10 players
- Test deletion in all 3 cases (leaf, one child, two children)
- Test edge cases: empty tree, all same scores, all different scores
- Draw trees on paper to understand structure!

### For Chase (Priority Queue Implementation)

**Your files:**
- Primary: `priority_queue.py`
- Tests: `test_leaderboard.py` (TestPriorityQueue class)

**Implementation order:**
1. Start with `_bubble_up()` - used by enqueue
2. Then `enqueue()` - test as you go
3. Then `_bubble_down()` - used by dequeue
4. Then `dequeue()` - test extensively
5. Finally `heapify()` - builds heap from list

**Key questions to answer:**
- Min-heap or max-heap? (Min-heap for timestamp-based priority)
- How to handle equal priorities? (FIFO - keep insertion order)
- Will you merge duplicate requests? (Optional advanced feature)

**Testing approach:**
- Test with 1, 3, 7, 15 requests (powers of 2 minus 1 fill a level)
- Verify heap property after every enqueue/dequeue
- Test dequeue on empty queue (should return None)
- Test with different priority values and verify order

**Heap refresher:**
- Parent of index i: `(i - 1) // 2`
- Left child of index i: `2 * i + 1`
- Right child of index i: `2 * i + 2`

### For Srinivas (Integration & Coordination)

**Your files:**
- Primary: `leaderboard_system.py`
- Secondary: `cli.py` (demo interface)
- Tests: `test_leaderboard.py` (TestLeaderboardSystem class)

**Implementation order:**
1. Wait for basic BST insert/delete from Rider
2. Wait for basic PQ enqueue/dequeue from Chase
3. Start with `add_player()` - direct BST insertion
4. Then `process_next_update()` - the core integration logic
5. Then query methods: `get_leaderboard()`, `get_player_rank()`, etc.
6. Finally demo and simulation features

**Key integration points:**
- `player_lookup` hash map: maps player_id → BSTNode for O(1) access
- Update flow: dequeue → lookup old node → delete from BST → insert new node
- New players: check if exists, if not create Player object

**Testing approach:**
- Test the full flow: add → update → process → query
- Test with many updates for same player
- Test updates for non-existent players
- Integration test: 100 players, 1000 updates, verify correctness

**Presentation prep:**
- Create slides showing architecture diagram
- Prepare complexity analysis table
- Record demo video as backup
- Write final report draft

## Development Workflow

### Branch Strategy
```bash
# Create your feature branch
git checkout -b rider/bst-implementation
# or
git checkout -b chase/priority-queue
# or
git checkout -b srinivas/integration

# Make changes, commit often
git add .
git commit -m "Implement BST insertion"

# Push your branch
git push origin your-branch-name

# Create pull request on GitHub
# Wait for code review from teammates
# Merge when approved
```

### Code Review Checklist
- [ ] Does the code have docstrings?
- [ ] Are there unit tests?
- [ ] Does it follow Python naming conventions?
- [ ] Are edge cases handled?
- [ ] Is complexity documented?

### Weekly Goals

**Week 1: Core Implementation**
- Rider: Basic BST insert/delete/search
- Chase: Basic PQ enqueue/dequeue
- Srinivas: Player class finalized, test data generator

**Week 2: Integration**
- Rider: Complete all BST methods, start tests
- Chase: Complete PQ including heapify, start tests
- Srinivas: Integrate BST + PQ, basic CLI working

**Week 3: Polish & Presentation**
- All: Complete unit tests
- Rider: Optional AVL balancing
- Chase: Optional request merging
- Srinivas: Tournament simulation, presentation, final report

## Common Issues & Solutions

### Issue: "My BST deletions aren't working"
- Draw the tree on paper before/after
- Test each case separately: leaf, one child, two children
- Use print statements to trace execution
- Check if you're updating parent pointers correctly

### Issue: "My heap doesn't maintain heap property"
- Verify parent/child index calculations
- Check comparison in bubble_up/bubble_down (< vs >)
- Test bubble operations separately before full enqueue/dequeue
- Print the heap array after each operation

### Issue: "Integration: players disappearing or duplicating"
- Check that you're removing old node before inserting new one
- Verify player_lookup hash map stays in sync with BST
- Make sure you're not confusing player_id with score

### Issue: "Tests are failing"
- Read the error message carefully - what was expected vs actual?
- Add print statements to understand what's happening
- Test components in isolation before integration
- Use debugger (pdb) to step through code

## Communication

### Team Meetings
- Schedule: [Fill in your meeting times]
- Agenda template:
  1. Progress updates (5 min each)
  2. Blockers and questions (10 min)
  3. Code review (15 min)
  4. Next steps (5 min)

### Code Review Protocol
1. Create pull request with clear description
2. Tag teammates for review
3. Wait for at least one approval
4. Address feedback
5. Merge to main

### Getting Help
- From each other: Post in team chat/Discord
- From professor: Office hours or email
- From internet: StackOverflow, but cite sources in comments

## Pre-Presentation Checklist

Two weeks before:
- [ ] All core features implemented
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] CLI demo works smoothly

One week before:
- [ ] Slides drafted
- [ ] Demo script written
- [ ] Report outline done
- [ ] Each person practices their section

Three days before:
- [ ] Full team run-through
- [ ] Slides finalized
- [ ] Demo recorded as backup
- [ ] Report first draft complete

Day before:
- [ ] Final practice run
- [ ] Test presentation on actual equipment
- [ ] Report submitted
- [ ] Everyone knows their parts

## Resources

**Python Documentation:**
- [Classes](https://docs.python.org/3/tutorial/classes.html)
- [Unit Testing](https://docs.python.org/3/library/unittest.html)

**Algorithms:**
- Visualizations: [VisuAlgo](https://visualgo.net/)
- BST operations: [GeeksforGeeks BST](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
- Heap operations: [GeeksforGeeks Heap](https://www.geeksforgeeks.org/heap-data-structure/)

**Git & GitHub:**
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Pull Requests](https://docs.github.com/en/pull-requests)

Good luck! You've got this! 🚀
