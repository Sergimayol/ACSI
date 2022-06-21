import xlsxwriter

book = xlsxwriter.Workbook('data.xlsx')
worksheet = book.add_worksheet()


def analyze(line):
    line_content = []
    try:
        # print(line)
        line_content = line.rstrip().split(',')
        # print(line_content)
    except ValueError as e:
        print("Error: {}".format(e))
    return line_content


def writeItem(row, line):
    col = 0
    # Analyze sentence
    line_content = analyze(line)
    worksheet.write(row, col, line_content.pop(0))
    worksheet.write(row, col + 1, line_content.pop(0))
    worksheet.write(row, col + 2, line_content.pop(0))


if __name__ == '__main__':
    row = 0
    line = ""
    file = open("data.txt", "r")
    while True:
        try:
            line = file.readline()
            # EOF
            if not line:
                break
            # Write items
            writeItem(row, line)
            row += 1
        except Exception as e:
            print("Error: {}".format(e))
    book.close()
