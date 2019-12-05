# !/usr/bin/env python3

# Created by: Manuel Garcia Yuste
# Created on : December 2019
# This program converts the time


import constants


def main():
    # Input
    days = int(input("Enter number of Days: "))
    hours = int(input("Enter number of Hours: "))
    minutes = int(input("Enter number of Minutes: "))
    seconds = int(input("Enter number of Seconds: "))

    # Output
    total_seconds = days * (constants.SECONDS_PER_DAY)
    total_seconds = total_seconds + (hours * (constants.SECONDS_PER_HOUR))
    total_seconds = total_seconds + (minutes * (constants.SECONDS_PER_MINUTE))
    total_seconds = total_seconds + seconds

    # Output
    print("Total number of seconds: ", "%d" % (total_seconds))


if __name__ == "__main__":
    main()
