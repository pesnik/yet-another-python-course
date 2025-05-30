import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r""" """)
    return


@app.cell
def _():
    f = open('/home/pesnik/yet-another-python-course/Microwave Link Report_05-19-2025_05-47-44.csv', 'r')
    return (f,)


@app.cell
def _(f):
    lines = f.readlines()
    len(lines)
    return


@app.cell
def _():
    return


@app.cell
def _(f):
    f.close()
    return


if __name__ == "__main__":
    app.run()
