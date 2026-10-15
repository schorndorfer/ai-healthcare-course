# /// script
# requires-python = ">=3.12"
# dependencies = ["marimo>=0.20,<1"]
# ///

import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Subgroup metrics on invented predictions

    An optional local Python companion to Week 8. The groups and labels are entirely
    invented. With only four examples per group, the numbers are for learning metric
    definitions **not** making fairness claims. Nothing is uploaded.
    """)
    return


@app.cell
def _(mo):
    fix_miss = mo.ui.checkbox(label="Correct the missed positive in group A", value=False)
    fix_miss
    return (fix_miss,)


@app.cell
def _(fix_miss):
    cases = [
        ("A", True, True), ("A", True, fix_miss.value),
        ("A", False, False), ("A", False, True),
        ("B", True, True), ("B", True, True),
        ("B", False, False), ("B", False, False),
    ]
    return (cases,)


@app.cell
def _(cases):
    def score(rows):
        tp = sum(reference and prediction for _, reference, prediction in rows)
        fp = sum(not reference and prediction for _, reference, prediction in rows)
        fn = sum(reference and not prediction for _, reference, prediction in rows)
        return (len(rows), tp, fp, fn,
                f"{tp / (tp + fp):.2f}" if tp + fp else "undefined",
                f"{tp / (tp + fn):.2f}" if tp + fn else "undefined")

    summary = [(label, *score(rows)) for label, rows in [
        ("overall", cases),
        ("A", [row for row in cases if row[0] == "A"]),
        ("B", [row for row in cases if row[0] == "B"]),
    ]]
    return (summary,)


@app.cell
def _(mo, summary):
    rows = "\n".join(
        f"| {group} | {n} | {tp} | {fp} | {fn} | {precision} | {recall} |"
        for group, n, tp, fp, fn, precision, recall in summary
    )
    mo.md(f"""| Group | n | TP | FP | FN | Precision | Recall |
    |---|---:|---:|---:|---:|---:|---:|
    {rows}

    Precision = TP/(TP+FP); recall = TP/(TP+FN). What changed when you fixed
    one case? Which metric did **not** improve for group A, and why? What information
    about real-world populations is missing from this tiny exercise?
    """)
    return


if __name__ == "__main__":
    app.run()
