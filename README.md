# Campus Route Planner Using Shortest Path Algorithms

A local Python/Flask web application inspired by the attached DAA presentation. It demonstrates a campus walkway graph, shortest-path search, an accessibility filter and a smoothed route display.

## Features

- Select start and destination campus locations.
- Run Dijkstra's shortest-path algorithm.
- Run A* heuristic search.
- Toggle wheelchair-friendly routing (only edges marked accessible are considered).
- View the chosen route on an interactive, offline-friendly campus map.
- View distance cost, visited-node count, execution time and route steps.
- Route line is visually smoothed for presentation; the algorithm still calculates on the original graph edges.

## Requirements

- Python 3.9 or newer
- pip

## Run on Windows

1. Extract the ZIP file.
2. Open the extracted `Campus_Route_Planner` folder.
3. Open Command Prompt or the VS Code terminal in this folder.
4. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

5. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

6. Run this file:

   ```bash
   python app.py
   ```

7. Open this address in your browser:

   `http://127.0.0.1:5000`

## Run on macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then visit `http://127.0.0.1:5000`.

## Which file should I run?

**Run `app.py`.** Do not run `algorithms.py`, `data.py` or files inside `templates` directly.

## Project structure

```text
Campus_Route_Planner/
├── app.py                 # Flask application entry point
├── algorithms.py          # Dijkstra and A* implementations
├── data.py                # Sample campus graph and locations
├── requirements.txt       # Python dependencies
├── README.md              # Setup and usage guide
├── templates/
│   └── index.html         # Website page
└── static/
    ├── style.css          # Website styling
    └── app.js             # Interactive map and API calls
```

## Important: sample campus data

The PPT does not include a measured campus map, surveyed coordinates, or a complete walkway dataset. The current graph is therefore an illustrative sample campus layout, not an accurate SGT University map. Edit `data.py` to add real buildings, walkway connections, distances and accessibility attributes.

Each node has `x`, `y`, and optional `z` coordinates. Each edge has:
- `from`: starting node ID
- `to`: connected node ID
- `weight`: route cost/distance units
- `accessible`: whether the edge is included in wheelchair-friendly routing

The weights in the demo are illustrative route-cost units, not measured metres.

## Algorithm note: A* versus Bellman–Ford

The PPT describes a heuristic algorithm using `f(n) = g(n) + h(n)`, where `g` is cost so far and `h` is estimated distance to the goal. That is the A* search evaluation function, not Bellman–Ford. This implementation labels that option **A*** to keep the algorithm technically correct. Bellman–Ford is a different algorithm based on repeated edge relaxation and is useful when negative edge weights may exist. Campus walkway distances are non-negative, so Dijkstra and A* are suitable choices for this demonstration.

## Accessibility note

The accessible toggle filters out edges whose `accessible` value is false. This is a simplified demonstration, not a certified accessibility assessment. Actual accessibility requires verified ramp gradients, widths, surfaces, lifts, door access and floor transitions. The sample graph does not model multi-floor indoor navigation.

## Performance note

Execution time is measured for the in-memory search only. It is not a claim that all campus-scale route calculations will complete under 2 ms. For a meaningful benchmark, use a surveyed graph and repeat tests at multiple graph sizes.
