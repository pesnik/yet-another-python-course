import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Function""")
    return


@app.cell
def _():
    i = 10
    while i <= 20:
        if i & 1:
            print("odd")
        else:
            print("even")

        i+= 1


    i = 20
    while i <= 30:
        if i & 1:
            print("odd")
        else:
            print("even")

        i+= 1
    return


@app.cell
def _():
    def even_odd_printer(start, end):
        while start <= end:
            if start & 1:
                print(f"{start} = odd")
            else:
                print(f"{start} = even")
    
            start += 1
        
    start = 10
    end = 20
    even_odd_printer(start, end)
    return (even_odd_printer,)


@app.cell
def _(even_odd_printer):
    even_odd_printer(45, 50)

    even_odd_printer(1, 10)
    return


@app.cell
def _():


    return


if __name__ == "__main__":
    app.run()
