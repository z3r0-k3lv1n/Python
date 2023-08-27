import datetime


class DateTimestampGenerator:
    def __init__(self):
        # Initialize the generator with current local time, date, and UTC time.
        self.current_time = datetime.datetime.now().strftime('%H:%M:%S hrs Local')
        self.current_date = datetime.datetime.today().strftime('%A, %d %B %Y')
        self.zulu_time = datetime.datetime.utcnow().strftime('%H:%M:%S hrs UTC')
        self.zulu_date = datetime.datetime.utcnow().strftime('%A, %d %B %Y')

    def generate_timestamp(self):
        """
        Generate and return the current local timestamp. Formatted in 'HH:MM:SS hrs Local'.
        """
        return self.current_time

    def generate_datestamp(self):
        """
        Generate and return the current local datestamp. Formatted in 'Sunday, 27 August 2023'.
        """
        return self.current_date

    def generate_utc_time(self):
        """
        Generate and return the current UTC time. Formatted in 'HH:MM:SS hrs UTC'.
        """
        return self.zulu_time

    def generate_utc_date(self):
        """
        Generate and return the current UTC date. Formatted in 'Sunday, 27 August 2023'.
        """
        return self.zulu_date


def main():
    # Create an instance of DateTimestampGenerator.
    dt = DateTimestampGenerator()

    # Generate timestamps and datestamps.
    time = dt.generate_timestamp()
    date = dt.generate_datestamp()
    utc_time = dt.generate_utc_time()
    utc_date = dt.generate_utc_date()

    # Print the generated information.
    print(f"{utc_date} - {utc_time}\n{date} - {time}")


if __name__ == '__main__':
    main()
