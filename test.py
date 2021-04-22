train_file = "testing_file.txt" 

file_clean = open(train_file,'r+')
file_clean.truncate(0)
file_clean.close()
