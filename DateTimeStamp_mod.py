import datetime


class DateTimestampGenerator():
    def __init__(self):
        self.current_time = datetime.datetime.now()
        self.current_time = datetime.datetime.strftime(self.current_time, format='%H:%M:%S hrs Local')
        self.current_date = datetime.datetime.today()
        self.current_date = datetime.datetime.strftime(self.current_date, format='%A, %d %B %Y')
        self.zulu = datetime.datetime.utcnow()
        self.zulu_time = datetime.datetime.strftime(self.zulu, format='%H:%M:%S hrs UTC')
        self.zulu_date = datetime.datetime.strftime(self.zulu, format='%A, %d %B %Y')

    def generate_timestamp(self):
        timestamp = self.current_time
        return timestamp

    def generate_datestamp(self):
        datestamp = self.current_date
        return datestamp

    def generate_utc_time(self):
        utc_time = self.zulu_time
        return utc_time

    def generate_utc_date(self):
        utc_date = self.zulu_date
        return utc_date


def main():
    dt = DateTimestampGenerator()
    time = dt.generate_timestamp()
    date = dt.generate_datestamp()
    utc_time = dt.generate_utc_time()
    utc_date = dt.generate_utc_date()
    print(f"{utc_date} - {utc_time}\n{date} - {time}")


if __name__ == '__main__':
    main()
