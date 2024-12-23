from CRUD_menagment import *
from DataSet_SaveLoad import *
from DataSet_Subdivision import *
from Add_Post import *


base = Abrir_DataSet('DataSet_Main.json')

print(len(base))

#idxPost(base)

'''
DOIs = []
for i in base:
    DOIs.append(i['doi'][29:])


print(DOIs)
print(len(DOIs))    
'''

'''
dois = all_PublishDates(base)
print(dois)'''


print(len(all_Authors(base)))

print(all_KeyWords(base))