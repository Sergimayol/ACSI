output = open("output.txt", "w")


def analyze(line):
    try:
        if '-1' in line:
            # Not write line
            pass
        else:
            if '\t' in line:
                line = line.replace('\t', ",")
            if line.count(",") > 2:
                # recorrer linea y borrar las "," restantes
                res = 0
                aux = ""
                for i in range(len(line)):
                    if "," in line[i]:
                        res += 1
                    if res <= 2:
                        aux += line[i]
            aux += "\n"
            output.write(aux)
    except ValueError as e:
        print("Error: {}".format(e))


if __name__ == '__main__':
    line = ""
    file = open("data.txt", "r")
    limite = 0
    output.write(file.readline())
    while True:
        try:
            line = file.readline()
            # EOF
            if not line:
                break
            # Analyze sentence
            # if limite == 10:
            #     break
            limite += 1
            analyze(line)
        except Exception as e:
            print("Error: {}".format(e))
