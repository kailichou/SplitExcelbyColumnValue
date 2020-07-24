#### automate Excel using Python script
import pandas as pd
#OS module in Python provides functions for interacting with operating system. os.path used for common pathname manipulation
import os
#from openpyxl import load_workbook
#a number of high-level operations on files and collections of files, especially file copying and removal
#Warning Even the higher-level file copying functions (shutil.copy(), shutil.copy2()) cannot copy all file metadata.
from shutil import copyfile


file = input("File Path: ")
extension = os.path.splitext(file)[1]#split the path name into a pair root and ext.
filename = os.path.splitext(file)[0]
pth = os.path.dirname(file)#used to get the directory name from the specified path
newfile=os.path.join(pth, filename + '_2' + extension)
df = pd.read_excel(file)
print('columns: ' + str(df.columns.values))
colpick = input("Select Column: ")
cols = list(set(df[colpick].unique())) 
   



def sendTofile(cols):
    for i in cols:
        df[df[colpick]==i].to_excel("{}/{}.xlsx".format(pth, i), sheet_name=str(i), index=False)
    print('\nCompleted')
    print('Thanks for using the program.')
    
def sendTosheet(cols):
    copyfile(file, newfile)# Copy the content of source to destination 
    for j in cols:
        writer = pd.ExcelWriter(newfile, engine='openpyxl')
        for myname in cols:
            mydf = df.loc[df[colpick]==myname]
            mydf.to_excel(writer, sheet_name=myname, index=False)
        writer.save()
    print('\nCompleted')
    print('Thanks for using this program.')


print("Your data will split based on these values {} and create {} files or sheets based on next selection. If you are ready to proceed please type 'Y' and hit enter. Hit 'N' to exit".format(', '.join(str(cols)), len(cols)))





while True:
    x=input('Ready to Proceed [Y/N: ').lower()
    if x=='y':
        while True:
            s = input('Split into different Sheets or File (S/F): ').lower()
            if s == 'f':
                sendTofile(cols)
                break
            elif s == 's':
                sendTosheet(cols)
                break
            else: continue
        break
    elif x=='n':
        print('\nThanks for using the program.')
        break
