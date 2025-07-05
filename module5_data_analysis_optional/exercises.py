import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _():
    # pd.read_csv()
    ...
    ...
    ...
    # pd.to_csv()
    return


@app.cell
def _(pd):
    df = pd.read_csv("Microwave Link Report_05-19-2025_05-47-44.csv", skiprows=11)
    df
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Requirements""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## 1. New column: Source PLA Name [=A2&"-"&J2&"("&"PLA"&"-"&J2&")"]
    ## 2. New column: Sink PLA Name [=D2&"-"&K2&"("&"PLA"&"-"&K2&")"]
    ## 3. New column: Source Site Name
    ## 4. New column: Sink Site Name
    ## 5. New column: Link Name
    ## 6. New column: Link Capacity
    ## 7. New column: Capacity
    """
    )
    return


@app.cell
def _(df):
    df.head()
    return


@app.cell
def _(df):
    desc_df = df.describe()
    print(desc_df)
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Data Structure
    ### Series
    #### Column, List, 1 Dimension
    ### Datafram
    #### Table, Multi Dimension
    """
    )
    return


@app.cell
def _():
    breakfast_items = ['Apple Vineger', 'Ruti Porota']
    print(breakfast_items[1])
    return


@app.cell
def _(df):
    source_ne_names = df['Source NE Name']
    # type(source_ne_names)
    # type(df)
    source_ne_names
    return


@app.cell
def _(df):
    sink_ne_names = df['Sink NE Name']
    sink_ne_names
    return


@app.cell
def _():
    # df[['Source NE Name', 'Sink NE Name']].to_csv("ne_names.csv")
    return


@app.cell
def _(df):
    df['Source NE Name Cleaned'] = df['Source NE Name'].str.split("_NE_").str[0].str.split('-').str[1]
    df['Source NE Name Cleaned']
    return


@app.cell
def _(df):
    sample = df['Source NE Name Cleaned'].loc[1]
    # sample.split("_NE_")[0]
    sample
    return


@app.cell
def _(df):
    df.to_csv("cleaned.csv")
    return


@app.cell
def _(df):
    df.columns[0]
    return


@app.cell
def _(df):
    # 1. New column: Source PLA Name [=A2&"-"&J2&"("&"PLA"&"-"&J2&")"]
    cleaned_df = df[df['Source PLA ID'] != '/']

    cleaned_df['Source PLA Name'] = cleaned_df['Source NE Name'] + '-' + cleaned_df['Source PLA ID'] + '(' + "PLA" + "-" + cleaned_df['Source PLA ID'] + ')'
    cleaned_df['Source PLA Name']

    cleaned_df.to_csv("cleanded.csv")
    return (cleaned_df,)


@app.cell
def _(cleaned_df):
    cleaned_df['Level Numeric'] = cleaned_df['Level'].str.extract(r'(\d+)').astype(int)
    cleaned_df['Level Numeric']
    return


@app.cell
def _(cleaned_df):
    pla_capacity = (
        cleaned_df
        .groupby('Source PLA Name')['Level Numeric']
        .sum()
    )
    pla_capacity.to_csv("pla_cap.csv")
    return


if __name__ == "__main__":
    app.run()
