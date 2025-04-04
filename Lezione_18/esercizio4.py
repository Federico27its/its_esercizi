'''Database of dates:  Write a class that manages a database of dates with the format gg.mm.aaaa implementing methods to add a new date,
 delete a given date, modify a date, and perform a query on a given date is required.  A query on a given date allows for retrieving a given new date. 
 Note that a date is an object for your database; it must be instantiated from a string.'''

class date_db():

    def __init__(self) -> None:
        self.data = []

    def add_date(self, date: str) -> None:
        self.data.append(date)

    def del_date(self, date: str) -> None:
        if date in self.data:
            self.data.remove(date)
        else:
            raise ValueError("Date not found :(")

    def get_date(self, date: str) -> str:
        if date in self.data:
            return date
        else: raise ValueError("Date not found :(")

db = date_db()
db.add_date("27.07.1995")
print(db.data)
        