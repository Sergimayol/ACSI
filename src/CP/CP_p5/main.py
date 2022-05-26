# from openpyxl import load_workbook
# from openpyxl.utils import get_column_letter
# import re


# def line_to_excel(line):
#     line_with_number = ""
#     try:

#     except ValueError as e:
#         print("Error: {}".format(e))


def main():
    file = open("input.txt", "r")
    line = ""
    res = ""
    while True:
        try:
            line = file.read(5)
            # Check EOF
            if not line:
                break
            # Check if line is valid
            # line_to_excel(line)
            while True:
                line = file.read(1)
                if line == ",":
                    file.read(1)
                    break
                res += line
            print("X1: {}".format(res))
            res = ""
            while True:
                line = file.read(1)
                if line == "]":
                    break
                res += line
            print("X2: {}".format(res))
            res = ""
            # Next line
            file.read(1)
            line = file.read(5)
            while True:
                line = file.read(1)
                if line == ",":
                    file.read(1)
                    break
                res += line
            print("N1: {}".format(res))
            res = ""
            while True:
                line = file.read(1)
                if line == "]":
                    break
                res += line
            print("N2: {}".format(res))
            res = ""
            # Next line
            file.read(1)
            line = file.read(5)
            while True:
                line = file.read(1)
                if line == ",":
                    file.read(1)
                    break
                res += line
            print("R1: {}".format(res))
            res = ""
            while True:
                line = file.read(1)
                if line == "]":
                    break
                res += line
            print("R2: {}".format(res))
            res = ""
            # Next line
            file.read(1)
            line = file.read(5)
            while True:
                line = file.read(1)
                if line == ",":
                    file.read(1)
                    break
                res += line
            print("U1: {}".format(res))
            res = ""
            while True:
                line = file.read(1)
                if line == "]":
                    break
                res += line
            print("U2: {}".format(res))
            res = ""
            # Next line
            file.read(1)
            file.readline()
            file.readline()
        except Exception as e:
            print("Error: {}".format(e))


if __name__ == '__main__':
    main()
