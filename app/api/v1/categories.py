from typing import Any
from fastapi import APIRouter

router = APIRouter()


@router.get("/categories")
async def get_categories() -> Any:
    categories = [
        {"name": "DLVA", "label": "dlva"},
        {"name": "Vehicle log book", "label": "vehicle_log_book"},
        {"name": "Council tax", "label": "council"},
        {"name": "HM Revenue & Customs (HMRC)", "label": "hmrc"},
        {"name": "Electoral", "label": "electoral"},
        {"name": "Department of Works and Pensions (DWP)", "label": "dwp"},
        {"name": "Energy", "label": "energy"},
        {"name": "Water", "label": "water"},
        {"name": "NHS", "label": "nhs"},
        {"name": "TV", "label": "tv"},
        {"name": "Charity", "label": "charity"},
        {"name": "Mobile", "label": "charity"},
        {"name": "Pharmacy", "label": "pharmacy"},
        {"name": "GP", "label": "gp"},
        {"name": "Dentist", "label": "dentist"},
        {"name": "Hospital", "label": "hospital"},
        {"name": "Opticians", "label": "opticians"},
        {"name": "Breakdown", "label": "breakdown"},
        {"name": "Pets", "label": "pets"},
        {"name": "Lottery cards", "label": "lottery"},
        {"name": "Gyms", "label": "gyms"},
        {"name": "Royal Mail", "label": "royal_mail"},
        {"name": "Schools & Colleges", "label": "schools_and_colleges"},
        {"name": "Home insurance", "label": "home_insurance"},
        {"name": "Banks", "label": "banks"},
        {"name": "Inform family & friends", "label": "inform_family_friends"},
    ]
    return categories
