output = open("output.txt", "w")


def analyze(line):
    try:
        if '-1' in line:
            # Not write line
            pass
    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == '__main__':
    line = ""
    file = open(str(input("Path fichero: ")), "r")
    while True:
        try:
            line = file.readline()
            # EOF
            if not line:
                break
            # Analyze sentence
            analyze(line)
        except Exception as e:
            print("Error: {}".format(e))
