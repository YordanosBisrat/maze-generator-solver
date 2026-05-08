# Maze Generator and Solver

This project generates and solves rectangular mazes using stack-based depth-first search (DFS) and backtracking algorithms.
The maze is visualized dynamically using Pygame, where an invisible “mouse” carves paths through walls to create a proper maze structure. A second solving algorithm then traverses the maze while visualizing explored paths, dead ends, and the final solution.

---

# Features

- Random maze generation
- Dynamic “wall eating” animation
- Stack-based DFS generation
- Backtracking maze solver
- Real-time OpenGL visualization
- Dead-end visualization
- Final solution path visualization
- Randomized traversal behavior
- Interactive controls
- Adjustable animation speed
- Random cycle generation (bonus feature)


---

# Maze Representation

The maze consists of a rectangular grid of cells.

Each cell stores wall information:

- North wall
- South wall
- East wall
- West wall

The assignment's required wall arrays are represented internally using object-oriented cell structures.

```python
# northWall and eastWall representation
cell.north -> northWall
cell.east  -> eastWall
```

---

# Algorithms Used

## 1. Maze Generation (DFS Backtracking)

The maze is generated using recursive backtracking with a stack.

### Process

1. Start with all walls intact.
2. Place a “mouse” in a starting cell.
3. Randomly choose an unvisited neighboring cell.
4. Remove the wall between the two cells.
5. Push the current position onto a stack.
6. Continue until trapped.
7. Backtrack using the stack.
8. Finish when all cells have been visited.

This guarantees a proper maze where every cell is connected by a unique path.

---

## 2. Maze Solving (Backtracking DFS)

The maze solver uses another DFS traversal algorithm.

### Visualization

- 🟡 Yellow Cell → current mouse position
- 🟠 Orange Cell → explored path
- 🔵 Blue Cell → dead end / backtracked path
- 🔴 Red Cell → final successful path
- 🟢 Green Cell → start and goal cells



The solver explores paths dynamically and backtracks whenever a dead end is reached.

---

## Technologies

- Python
- Pygame

---

# Project Structure

```text
maze-generator-solver/
│
├── src/
│   ├── main.py
│   ├── maze.py
│   ├── renderer.py
│   ├── solver.py
│   └── cell.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd maze-generator-solver
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

```bash
python src/main.py
```

---

# Controls

| Key | Action |
|-----|--------|
| R | Reset maze  |
| SPACE | Pause / Resume  |

---

# Bonus Features 

- Random cycle generation (1 in 20 wall removals)
- Pause / Play controls
- Speed control
- Instant maze regeneration
- Cleaner visualization improvements
- Interactive UI panel
- Dynamic solver animation

---

# Educational Concepts Demonstrated

- Depth-First Search (DFS)
- Backtracking
- Stack data structures
- Graph traversal
- Procedural generation
- Pygame rendering
- Maze theory

---

### Loom = https://www.loom.com/share/6e2fdcba65aa4443a143f722d3f496a6

---

# Author

Yordanos Bisrat
