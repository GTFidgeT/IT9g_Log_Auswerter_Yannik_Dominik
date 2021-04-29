import csv
from tkinter.filedialog import askopenfilename

Filename = askopenfilename()
OpenLogfile = open(Filename, 'r')

KursCounter = 0

for row in OpenLogfile:
    KursName = row.split(';')[1]
    if 'Kurs:' in row:
        KursCounter = KursCounter + 1
        Kursvar = KursName

OpenLogfile.close()

print(KursName)
print("Kurscounter:" + str(KursCounter))
