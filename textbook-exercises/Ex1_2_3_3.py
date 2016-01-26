#!/usr/bin/python3

# solution to Exercise 1.2.3 problem #3 from "Competitive Programming 3"

from datetime import datetime

date = datetime.strptime(input(), '%d %B %Y')
print(date.strftime('%A'))
