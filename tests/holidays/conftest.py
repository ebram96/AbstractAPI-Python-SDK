import pytest


@pytest.fixture
def holidays_sample():
    return [
        {
            "name": "June 30 Revolution",
            "name_local": "",
            "language": "",
            "description": "",
            "country": "EG",
            "location": "Egypt",
            "type": "National",
            "date": "06/30/2023",
            "date_year": "2023",
            "date_month": "06",
            "date_day": "30",
            "week_day": "Friday"
        },
        {
            "name": "Eid al-Adha Day 2",
            "name_local": "",
            "language": "",
            "description": "",
            "country": "EG",
            "location": "Egypt",
            "type": "National",
            "date": "06/30/2023",
            "date_year": "2023",
            "date_month": "06",
            "date_day": "30",
            "week_day": "Friday"
        }
    ]
