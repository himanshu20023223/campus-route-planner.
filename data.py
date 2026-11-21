# Illustrative campus graph. Replace these sample locations and edges
# with surveyed campus coordinates and verified walkway connections.
NODES = {
    "gate": {"name": "Main Gate", "x": 0, "y": 0, "z": 0, "kind": "entry"},
    "admin": {"name": "Admin Block", "x": 2, "y": 1, "z": 0, "kind": "building"},
    "library": {"name": "Central Library", "x": 5, "y": 1, "z": 0, "kind": "building"},
    "cafeteria": {"name": "Cafeteria", "x": 3, "y": 4, "z": 0, "kind": "amenity"},
    "academic": {"name": "Academic Block", "x": 7, "y": 4, "z": 0, "kind": "building"},
    "auditorium": {"name": "Auditorium", "x": 10, "y": 2, "z": 0, "kind": "amenity"},
    "sports": {"name": "Sports Complex", "x": 1, "y": 7, "z": 0, "kind": "amenity"},
    "hostel": {"name": "Hostel", "x": 6, "y": 8, "z": 0, "kind": "building"},
    "medical": {"name": "Medical Centre", "x": 10, "y": 7, "z": 0, "kind": "amenity"},
    "parking": {"name": "Parking Area", "x": -2, "y": 3, "z": 0, "kind": "amenity"},
    "quad": {"name": "Central Courtyard", "x": 5, "y": 5, "z": 0, "kind": "junction"},
    "lab": {"name": "Computer Lab", "x": 8, "y": 7, "z": 0, "kind": "building"}
}
RAW_EDGES = [
    ("gate","admin",1.0,True), ("gate","parking",1.2,True),
    ("gate","sports",2.0,True), ("admin","library",1.5,True),
    ("admin","cafeteria",1.4,True), ("library","academic",1.8,True),
    ("library","quad",1.6,True), ("cafeteria","quad",1.3,True),
    ("cafeteria","sports",1.8,True), ("quad","academic",1.5,True),
    ("quad","hostel",2.0,True), ("academic","auditorium",1.7,False),
    ("academic","lab",1.4,True), ("lab","medical",1.5,True),
    ("hostel","medical",2.1,True), ("sports","hostel",2.7,False),
    ("auditorium","medical",2.2,True), ("parking","cafeteria",2.8,True),
    ("library","auditorium",3.2,True), ("admin","quad",2.5,True)
]
EDGES = [{"from": a, "to": b, "weight": w, "accessible": ok} for a,b,w,ok in RAW_EDGES]
CAMPUS_GRAPH = {"nodes": NODES, "edges": EDGES}
LOCATIONS = [{"id": k, "name": v["name"]} for k,v in NODES.items()]
