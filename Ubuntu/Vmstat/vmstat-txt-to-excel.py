from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


tmp = input("Path fichero de texto: ")
file = open("C:/Users/Sergi/Desktop/VmstatMem.txt")
tmp = str(input("Path excel: "))
wb = load_workbook("C:/Users/Sergi/Desktop/Vmstat.xlsx")
ws = wb.active

if __name__ == "__main__":
    info = ""
    row = 2
    col = int(input("Columna inicio: "))
    try:
        text = file.readline()
        while True:
            if not text:
                break
            if text.isdigit():
                ws[get_column_letter(col) + str(row)].value = int(text)
                col = col + 1
            text = file.readline()
    except Exception as e:
        print(e)
        file.close()
        wb.save("C:/Users/Sergi/Desktop/Vmstat.xlsx")

    # End of while, close buffer and save info excel
    file.close()
    wb.save("C:/Users/Sergi/Desktop/Vmstat.xlsx")
    print("Proceso finalizado con éxito :D")
    input("<<<<<<Pulse cualquier tecla para finalizar>>>>>>")