import os
import win32api
import PyInquirer 

def get_drives():
    drives = []
    string_partitii = win32api.GetLogicalDriveStrings()
    drives = list(string_partitii.split("\\\x00"))
    return drives

questions =[{
    'type' : 'list',
    'name': 'drive',
    'message': 'Ce partitie doriti sa alegeti ? ',
    'choices' : get_drives(),
},
{
    'type': 'input',
    'name': 'extensie_fisier',
    'message': 'Ce tip de fisier cauti ?',   
}]

answers = PyInquirer.prompt(questions)
print(answers)


#print (get_drives())
path = answers['drive']

try:
    file = open("fisiere.txt","a")
finally:
    try:
        for (dirpath, dirnames, filenames ) in os.walk(path):
            for filename in filenames:
                if filename.endswith("."+answers['extensie_fisier']):
                    #file.write(entry + "\n")
                    print(os.path.join(dirpath, filename))
    finally:
        file.close()
