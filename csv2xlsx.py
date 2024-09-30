import pandas as pd
import numpy as np
import csv
import xlsxwriter
import sys

csv_file = "c:/mysingle/temp/diff.csv"
# excel_file = "c:/mysingle/temp/diff.xlsx"
excel_file = "diff.xlsx"
MESSAGE_END = "- `Additional Comments` :"
REVERT = "Reverts "
FILE_DIFF = ['(M)', '(A)', '(R)', ',(M)', ',(A)', ',(R)']

if len(sys.argv) >= 2:
    csv_file = sys.argv[1]
    if 'sonosync-server' in csv_file:
        excel_file = 'sonosync-server-ChangeFileList.xlsx'
    elif 'sonosync-web' in csv_file:
        excel_file = 'sonosync-web-ChangeFileList.xlsx'

fcsv = open(csv_file, 'r', encoding='utf-8-sig')
sheet_csv = csv.reader(fcsv)
fxls = xlsxwriter.Workbook(excel_file)
sheet_xls = fxls.add_worksheet()
wrap = fxls.add_format({'text_wrap': True, 'valign': 'vcenter'})

def reformat_excel_sheet(sheet):
    sheet.set_column(0,4, 10)
    sheet.set_column(5,6, 90)

def write_line(line, y):
    # remove index==0
    index = line[0].strip()
    if index=='0':
        return
    
    for x in range(len(line)):
        sheet_xls.write(y, x, line[x], wrap)

def bypass_header(sheet):
    line = next(sheet)
    write_line(line, 0)
    
def normal_line(line):
    return len(line)==7

def first_abnormal_line(line):
    return len(line)==6

def is_file_diff(column):
    for sub_str in FILE_DIFF:
        if column.startswith(sub_str):
            return True
    return False
    
reformat_excel_sheet(sheet_xls)
bypass_header(sheet_csv)

y = 1
line = next(sheet_csv)
# index = str2int(line[0]) # assume [0] exists
while True:
    try:
        if normal_line(line):
            write_line(line, y)
            line = next(sheet_csv)
        elif first_abnormal_line(line):
            partial_line = line
            remaining_message = ''
            file_diff = ''
            line = next(sheet_csv)
            while not normal_line(line) and not first_abnormal_line(line):
                is_include_message = True
                for column in line:
                    if is_file_diff(column):
                        file_diff += column + '\n'
                        is_include_message = False
                    else:
                        remaining_message += column
                if is_include_message:
                    remaining_message += '\n'                
                line = next(sheet_csv)
            partial_line[5] += '\n' + remaining_message
            partial_line.append(file_diff.lstrip(',').rstrip('"\n'))
            write_line(partial_line,y)
        else:
            print('Something is wrong: line length =', len(line))
            break
        y += 1
    except StopIteration:
        print('End of file')
        break
        
fxls.close()
fcsv.close()
