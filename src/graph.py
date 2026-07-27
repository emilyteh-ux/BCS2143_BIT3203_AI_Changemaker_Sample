"""Graph loading and lookup utilities for the campus map."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List


@dataclass(frozen=True)
class Edge:
    to: str
    distance: float
    wheelchair_accessible: bool
    surface: str


class CampusGraph:
    """Undirected weighted graph built from a JSON campus map file."""

    def __init__(self, nodes: Dict[str, dict], adjacency: Dict[str, List[Edge]]):
        self.nodes = nodes
        self.adjacency = adjacency

    @classmethod
    def from_json(cls, path: str | Path) -> "CampusGraph":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        nodes = data["nodes"]
        adjacency: Dict[str, List[Edge]] = {node_id: [] for node_id in nodes}

        for edge in data["edges"]:
            a, b = edge["from"], edge["to"]
            forward = Edge(b, edge["distance"], edge["wheelchair_accessible"], edge["surface"])
            backward = Edge(a, edge["distance"], edge["wheelchair_accessible"], edge["surface"])
            adjacency[a].append(forward)
            adjacency[b].append(backward)

        return cls(nodes, adjacency)

    def neighbours(self, node_id: str) -> List[Edge]:
        return self.adjacency.get(node_id, [])

    def coordinates(self, node_id: str) -> tuple[float, float]:
        n = self.nodes[node_id]
        return n["x"], n["y"]

    def name(self, node_id: str) -> str:
        return self.nodes[node_id]["name"]
