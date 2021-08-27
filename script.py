import os
import sys
import csv

def main():
    file_substring()

# Starter method to add another column showing whether a match occured in the csv file
def file_substring(): 
    with open('file_info.csv', 'r') as file_data:
        with open('output_file_info.csv', 'w') as file_writer:
            csv_reader = csv.reader(file_data)
            csv_writer = csv.writer(file_writer)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    # Add the column header to the file
                    row.append('Match')
                    csv_writer.writerow(row)
                    line_count += 1
                else: 
                    # Check whether a matching file substring exists
                    bucket_name = 'Hello'
                    file_name = row[0]
                    match = find_substring_match(bucket_name, file_name)
                    row.append(match)
                    csv_writer.writerow(row)
                    line_count += 1
    
# Method to find match with the substring and files
def find_substring_match(bucket_name, file_name):
    print(bucket_name, file_name)
    match_found = False

    return match_found

if __name__ == '__main__':
    main()