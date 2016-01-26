#!/usr/bin/python3

# solution to Exercise 1.2.3 problem #5 from "Competitive Programming 3"

class Birthdate():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day
    def __str__(self):
        return str(self.year) + '-' + str(self.month) + '-' + str(self.day)

class BirthdateSortDay(Birthdate):
    def __gt__(self, other):
        return self.day > other.day

class BirthdateSortMonth(Birthdate):
    def __gt__(self, other):
        return self.month > other.month

class BirthdateSortAge(Birthdate):
    def __gt__(self, other):
        if self.year < other.year: return True
        if self.year > other.year: return False
        if self.month < other.month: return True
        if self.month > other.month: return False
        if self.day < other.day: return True
        return False

def main():
    birthdates = []
    while True:
        s = input()
        if s == '': break
        birthdates.append(BirthdateSortMonth(s.split(' ')[2], s.split(' ')[1], s.split(' ')[0]))
    print("Sorted by month:")
    for date in sorted(birthdates): print(date)
    birthdates2 = [BirthdateSortDay(b.year, b.month, b.day) for b in birthdates]
    print("Sorted by day:")
    for date in sorted(birthdates2): print(date)
    birthdates3 = [BirthdateSortAge(b.year, b.month, b.day) for b in birthdates]
    print("Sorted by age:")
    for date in sorted(birthdates3): print(date)

if __name__=='__main__':
    main()
