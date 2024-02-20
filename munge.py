# place your code to clean up the data file below.
opendata = open('data/worldbank_terrorism_estimates.txt', 'r', encoding='utf_8')
listlines = opendata.readlines()
# counter for index
count = -1
for line in listlines:
    count += 1
    if line[0:7] == 'Country' and 'Series' in line:
        # deal with two word headings
        heading_list = line.split('"')
        cleaned_list = []
        for i in heading_list:
            if i.strip():
                cleaned_list += [i.strip().replace('\t', '')]
        break
heading_str = ';'.join(cleaned_list)
# save in a new file
csvfile = open('data/clean_data.csv', 'w', encoding='utf_8')
csvfile.write(heading_str + '\n')
print(heading_str)
for line in listlines[count+1:]:
    # so there is no whitespace
    if line[0:4] == "Data" or line[0:4] == "Last":
        continue
    elif line[0].isalpha() == True or line[0] == '"':
        data_line_list = line.split('"')
        cleaned_data_list = []
        for i in data_line_list:
            if i.strip():
                cleaned_data_list += [i.strip().replace('\t', '')]
        NAindex = -1
        for value in cleaned_data_list:
            NAindex += 1
            if value == 'NA':
                cleaned_data_list[NAindex] = ''
        #use tabs because commas in data
        data_line_str = ';'.join(cleaned_data_list)
        csvfile.write(data_line_str + '\n')
        print(data_line_str)
csvfile.close()
#when importing data to Excel, make sure separator is set to ';' not ','