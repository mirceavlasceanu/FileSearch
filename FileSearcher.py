import os
import win32api
import PyInquirer
import shutil
import datetime

#aduce data curenta
now = datetime.datetime.now()
#nume fisier temporar
filepath = 'temp.txt'

#aducem driverele din calculator
def get_drives():
    drives = []
    string_partitii = win32api.GetLogicalDriveStrings()
    drives = list(string_partitii.split("\\\x00"))
    return drives

def create_folder(path):
    os.mkdir(path)

def copiere_fisiere():
    with open(filepath,'r') as fp:
        lines = fp.read().splitlines()
        for line in lines:
            newPath = shutil.copy(str(line), d_path)
    file.close()

def curata_fisier(file):
    open(file, 'w').close()


#partea de interactiune cu utilizatorul
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
},
{
    'type': 'list',
    'name': 'copiere',
    'message': 'Vrei sa copiezi fisierele ?',
    'choices' : ['DA', 'NU'],
}]
answers = PyInquirer.prompt(questions)
print(answers)

#creaza fisierul cu raspunsuri
path = answers['drive']
#calea fisierelor daca se doreste copierea
d_path = ("H:\\TESTE FISIERE\\" 
         + answers['extensie_fisier'] 
         + now.strftime("%Y-%m-%d %H_%M"))

curata_fisier(filepath)
try:
    file = open("temp.txt","a")
finally:
    try:
        for (dirpath, dirnames, filenames ) in os.walk(path):
            for filename in filenames:
                if filename.endswith("."+answers['extensie_fisier']):
                    file.write(os.path.join(dirpath, filename) + "\n")
    finally:
        file.close()

print ("fisierul rezultat a fost creat")


if answers['copiere'] == 'DA':
    create_folder(d_path)
    copiere_fisiere()
else:
    os.startfile(filepath)