import pandas as pd
from pathlib import Path
from sqlalchemy.orm import Session
from app.db import database
from app.models import models
from app.constant import constants


def load_council(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    council_data = [
        models.Council(
            gss=row["gss"],
            local_custodian_code=row["local_custodian_code"],
            slug=row["slug"],
            country_name=row["country_name"],
            homepage_url=row["homepage_url"],
            name=row["name"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(council_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading council data: {e}")
        raise


def load_nhs(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    nhs_data = [
        models.NHSOrganisation(
            ods_code=row["ODS Code"],
            organisation_type=row["Organisation Type"],
            organisation_name=row["Organisation Name"],
            address1=row["Address1"],
            address2=row["Address2"],
            address3=row["Address3"],
            city=row["City"],
            county=row["County"],
            postcode=row["Postcode"],
            telephone=row["Telephone"],
            email=row["Email"],
            website=row["Website"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(nhs_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading nhs data: {e}")
        raise


def load_optician(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    optician_data = [
        models.Optician(
            postcode=row["Postcode"],
            optician_name=row["OPTICIAN"],
            address1=row["ADDRESS_1"],
            address2=row["ADDRESS_2"],
            address3=row["ADDRESS_3"],
            address4=row["ADDRESS_4"],
            telephone_number=row["TELEPHONE_NUMBER"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(optician_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading optician data: {e}")
        raise


def load_gp_practice(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    gp_data = [
        models.GPPracticeByConstituency(
            prac_code=row["prac_code"],
            prac_name=row["prac_name"],
            address1=row["address1"],
            address2=row["address2"],
            address3=row["address3"],
            address4=row["address4"],
            address5=row["address5"],
            postcode=row["postcode"],
            phone=row["phone"],
            type=row["type"],
            x=row["X"],
            y=row["Y"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(gp_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading GP practices data: {e}")
        raise


def load_water_supply(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    water_data = [
        models.WaterSupply(
            constituency_code=row["Constituency Code"],
            constituency_name=row["Constituency Name"],
            company=row["COMPANY"],
            website=row["website"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(water_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading Water Supply data: {e}")
        raise


def load_sewerage(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    sewerage_data = [
        models.Sewerage(
            constituency_code=row["Constituency Code"],
            constituency_name=row["Constituency Name"],
            company=row["Company"],
            website=row["website"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(sewerage_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading Sewerage data: {e}")
        raise


def load_school(session: Session, csv_file: str):
    if not csv_file.exists():
        raise ValueError(f"{csv_file} does not exist.")
    df = pd.read_csv(csv_file)
    schools_data = [
        models.School(
            laname=row["LANAME"],
            schname=row["SCHNAME"],
            street=row["STREET"],
            locality=row["LOCALITY"],
            address_3=row["ADDRESS3"],
            town=row["TOWN"],
            postcode=row["POSTCODE"],
            schstatus=row["SCHSTATUS"],
            minorgroup=row["MINORGROUP"],
            school_type=row["SCHOOLTYPE"],
            is_primary=True if row["ISPRIMARY"] == 1 else False,
            is_secondary=True if row["ISSECONDARY"] == 1 else False,
            is_post16=True if row["ISPOST16"] == 1 else False,
            gender=row["GENDER"],
            relchar=row["RELCHAR"],
            admpol=row["ADMPOL"],
            ofsted_rating=row["OFSTEDRATING"],
            ofsted_last_insp=row["OFSTEDLASTINSP"],
        )
        for _, row in df.iterrows()
    ]
    try:
        session.bulk_save_objects(schools_data)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading Schools data: {e}")
        raise


def load_categories(session: Session, items: list[dict[str, str]]):
    if not items:
        raise ValueError("Category items does not exist.")
    categories = [
        models.Category(name=cat["name"], label=cat["label"]) for cat in items
    ]
    try:
        session.bulk_save_objects(categories)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"An error occurred when loading categories: {e}")
        raise


def main():
    session_generator = database.get_db()
    session = next(session_generator)

    try:
        load_categories(session, constants.CATEGORIES)

        BASE_DIR = Path(__file__).resolve().parent
        DATA_DIR = BASE_DIR / "app" / "data"

        load_council(session, DATA_DIR / "local-authorities.csv")
        load_nhs(session, DATA_DIR / "nhs_data.csv")
        load_optician(session, DATA_DIR / "opticians.csv")
        load_gp_practice(session, DATA_DIR / "gp_practices_by_constituency.csv")
        load_water_supply(session, DATA_DIR / "water_supply.csv")
        load_sewerage(session, DATA_DIR / "sewerage.csv")
        load_school(session, DATA_DIR / "england_school.csv")
    finally:
        session_generator.close()


if __name__ == "__main__":
    main()
