from datetime import datetime
from typing import Final

MAX_AGE: Final[int] = 100
MIN_AGE: Final[int] = 0


class User:

    name: str
    email: str
    picture: str
    birthdate: datetime

    def __init__(self, name: str, email: str, picture: str, birthdate: str) -> None:
        self.name = name
        self.email = email
        self.picture = picture
        self.birthdate = datetime.strptime(birthdate, "%Y-%m-%d")

    def validate_birth_date(self) -> bool:
        """
        Validate birth date from user input:

        constraints:
        - year must be less than 100
        - year must be greater than 0
        """

        date_today: datetime = datetime.today()
        date_comparison_year = date_today.year - self.birthdate.year

        return (date_comparison_year < MAX_AGE) and (date_comparison_year > MIN_AGE)
