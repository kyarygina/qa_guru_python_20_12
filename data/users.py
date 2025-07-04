import dataclasses
from enum import Enum


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Hobby(Enum):
    SPORTS = "Sports"
    MUSIC = "Music"
    READING = "Reading"


class State (Enum):
    NCR = "NCR"
    UTTAR_PRADESH = "Utar Pradesh"
    HARYANA = "Haryana"
    RAJASTHAN = "Rajasthan"


@dataclasses.dataclass
class User:
    first_name: str = 'Alex'
    last_name: str = 'Ivanov'
    email: str = 'alex.iv@gmail.com'
    gender: Gender = Gender.MALE
    phone_number: str = '9050050506'
    birth_year: str = '1999'
    birth_month: str = 'June'
    birth_day: str = '18'
    subject: str = 'Physics'
    hobbies: Hobby = Hobby.MUSIC
    picture: str = 'test_file.jpg'
    address: str = 'Test Address'
    state: State = State.NCR
    city: str = 'Noida'