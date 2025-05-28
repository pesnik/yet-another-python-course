import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# File Operation""")
    return


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(pd):
    df = pd.read_csv("Microwave Link Report_05-19-2025_05-47-44.csv", skiprows=11)
    df[df['Source PLA ID'] != '/']
    return


if __name__ == "__main__":
    app.run()
