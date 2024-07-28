import json
# from fastapi import HTTPException


class AddressesService:
    def __init__(self) -> None:
        pass

    def get_addresses(self, post_code: str):
        with open("app/mock/postcode.json") as f:
            content = json.load(f)

        return content
