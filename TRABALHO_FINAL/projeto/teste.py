from CRUD_menagment import *
import random

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

