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
    df = pd.read_csv("data/Microwave Link Report_05-19-2025_05-47-44.csv", skiprows=11)
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
    breakfast_items = ["Apple Vineger", "Ruti Porota"]
    print(breakfast_items[1])
    return


@app.cell
def _(df):
    source_ne_names = df["Source NE Name"]
    # type(source_ne_names)
    # type(df)
    source_ne_names
    return


@app.cell
def _(df):
    sink_ne_names = df["Sink NE Name"]
    sink_ne_names
    return


@app.cell
def _():
    # df[['Source NE Name', 'Sink NE Name']].to_csv("ne_names.csv")
    return


@app.cell
def _(df):
    df["Source NE Name Cleaned"] = (
        df["Source NE Name"].str.split("_NE_").str[0].str.split("-").str[1]
    )
    df["Sink NE Name Cleaned"] = (
        df["Sink NE Name"].str.split("_NE_").str[0].str.split("-").str[1]
    )
    df["Source NE Name Cleaned"]
    return


@app.cell
def _(df):
    sample = df["Source NE Name Cleaned"].loc[1]
    # sample.split("_NE_")[0]
    sample
    return


@app.cell
def _():
    # df.to_csv("cleaned.csv")
    return


@app.cell
def _(df):
    df.columns[0]
    return


@app.cell
def _(df):
    # 1. New column: Source PLA Name [=A2&"-"&J2&"("&"PLA"&"-"&J2&")"]
    cleaned_df = df[df["Source PLA ID"] != "/"]

    cleaned_df["Source PLA Name"] = (
        cleaned_df["Source NE Name"]
        + "-"
        + cleaned_df["Source PLA ID"]
        + "("
        + "PLA"
        + "-"
        + cleaned_df["Source PLA ID"]
        + ")"
    )
    cleaned_df["Source PLA Name"]

    # cleaned_df.to_csv("cleanded.csv")
    return (cleaned_df,)


@app.cell
def _(cleaned_df):
    cleaned_df["Level Numeric"] = (
        cleaned_df["Level"].str.extract(r"(\d+)").astype(int)
    )
    cleaned_df["Level Numeric"]
    return


@app.cell
def _(cleaned_df):
    pla_capacity = cleaned_df.groupby("Source PLA Name")["Level Numeric"].sum()
    # pla_capacity.to_csv("pla_cap.csv")
    return


@app.cell
def _(cleaned_df):
    cleaned_df["Source NE Name Cleaned"]
    cleaned_df["Sink NE Name Cleaned"]
    return


@app.cell
def _(cleaned_df):
    # cleaned_df['Link Name'] = cleaned_df['Source NE Name Cleaned'] + '-' + cleaned_df['Sink NE Name Cleaned']
    import re

    pattern = r"\d+"


    def link_name_creator(row):
        src_name = row["Source NE Name Cleaned"]
        sink_name = row["Sink NE Name Cleaned"]

        match = re.search(pattern, src_name)
        if match:
            src_side = match.group()
        else:
            print("Not Matched")

        match = re.search(pattern, sink_name)
        if match:
            sink_side = match.group()
        else:
            print("Not Matched")
            # raise Exception("DQ Issue")

        if src_side > sink_side:
            return src_name + "-" + sink_name
        else:
            return sink_name + "-" + src_name


    cleaned_df["Link Name"] = cleaned_df.apply(link_name_creator, axis=1)
    cleaned_df["Link Name"]
    return pattern, re


@app.cell
def _(cleaned_df, pattern, re):
    cleaned_df['Link Name Lambda'] = cleaned_df.apply(lambda row: row['Source NE Name Cleaned'] + '-' + row['Sink NE Name Cleaned'] if re.search(pattern, row['Source NE Name Cleaned']).group() > re.search(pattern, row['Sink NE Name Cleaned']).group() else row['Sink NE Name Cleaned'] + '-' + row['Source NE Name Cleaned'], axis=1)
    cleaned_df[['Link Name Lambda', 'Source NE Name Cleaned', 'Sink NE Name Cleaned']]
    return


@app.cell
def _():
    print("Chat123" > "Dhaka001")
    return


@app.cell
def _(cleaned_df):
    cleaned_df[["Source NE Name Cleaned", "Sink NE Name Cleaned"]]
    return


@app.cell
def _():
    # cleaned_df.to_csv('link.csv')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Pandas: merge two dataframes""")
    return


@app.cell
def _(pd):
    students = pd.DataFrame({
        'roll': [1, 2, 3, 4],
        'name': ['achinta', 'robin', 'asif', 'fakhrul']
    })
    students
    return (students,)


@app.cell
def _(pd):
    grades = pd.DataFrame({
        'roll': [2, 4, 5],
        'grade': ['A+', 'A', 'D'],
        'name': ['robin', 'fakhrul', 'Unknown']
    })
    grades
    return (grades,)


@app.cell
def _(grades, pd, students):
    pd.merge(students, grades, on='name', how='right')
    return


@app.cell
def _(grades, pd, students):
    pd.merge(students, grades, on='id', how='right')
    return


@app.cell
def _(grades, pd, students):
    new_df = pd.merge(students, grades, on='roll', how='outer', suffixes=('_student', '_grade'))
    new_df
    return


@app.cell
def _(grades):
    # grades.drop('name', axis=1)
    grades
    return


@app.cell
def _(cleaned_df):
    cleaned_df['Source PLA Type'].unique()
    return


@app.cell
def _(cleaned_df):
    cleaned_df.groupby('Link Name').sum('Level Numeric')
    cleaned_df.groupby('Source PLA Name').sum('Level Numeric')
    return


@app.cell
def _(cleaned_df):
    def add_group_column(row):
        # print(row)
        source_pla_type = row['Source PLA Type']
        link_name = row['Link Name']
        source_pla_name = row['Source PLA Name']
    
        print(source_pla_type)
        if source_pla_type == 'EPLA' or source_pla_type == 'PLA':
            return source_pla_name
            print("HERE")
        else:
            return link_name
            print("HERE ALSO")
    
    cleaned_df['group_key'] = cleaned_df.apply(add_group_column, axis=1)
    cleaned_df[['group_key', 'Source PLA Type']]

    return


@app.cell
def _(cleaned_df):
    cleaned_df.groupby('group_key').sum('Level Numeric').to_csv('grouped_df.csv')
    cleaned_df.to_csv('cleaned_df.csv')
    return


if __name__ == "__main__":
    app.run()
