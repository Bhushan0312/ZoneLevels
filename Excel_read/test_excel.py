import openpyxl

xl = openpyxl.load_workbook("ZONE LEVELS_223.xlsx")

for i in xl.sheetnames:
    print(i)
    if i == 'Sheet1':
        sh = xl[i]
        sh.sheet_state = 'hidden'

        ws.protection.set_password('Test')
        ws.protection.sheet = True
        ws.protection.enable()



xl.save(filename="ZONE LEVELS.xlsx")
