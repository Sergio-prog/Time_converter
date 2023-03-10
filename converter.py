import datetime
from typing import Union, Optional

__version__ = "0.6a"


class Time:
    def __init__(self, _type: str = "second", value: Union[float, int, datetime.timedelta] = 0):
        """
                :type _type: str
                :type value: float, int
                :argument _type: Can be a ['nanosecond', 'microsecond', 'millisecond', 'minute', 'hour', 'day', 'week', 'month', 'year', 'century]
                :argument value: Amount of time of the specified type
            """

        self.type = _type.lower()
        self.value = value.total_seconds() if type(value) == datetime.timedelta else value
        self.convert_to_seconds = {"nanosecond": "{}/1000000000", "microsecond": "{}/1000000", "millisecond": "{}/1000",
                                   "minute": "{}*60",
                                   "hour": "{}*3600", "day": "{}*86400", "week": "{}*604800", "month": "{}*2419200",
                                   "year": "{}*31556930", "century": "{}*3155693000", "second": "{}"}
        valid_types = list(self.convert_to_seconds.keys())

        if self.type not in valid_types:
            raise TypeError("Incorrect type to convert, please, read func doc string.")
        
        if self.type != "second" and type(value) == datetime.timedelta:
            raise TypeError("Incorrect attributes types, you can not use '_type' and 'datetime.timedelta' value.")

    def to_seconds(self) -> float:
        if self.type == "second":
            return self.value
        return eval(self.convert_to_seconds[self.type].format(self.value))

    def to_nanosecond(self) -> float:
        if self.type == "nanosecond":
            return self.value
        return self.to_seconds() * 1000000000

    def to_microsecond(self) -> float:
        if self.type == "microsecond":
            return self.value
        return self.to_seconds() * 1000000

    def to_millisecond(self) -> float:
        if self.type == "millisecond":
            return self.value
        return self.to_seconds() * 1000

    def to_minute(self) -> float:
        if self.type == "minute":
            return self.value
        return self.to_seconds() / 60

    def to_hour(self) -> float:
        if self.type == "hour":
            return self.value
        return self.to_seconds() / 3600

    def to_day(self) -> float:
        if self.type == "day":
            return self.value
        return self.to_seconds() / 86400

    def to_week(self) -> float:
        if self.type == "week":
            return self.value
        return self.to_seconds() / 604800

    def to_month(self) -> float:
        if self.type == "month":
            return self.value
        return self.to_seconds() / 2419200

    def to_year(self) -> float:
        if self.type == "year":
            return self.value
        return self.to_seconds() / 31556926

    def to_century(self) -> float:
        if self.type == "century":
            return self.value
        return self.to_year() / 100

    def __str__(self):
        return "{} {}s".format(str(self.value), str(self.type))

    def full_report(self):
        return {"nanosecond": self.to_nanosecond(), "microsecond": self.to_microsecond(),
                "millisecond": self.to_millisecond(),
                "second": self.to_seconds(),
                "minute": self.to_minute(),
                "hour": self.to_hour(), "day": self.to_day(), "week": self.to_week(),
                "month": self.to_month(),
                "year": self.to_year(), "century": self.to_century()}

    @property
    def timedelta_object(self):
        return datetime.timedelta(seconds=self.to_seconds())


if __name__ == "__main__":
    t = datetime.timedelta(seconds=15, minutes=9)
    s = Time(_type="week", value=5)
    print(s.full_report())
