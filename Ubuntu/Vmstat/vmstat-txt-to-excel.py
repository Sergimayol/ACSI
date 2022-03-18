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
    # aqui ya viene la info
