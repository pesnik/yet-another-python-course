import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# For Loop""")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    # keywords
    name
    break
    while
    laptop
    loop
    for
    in
    with
    """
    )
    return


@app.cell
def _():
    for i in range(1, 11):
        if i & 1:
            print(f"{i} is odd")
        else:
            print(f"{i} is even")


    print(0 == False)
    print(1 == True)
    print(0 == True)

    i = 1
    while i <= 10:
        print(i)
        i += 1
        i = i + 1
    return


@app.cell
def _():
    pythonsita = ["asif", "rakib", "robin"]

    for i in pythonsita:
        print(i)
    return


if __name__ == "__main__":
    app.run()
