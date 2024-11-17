import os
import csv
import re

input_file = 'raw-web-data.txt'
output_file = 'prelim-data.csv'

try:
    input_f = open(input_file, 'r')
    output_f = open(output_file, 'w')
    current_line = input_f.readline()
    line_index = 0
    tissue_type = ''
    run = ''
    bases = ''
    download_size = ''
    accession_no = ''
    select_item_no = ''
    # Write Headers
    output_f.write('tissue_type,run,bases,download_size,accession_no,select_item_no\n')
    # Write Data
    while (current_line != ''):
        if re.match(r"^[0-9]+\.", current_line):
            line_index = 0
        # Get Tissue Type From Second Line
        elif line_index == 0:
            tissue_type = current_line.split(': ')[-1][:-1]
            line_index += 1
        #Skip Third Line
        elif line_index == 1:
            line_index += 1
        #Get DL_Size, Bases and Run From Fourth Line
        elif line_index == 2:
            current_line = current_line.split(',')
            download_size = current_line[-1].split( )[0]
            bases = current_line[-2].split( )[0]
            temp = ''.join(current_line)
            run = temp.split(': ')[1].split('spots')[0].replace(',','')
            if 'M' in run:
                run = float(run[:-2]) * 1000000

            line_index += 1
        #Skip Fifth line
        elif line_index == 3:
            line_index += 1
        #Get Accession Number from 5th Line
        elif line_index == 4:
            current_line = current_line.split()
            accession_no = current_line[-1]
            line_index += 1
        #Get Select Item Number from 5th Line
        elif line_index == 5:
            current_line = current_line.split()
            select_item_no = current_line[-1]
            output_f.write(f'{tissue_type},{run},{bases},{download_size},{accession_no},{select_item_no}\n')
            line_index += 1
        current_line = input_f.readline()
except Exception as e:
    print('error occured in parsing data', e)