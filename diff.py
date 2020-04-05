def listToDict(lst):
    op = { i : lst[i] for i in range(0, len(lst) ) }
    return op

def readFileToList(file):
    with open(file, 'r') as f: # Open the file for reading.
        data = f.read()    # Read the contents of the file into memory.
    lines = data.splitlines()   # Return a list of the lines, breaking at line boundaries.
    file_content_list = [line.replace(' ', '') for line in lines] # Replace white space from each line
    return file_content_list

file_name_1 = 'Master.xml'
file_name_2 = 'Slave.xml'
master_list = readFileToList(file_name_1)
slave_list = readFileToList(file_name_2)
diff_list = [x for x in master_list + slave_list if x not in master_list or x not in slave_list]
 
print (diff_list)   #print diff as list 
# print (listToDict(diff_list)) #print diff as dict

if not diff_list:
    print(file_name_1 + " and " + file_name_2 + " contents are same")
else:
    print(file_name_1 + " and " + file_name_2 + " contents are NOT same")

