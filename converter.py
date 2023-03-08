import time
import math


class Time:
    def __init__(self, type: str, value: float):
        """
                :type type: str
                :type value: float, int
                :argument type: Can be a ['nanosecond', 'microsecond', 'millisecond', 'minute', 'hour', 'day', 'week', 'month', 'year']
                :argument value: Amount of time of the specified type
            """

        self.type = type
        self.value = value
        self.convert_to_seconds = {"nanosecond": "{}/1000000000", "microsecond": "{}/1000000", "millisecond": "{}/1000",
                                   "minute": "{}*60",
                                   "hour": "{}*3600", "day": "{}*86400", "week": "{}*604800", "month": "{}*2419200",
                                   "year": "{}*31556930", "century": "{}*3155693000"}
        valid_types = list(self.convert_to_seconds.keys())

        if self.type not in valid_types:
            raise TypeError("Incorrect type to convert, please, read func doc string")

    def to_seconds(self):
        if self.type == "second":
            return self.value
        return eval(self.convert_to_seconds[self.type].format(self.value))

    def to_nanosecond(self):
        if self.type == "millisecond":
            return self.value
        return self.to_seconds() * 1000000000

    def to_microsecond(self):
        if self.type == "millisecond":
            return self.value
        return self.to_seconds() * 1000000

    def to_millisecond(self):
        if self.type == "millisecond":
            return self.value
        return self.to_seconds() * 1000

    def to_minute(self):
        if self.type == "minute":
            return self.value
        return self.to_seconds() / 60

    def to_hour(self):
        if self.type == "hour":
            return self.value
        return self.to_seconds() / 3600

    def to_day(self):
        if self.type == "day":
            return self.value
        return self.to_seconds() / 86400

    def to_week(self):
        if self.type == "week":
            return self.value
        return self.to_seconds() / 604800

    def to_month(self):
        if self.type == "month":
            return self.value
        return self.to_seconds() / 2419200

    def to_year(self):
        if self.type == "year":
            return self.value
        return self.to_seconds() / 31556926

    def to_century(self):
        if self.type == "century":
            return self.value
        return self.to_year() / 100

    def full_report(self):
        return {"nanosecond": self.to_nanosecond(), "microsecond": self.to_microsecond(),
                "millisecond": self.to_millisecond(),
                "minute": self.to_minute(),
                "hour": self.to_hour(), "day": self.to_day(), "week": self.to_week(),
                "month": self.to_month(),
                "year": self.to_year(), "century": self.to_century()}
