import orjson as json

import aiohttp
import urllib3

from redditeasy.classes.client_data import ClientData
from redditeasy.exceptions.exceptions import RequestError


async def async_request(rtype, rfor, slash, is_auth_provided, headers=None, client_auth=None):
    if is_auth_provided:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://reddit.com/{slash}/{rfor}/{rtype}.json?limit=100", headers=headers,
                              auth=client_auth) as r:
                content = await r.json()
                return content
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://reddit.com/{slash}/{rfor}/{rtype}.json?limit=100") as r:
                content = await r.json()
                return content


def get_meme(rtype, slash, rfor, is_auth_provided, client_data: ClientData = None):
    http = urllib3.PoolManager()

    if is_auth_provided:
        header = urllib3.make_headers(
            basic_auth=f"Authorization: {client_data.client_id, client_data.client_secret}",
            user_agent=client_data.user_agent
        )

        request = http.request(
            "GET",
            f"https://www.reddit.com/{slash}/{rfor}/{rtype}.json?limit=100",
            headers=header,
        )
    else:
        request = http.request(
            "GET",
            f"https://www.reddit.com/{slash}/{rfor}/{rtype}.json?limit=100",
        )

    return json.loads(request.data.decode('utf-8'))


def check_for_api_error(response):
    if "message" in list(response.keys() if type(response) != list else response[0].keys()):
        raise RequestError(f"{response['error']} {response['message']}")
