""" 
Given a date string in the form Day Month Year, where:

    Day is in the set {"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}.
    Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
    Year is in the range [1900, 2100].

Convert the date string to the format YYYY-MM-DD, where:

    YYYY denotes the 4 digit year.
    MM denotes the 2 digit month.
    DD denotes the 2 digit day.

"""


class Solution:
    def reformatDate(self, date: str) -> str:
        days = {
            "1st": "01",
            "2nd": "02",
            "3rd": "03",
            "4th": "04",
            "5th": "05",
            "6th": "06",
            "7th": "07",
            "8th": "08",
            "9th": "09",
            "10th": "10",
            "11th": "11",
            "12th": "12",
            "13th": "13",
            "14th": "14",
            "15th": "15",
            "16th": "16",
            "17th": "17",
            "18th": "18",
            "19th": "19",
            "20th": "20",
            "21st": "21",
            "22nd": "22",
            "23rd": "23",
            "24th": "24",
            "25th": "25",
            "26th": "26",
            "27th": "27",
            "28th": "28",
            "29th": "29",
            "30th": "30",
            "31st": "31",
        }

        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }

        day, month, year = date.split(r" ")
        return f"{year}-{months[month]}-{days[day]}"


s = Solution()
print(s.reformatDate("20th Oct 2052"))
