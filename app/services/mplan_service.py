# from fastapi import HTTPException
from datetime import date
from app.schema.mplan_schema import MplanSchema, CreateMplanSchema


class MplanService:
    def __init__(self) -> None:
        pass

    def create_mplan(self, item: CreateMplanSchema):
        return item

    def get_mplans(self, user_id: str):
        items = [
            MplanSchema(
                id="item_1",
                moving_date=date(2024, 7, 25),
                old_address="24 Abingdon Road B242QF",
                new_address="2 Abingdon Road B242QF",
                user_id="user_1",
            ),
            MplanSchema(
                id="item_2",
                moving_date=date(2024, 7, 29),
                old_address="21 Abingdon Road B242QF",
                new_address="13 Abingdon Road B242QF",
                user_id="user_2",
            ),
            MplanSchema(
                id="item_3",
                moving_date=date(2024, 7, 25),
                old_address="24 Abingdon Road B242QF",
                new_address="2 Abingdon Road B242QF",
                user_id="user_1",
            ),
        ]
        user_items = [i for i in items if i.user_id == user_id]
        return user_items

    def get_mplan_by_id(self, id):
        item = MplanSchema(
            id=id,
            moving_date=date(2024, 7, 27),
            old_address="28 Example B26 0sq",
            new_address="18 Example B26 0sq",
        )
        return item

    def delete_mplan(self):
        pass
