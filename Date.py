from dateutil import parser
import pandas as pd
from datetime import datetime
import abc
from datetime import timedelta
import dateutil.relativedelta as relativedelta


class Date(abc.ABC):

    def check_date_string(self, input_string: str) -> bool:
        """
        This function checks if the input string contains a date or not
           Parameters
        ----------
        input_string: str
                Any str
            Outputs
        -------
        bool: returns if the input string contains a date

        """
        flag = True
        try:
            flag = bool(parser.parse(input_string, fuzzy=True, dayfirst=True))
        except ValueError:
            flag = False
        return flag

    def extract_date_within_string(self, input_string: str) -> datetime:
        """
        This function extracts a date if the input string contains a recognizable date
           Parameters
        ----------
        input_string: str
                Any str
            Outputs
        -------
        datetime object: returns the datetime object if a recognizable date is present
                         within the input string
        None: when there is no recognizable date in the input string

        """
        date = None
        try:
            date = parser.parse(input_string, fuzzy=True, dayfirst=True)
        except ValueError:
            date = None
        return date

    def find_recent_datetime(self, datetimes: list[datetime]) -> datetime:
        """
        Given a list of datetime objects, return the most recent.

        parameters
        ----------
        datetimes: list[Datetime]

        Outputs
        -------
        datetime: most recent date in datetime format


        """
        most_recent_datetime = max(datetimes)

        return most_recent_datetime

    def find_oldest_datetime(self, datetimes: list[datetime]) -> datetime:
        """
        Given a list of datetime objects, return the oldest date.


        parameters
        ----------
        datetimes: list[Datetime]

        Outputs
        -------
        datetime: most oldest date in datetime format


        """
        oldest_datetime = min(datetimes)

        return oldest_datetime

    def str_to_date(self, date_str: str, str_in_format: str) -> datetime:
        """
        Given a string converts it into datetime format

        parameters
        ----------
        date_string: str
                date in string format

        Outputs
        -------
        datetime: date as datetime object


        """

        date_out = datetime.strptime(date_str, str_in_format)

        return date_out

    def date_to_str(self, date_datetime: datetime, date_in_format: str) -> str:
        """
        Given a datetime object converts it into string format

        parameters
        ----------
        date_datetime: datetime
                date as datetime object

        str_in_format: str
                format of the input date

        Outputs
        -------
        str : date in string format


        """

        str_out = date_datetime.strftime(date_in_format)

        return str_out

    def generate_dates(self, start_date: str, end_date: str, **Kwargs) -> list[datetime]:
        """

        Given start, end datetime object and relative time delta duration,
        generates dates between start and end dates.

        parameters
        ----------
        start_date: datetime
                start date as datetime object

        end_date: datetime
                end date as datetime object
        Kwargs: relative time delta arguments
                Documentation: https://dateutil.readthedocs.io/en/stable/relativedelta.html
                Need to use the plural arguments: years,months,days
                e.g years=+1 to add 1 year to start date
                    months=+1 to add 1 month to start date
                    days=+1 to add 1 day to start date

        Outputs
        -------
        list[datetime] : list of datetimes between the start and end dates

        """

        if len(Kwargs.values()) == 0:
            raise ValueError("Need to specify additional arguments for relative delta function")
        s_date = self.str_to_date(start_date, '%d-%m-%Y')

        e_date = self.str_to_date(end_date, '%d-%m-%Y')
        print(s_date, e_date)

        date_list = []

        if s_date > e_date:
            raise ValueError("Start date is beyond end date")
        else:
            current_date = s_date + relativedelta.relativedelta(**Kwargs)
            while current_date < e_date:
                date_list.append(current_date)
                current_date = current_date + relativedelta.relativedelta(**Kwargs)

        return date_list






































