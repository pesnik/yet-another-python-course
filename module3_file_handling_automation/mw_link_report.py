import marimo

__generated_with = "0.13.8"
app = marimo.App(width="columns")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return


@app.cell
def _():
    f = open('/home/pesnik/yet-another-python-course/Microwave Link Report_05-19-2025_05-47-44.csv', 'r')
    return (f,)


@app.cell
def _(f):
    lines = f.readlines()
    len(lines)
    return (lines,)


@app.cell
def _(lines):
    lines[11].split(',')
    return


@app.cell
def _(lines):
    # Meta Information Store

    total_rows = lines[9]
    modified_time = lines[5]
    print(total_rows, modified_time)
    return


@app.cell
def _(f):
    f.close()
    return


@app.cell
def _():
    import csv


    with open('/home/pesnik/yet-another-python-course/Microwave Link Report_05-19-2025_05-47-44.csv') as csvfile:
        csv_lines = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in csv_lines:
            print(row)

        # print("file closed")

    print("outside scope")
    return


@app.cell
def _():
    import pandas as pd

    df = pd.read_csv("Microwave Link Report_05-19-2025_05-47-44.csv", skiprows=11)
    meta_df = pd.read_csv("Microwave Link Report_05-19-2025_05-47-44.csv", skipfooter=len(df) + 1)
    return df, meta_df


@app.cell
def _(df):
    print(df.columns)
    print(len(df))

    # df.describe()

    df.head()
    return


@app.cell
def _(meta_df):
    meta_df
    return


@app.cell
def _(df):
    df[df['Source PLA Type'] != '/']
    return


@app.cell
def _(df):
    cleaned_df = df[['Source PLA Type', 'Source PLA ID']]
    cleaned_df
    return


if __name__ == "__main__":
    app.run()
