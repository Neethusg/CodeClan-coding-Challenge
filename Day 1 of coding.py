
# coding challenge
# Day 1/30
# code for calculating age of a person
from datetime import date

Current_year = date.today().year
# asking the person's Birth year
Birth_year = int(input('Enter your Birth year: '))

# calculating the age
Age = Current_year - Birth_year

# printing the age of the person
print(f"You are {Age} year old.")

