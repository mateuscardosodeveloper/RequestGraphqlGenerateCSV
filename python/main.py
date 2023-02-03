import csv
import pandas
import requests
from typing import Callable
from functools import partial
from dataclasses import dataclass


@dataclass
class RickMoryResponse:
    name: str
    status: str
    species: str


QUERY = """query {
    characters {
    results {
      name
      status
      species
    }
  }
}"""


def query_api() -> list[RickMoryResponse]:
    response = requests.post(
        url='https://rickandmortyapi.com/graphql/',
        json={'query': QUERY}
    )
    if response.status_code in range(200, 300):
        return response.json()['data']['characters']['results']


def generate_csv() -> None:
    data = query_api()
    keys = data[0].keys()

    with open('dados.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


QueryAPIGraphqlGenarateCSV = Callable[[], None]


def show_on_screen(csv: QueryAPIGraphqlGenarateCSV) -> None:
    csv()
    print(pandas.read_csv("dados.csv"))


order_food_stripe = partial(show_on_screen, csv=generate_csv)


def main() -> None:
    order_food_stripe()


if __name__ == '__main__':
    main()
