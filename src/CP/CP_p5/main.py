from openpyxl import load_workbook
from openpyxl.utils import get_column_letter
import re


def line_to_excel(line):
    line_with_number = ""
    try:
        # get numbers from the line
        for i in range(len(line)):
            if line[i].isdigit():
                line_with_number += str(line[i])
    except ValueError as e:
        print("Error: {}".format(e))


def main():
    file = open("input.txt", "r")
    line = file.readline()
    while True:
        try:
            # Check EOF
            if not line:
                break
            # Check if line is valid
            line_to_excel(line)
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == '__main__':
    main()
