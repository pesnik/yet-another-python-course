import marimo

__generated_with = "0.13.8"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Data Structure""")
    return


@app.cell
def _():
    import requests

    url = "https://web-api.banglalink.net/api/v1/offers-categories"

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.json())
    return


@app.cell
def _():
    # list
    print([])

    sauslys_items = ["fanta", "sandwithc", "laddu", "doi", "singara"]
    sauslys_prices = [10, "20", "5", "50", "25"]

    spicy_items = ["asdfa", "asfads"]
    spicy_prices = [12, 45]
    return sauslys_items, sauslys_prices


@app.cell
def _(sauslys_items, sauslys_prices):
    # index

    print(sauslys_items[0], " = ", sauslys_prices[0])
    print(sauslys_items[1], " = ", sauslys_prices[1])
    print(sauslys_items[2], " = ", sauslys_prices[2])
    print(sauslys_items[3], " = ", sauslys_prices[3])
    return


@app.cell
def _(sauslys_items, sauslys_prices):
    item_no = 0

    while item_no <= 4:
        print(sauslys_items[item_no], " =", sauslys_prices[item_no])
        item_no += 1
    return


@app.cell
def _(sauslys_items, sauslys_prices):
    total_item = len(sauslys_items)

    print(total_item)

    try:
        for item in range(0, total_item + 5):
            print(sauslys_items[item], " =", sauslys_prices[item])
    except Exception as error_occurred:
        print("Email to BL: ", error_occurred)
    return


@app.cell
def _(sauslys_items):
    for item_name in sauslys_items:
        print(item_name)
    return


@app.cell
def _():
    sim = [
        {
            "id": 1,
            "name": "Prepaid",
            "alias": "prepaid"
        },
        {
            "id": 2,
            "name": "Postpaid",
            "alias": "postpaid"
        },
        {
            "id": 3,
            "name": "Propaid",
            "alias": "propaid"
        }
    ]

    print(sim)
    print(type(sim))
    return (sim,)


@app.cell
def _(sim):
    prepaid = sim[0]
    print(prepaid)
    return (prepaid,)


@app.cell
def _(prepaid):
    print(type(prepaid))
    return


@app.cell
def _(prepaid):
    print(prepaid['alias'])

    keys = ["id", "name", "alias"]
    values = ["1", "Prepaid", "prepaid"]
    return


@app.cell
def _():
    sausly_bakes = {
        "fanta": 25,
        'singara': 40
    }


    sausly_bakes["kolija_singara"] = 56
    print(sausly_bakes)
    return


@app.cell
def _(sauslys_items, sauslys_prices):
    print(sauslys_items)
    print(sauslys_prices)
    return


app._unparsable_cell(
    r"""
     generated_list = {}
    print(generated_list)
    for i in range(len(sauslys_items)):
        generated_list[sauslys_items[i]] = sauslys_prices[i]
        print(sauslys_items[i], ' = ', sauslys_prices[i])

    print(generated_list)
    """,
    name="_"
)


if __name__ == "__main__":
    app.run()
