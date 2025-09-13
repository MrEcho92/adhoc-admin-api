from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime
from uuid import UUID


class MplanCategory(BaseModel):
    label: str
    is_completed: bool = False

    class Config:
        from_attributes = True


class MplanBaseSchema(BaseModel):
    moving_date: date
    old_address: str
    new_address: str
    selected_categories: list[MplanCategory] = []
    created_at: datetime = None
    modified_at: datetime = None
    user_id: UUID

    class Config:
        from_attributes = True


class MplanSchema(MplanBaseSchema):
    id: UUID


class MplanSchemaCreate(MplanBaseSchema):
    pass


class CouncilResponse(BaseModel):
    id: int
    gss: str
    local_custodian_code: Optional[int]
    slug: str
    country_name: str
    homepage_url: str
    name: str


class NhsSchemaResponse(BaseModel):
    id: int
    ods_code: str
    organisation_type: str
    organisation_name: str
    address1: str
    address2: str
    address3: str
    city: str
    county: str
    postcode: str
    telephone: str
    email: str
    website: str


class GPSchemaResponse(BaseModel):
    id: int
    prac_code: str
    prac_name: str
    address1: str
    address2: str
    address3: str
    address4: str
    address5: str
    postcode: str
    phone: str
    type: str
    x: int
    y: int


class WaterSewageSchema(BaseModel):
    id: int
    constituency_code: str
    constituency_name: str
    company: str
    website: str


class SchoolSchema(BaseModel):
    id: int
    laname: str
    schname: str
    street: str
    locality: str
    address_3: str
    town: str
    postcode: str
    schstatus: str
    minorgroup: str
    school_type: str
    is_primary: bool
    is_secondary: bool
    is_post16: bool
    gender: str
    relchar: str
    admpol: str
    ofsted_rating: str
    ofsted_last_insp: str


class MplanDetailSchema(BaseModel):
    mplan: MplanBaseSchema
    councils: list[CouncilResponse] = None
    gp: list[GPSchemaResponse] = None
    water: list[WaterSewageSchema] = None
    sewages: list[WaterSewageSchema] = None
    schools: list[SchoolSchema] = None
    gpbranch: list[NhsSchemaResponse] = None
    pharmacy: list[NhsSchemaResponse] = None
    hospital: list[NhsSchemaResponse] = None
    dentist: list[NhsSchemaResponse] = None
