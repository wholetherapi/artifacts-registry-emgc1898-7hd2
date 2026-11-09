"""Segment construction pipeline for Parallax Index."""

import json


def build_segments(keys, segment_size):
    segments = []
    for start in range(0, len(keys), segment_size):
        chunk = sorted(keys[start : start + segment_size])
        segments.append({"min": chunk[0], "max": chunk[-1], "size": len(chunk)})
    return segments


def write_manifest(path, segments):
    with open(path, "w", encoding="utf-8") as handle:
        json.dump({"segments": segments}, handle, indent=2)
