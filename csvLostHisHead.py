#! python
# csvLostHisHead.py - scripit in python responsible for deleting every header in every .csv file in cwd
# XI 2020 Arnold Cytrowski

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

for csv_filename in os.listdir('.'):
        if not csv_filename.endswith('.csv'):
            continue
        
        print(f'Deleting header from {csv_filename}...')

        csv_rows = []
        csv_file_object = open(csv_filename)
        reader_obj = csv.reader(csv_file_object)
        for row in reader_obj:
            if reader_obj.line_num == 1:
                continue
            csv_rows.append(row)
        csv_file_object.close()

        csv_file_object = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')
        
        csv_writer = csv.writer(csv_file_object)
        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_object.close()
