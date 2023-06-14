import requests
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"


def load() -> dict:
    rows = requests.get(url).text.split("\n")
    values = {}
    for i in rows[2:-1]:
        row = i.split("|")
        mult = int(row[2])
        values[f"{row[3]}"] = float((row[4]).replace(",", ".")) / mult
    values["CZK"] = 1
    return values


def ask(message: str, keys: list, default: str) -> str:
    return Prompt.ask(
        message,
        choices=keys,
        show_choices=False,
        default=default,
    ).upper()


def get_keys(values: dict) -> list:
    keys = []
    for i in values.keys():
        keys.append(i)
        keys.append(i.lower())
    return keys


def main():
    values = load()
    keys = get_keys(values)
    currency_from = ask("Zadejte pocatecni menu", keys, "CZK")
    prompt_price = Prompt.ask("Zadejte castku")
    price = float(prompt_price) if prompt_price.replace(".", "").isnumeric() else None
    if price is None:
        return print("Castka musi byt cislo")
    currency_to = ask("Zadejte cilovou menu", keys, "EUR")
    czk = values[currency_from] * price
    if currency_to == "CZK":
        return print(Panel.fit(f"{price} {currency_from} -> {czk} {currency_to}"))
    resutl = round(czk / values[currency_to], 3)
    return print(Panel.fit(f"{price} {currency_from} -> {resutl} {currency_to}"))


if __name__ == "__main__":
    main()