import requests


class HttpClient:
    """
    Generic HTTP client used by
    Automotive Knowledge providers.
    """

    def __init__(
        self,
        timeout: int = 30,
    ):

        self.session = (
            requests.Session()
        )

        self.timeout = timeout

    def get(
        self,
        url: str,
        params: dict | None = None,
        headers: dict | None = None,
    ) -> dict:

        response = self.session.get(

            url,

            params=params,

            headers=headers,

            timeout=self.timeout,

        )

        response.raise_for_status()

        return response.json()