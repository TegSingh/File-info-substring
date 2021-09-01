import os
import sys
import csv
import timeit

# Set the bucket name for all the file names to compare against
bucket_name = "com.ibm.ws.microprofile.config.1.1_fat"

def main():
    start = timeit.default_timer()
    file_substring()
    end = timeit.default_timer()
    printstring = "Execution time: " + str(end - start) + " seconds"
    print(printstring)

    # Test the find_common_substring method
    string1 = "com.ibm.ws"
    string2 = "com.ibm.ws.microprofile.config"
    print(find_common_substring(string1, string2))

# Starter method to add another column showing whether a match occured in the csv file
def file_substring(): 
    with open('file_info.csv', 'r') as file_data:
        with open('output_file_info.csv', 'w') as file_writer:
            csv_reader = csv.reader(file_data)
            csv_writer = csv.writer(file_writer)
            line_count = 0
            for row in csv_reader:
                # print(row)
                if line_count < 200000: 
                    if line_count == 0:
                        # Add the column header to the file
                        row.append('Match')
                        csv_writer.writerow(row)
                        line_count += 1
                    else: 
                        # Check whether a matching file substring exists
                        file_name = row[0]
                        # print("Hello1")
                        match = find_substring_match(bucket_name, file_name)
                        row.append(match)
                        csv_writer.writerow(row)
                        line_count += 1
                else:
                    break
    
# Method to find match with the substring and files
def find_substring_match(bucket_name, file_name):
    # Intialize the match value to false
    match = False
    # Split string based on /
    split_string = file_name.split('/')
    for i in range(len(split_string)):
        # Give priority to the files that are in dev directory
        if split_string[0] == 'dev':
            match, matchstring = find_common_substring(bucket_name, split_string[1])
    
    return match

# Method to find the longest common substring between 2 substrings (starting at index 0) passed as arguments
def find_common_substring(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    j = 0    
    common = ""
    # print(string1, string2)
    for i in range(l1):
        # print("BucketName: ", string1[i], "Filename: ", string2[j])
        if i == j:
            if string1[i] == string2[j]:
                j += 1
                if j >= len(string2):
                    break
                # Add the matching string to the value for common
                common += string1[i]
            else:
                break
        else: 
            break   

    # If the length of bucket name and file name end up being a perfect match
    if len(common) == len(string1) or len(common) == len(string2):
        return True, common
    # If common ends with ., only then return true
    elif common != "" and common[len(common) - 1] == '.':
        return True, common
    else:
        return False, "" 
    

if __name__ == '__main__':
    main()