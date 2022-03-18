from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


tmp = input("Path fichero de texto: ")
file = open(tmp)
tmp = str(input("Path excel: "))
wb = load_workbook(tmp)
ws = wb.active

if __name__ == "__main__":
    # 2 primeras lineas son nombres cols
    text = file.readline(2)
    info = ""
    row = 2
    col = 1
    while True:
        if not text:
            break
        if text == " ":
            ws[get_column_letter(col) + str(row)].value = info + ":"
            text = file.read(1)
            col = col + 1
            info = ""

        if text == "\n":
            ws[get_column_letter(col) + str(row)].value = info
            # siguiente linea y reset columna e info
            row = row + 1
            col = 1
            info = ""

        info += text
        text = file.read(1)

    # End of while, close buffer and save info excel
    file.close()
    wb.save(tmp)
    print("Proceso finalizado con éxito :D")
    input("<<<<<<Pulse cualquier tecla para finalizar>>>>>>")