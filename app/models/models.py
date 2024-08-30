import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, BigInteger
from sqlalchemy.dialects.postgresql import UUID

# Base class for all models
Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    label = Column(String)


class MPlan(Base):
    __tablename__ = "mplan"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)


class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)


class Council(Base):
    __tablename__ = "councils"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    gss = Column(String, unique=True)
    local_custodian_code = Column(BigInteger)
    slug = Column(String, index=True)
    country_name = Column(String, index=True)
    homepage_url = Column(String)
    name = Column(String)


class NHSOrganisation(Base):
    __tablename__ = "nhs"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    ods_code = Column(String, unique=True)
    organisation_type = Column(String)
    organisation_name = Column(String)
    address1 = Column(String)
    address2 = Column(String, nullable=True)
    address3 = Column(String, nullable=True)
    city = Column(String)
    county = Column(String, nullable=True)
    postcode = Column(String)
    telephone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    website = Column(String, nullable=True)


class Optician(Base):
    __tablename__ = "opticians"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    postcode = Column(String)
    optician_name = Column(String)
    address1 = Column(String)
    address2 = Column(String, nullable=True)
    address3 = Column(String, nullable=True)
    address4 = Column(String, nullable=True)
    telephone_number = Column(String, nullable=True)


class GPPracticeByConstituency(Base):
    __tablename__ = "gp_practices_by_constituency"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    prac_code = Column(String)
    prac_name = Column(String)
    address1 = Column(String)
    address2 = Column(String, nullable=True)
    address3 = Column(String, nullable=True)
    address4 = Column(String, nullable=True)
    address5 = Column(String, nullable=True)
    postcode = Column(String)
    phone = Column(String, nullable=True)
    type = Column(String)
    x = Column(BigInteger)
    y = Column(BigInteger)


class WaterSupply(Base):
    __tablename__ = "water_supplies"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    constituency_code = Column(String)
    constituency_name = Column(String, index=True)
    company = Column(String)
    website = Column(String)


class Sewerage(Base):
    __tablename__ = "sewerages"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    constituency_code = Column(String)
    constituency_name = Column(String, index=True)
    company = Column(String)
    website = Column(String)


class School(Base):
    __tablename__ = "schools"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    laname = Column(String)
    schname = Column(String)
    street = Column(String)
    locality = Column(String, nullable=True)
    address_3 = Column(String, nullable=True)
    town = Column(String)
    postcode = Column(String)
    schstatus = Column(String)
    minorgroup = Column(String)
    school_type = Column(String)
    is_primary = Column(Boolean)
    is_secondary = Column(Boolean)
    is_post16 = Column(Boolean)
    # age_low = Column(BigInteger)
    # age_high = Column(BigInteger)
    gender = Column(String, nullable=True)
    relchar = Column(String, nullable=True)
    admpol = Column(String, nullable=True)
    ofsted_rating = Column(String, nullable=True)
    ofsted_last_insp = Column(String, nullable=True)
