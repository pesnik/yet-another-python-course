

import marimo

__generated_with = "0.11.12"
app = marimo.App(width="medium", layout_file="layouts/exercises.grid.json")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(r"""# Loop in Python""")
    return


@app.cell
def _():
    print(1)
    print(2)
    print(3)
    print(4)
    return


@app.cell
def _():
    for i in range(1, 11):
        print(i)
    return (i,)


@app.cell
def _():
    j = 1
    while j <= 1:
        print(j)
        j = j + 1

    print("While Loop Finished")
    return (j,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # 🚀 Liftoff Countdown: The Story Behind the Numbers

        When you think of a rocket launch, what's the first thing that comes to mind?

        **"10... 9... 8... 7..."** — the classic **reverse countdown**!
        But did you know this tradition started in the **movies** before it became a real-life NASA staple?

        ### 🎬 The Origin Story

        The reverse countdown was popularized in Fritz Lang’s 1929 sci-fi film *Woman in the Moon*, where it added dramatic tension. NASA adopted it later — not for the drama, but to build precision and coordination in rocket launches.
        """
    )
    return


@app.cell
def _():
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Guessing Game""")
    return


@app.cell
def _():
    hidden_number = "6"
    gussed = input("Please guess a number  between 1 to 10: ")
    while gussed != hidden_number:
        print(f"Ohhh...you gussed it wrong!")
        gussed = input("Please guess another number  between 1 to 10: ")
        if gussed == hidden_number:
            print("You're right!")
    return gussed, hidden_number


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## [Feature]: Oops! Limit exceeded""")
    return


@app.cell
def _(mo):
    mo.md(r"""# Excercise""")
    return


if __name__ == "__main__":
    app.run()
