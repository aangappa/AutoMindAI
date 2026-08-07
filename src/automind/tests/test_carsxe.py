from automind.akr.http_client import (
    HttpClient,
)
from automind.config.settings import (
    settings,
)


def main():

    client = HttpClient()

    response = client.get(

        "https://api.carsxe.com/v1/ymm",

        params={

            "key":
                settings.CARSXE_API_KEY,

            "year":
                2024,

            "make":
                "Toyota",

            "model":
                "Hyryder",

        },

    )

    print(response)


if __name__ == "__main__":

    main()