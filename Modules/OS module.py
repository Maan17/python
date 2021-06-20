import os
print("Name of the operating system is:",os.name)
print("Current Working Directory(CWD) of the file is:",os.getcwd())

#raidsing OSError
try:
    #if the file doesn't exist then it would throw an error
    filename='GFG.txt'
    f=open(filename,'rU')
    text=f.read()
    f.close()

#Control panel directly jumps to here if any of the above lines throws IOError
except IOError:
    #print(os.error) will <class 'OSError'>
    print('Problem reading: ',filename)

#in any case the code then continues with the line after try/except    

fd="GFG.txt"
#popen() provides a pipe/gateway and accesses the file directly
file=os.popen(fd,'w')
file.write("Hello")

#closing a file opened by popen()
os.close("GFG.txt")

#renaming a file
os.rename(fd,'New.txt')
