#!/usr/bin/python3
"""BOXES"""


def canUnlockAll(boxes):
    """take boxes"""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop(0)
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)
