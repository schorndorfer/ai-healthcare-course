"""Offline, invented extraction labels; no patient data or API calls."""

from collections import defaultdict

# Each row is an invented note label, prediction, and teaching-only subgroup.
CASES = [
    ("A", True, True),
    ("A", True, False),
    ("A", False, False),
    ("A", False, True),
    ("B", True, True),
    ("B", True, True),
    ("B", False, False),
    ("B", False, False),
]


def metrics(rows):
    tp = sum(reference and prediction for _, reference, prediction in rows)
    fp = sum(not reference and prediction for _, reference, prediction in rows)
    fn = sum(reference and not prediction for _, reference, prediction in rows)
    tn = sum(not reference and not prediction for _, reference, prediction in rows)
    return {"n": len(rows), "tp": tp, "fp": fp, "fn": fn, "tn": tn,
            "precision": tp / (tp + fp) if tp + fp else None,
            "recall": tp / (tp + fn) if tp + fn else None}


def main():
    by_group = defaultdict(list)
    for row in CASES:
        by_group[row[0]].append(row)
    for name, rows in [("overall", CASES), *sorted(by_group.items())]:
        print(name, metrics(rows))
    print("Teaching example only: n=4 per group; do not infer population fairness.")


if __name__ == "__main__":
    main()
