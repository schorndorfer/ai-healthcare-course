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
    from math import exp, sqrt

    return exp, mo, sqrt


@app.cell
def _(mo):
    mo.md("""
    # Attention on invented tokens

    An **optional Python companion** to the R-first Week 2 lab. These vectors are
    hand-picked to illustrate attention, not learned clinical embeddings. No API,
    patient text or model download is used. Attention weights are **not** explanations
    of clinical decisions.
    """)
    return


@app.cell
def _(mo):
    scale = mo.ui.slider(start=0.5, stop=3.0, step=0.5, value=1.0,
                         label="Query strength")
    scale
    return (scale,)


@app.cell
def _(exp, scale, sqrt):
    tokens = ("no", "fever", "today")
    keys = ((1.0, 0.0), (0.0, 1.0), (0.5, 0.5))
    values = ((1.0, 0.0), (0.0, 1.0), (0.5, 0.5))
    query = (scale.value, 0.5)  # invented query, not a clinical concept
    scores = [sum(a * b for a, b in zip(query, key)) / sqrt(2) for key in keys]
    unnormalized = [exp(score - max(scores)) for score in scores]
    weights = [value / sum(unnormalized) for value in unnormalized]
    output = [sum(weight * value[i] for weight, value in zip(weights, values))
              for i in range(2)]
    return output, scores, tokens, weights


@app.cell
def _(mo, output, scores, tokens, weights):
    rows = "\n".join(
        f"| {token} | {score:.3f} | {weight:.3f} |"
        for token, score, weight in zip(tokens, scores, weights)
    )
    mo.md(f"""| Invented token | scaled score | softmax weight |
    |---|---:|---:|
    {rows}

    Output vector: **({output[0]:.3f}, {output[1]:.3f})**.
    Weights sum to {sum(weights):.3f}. Change the slider: which weights shift?
    Why does this not establish whether a person has a fever?
    """)
    return


if __name__ == "__main__":
    app.run()
