from HelperFunctions import *
from DataSet_SaveLoad import *
from DataSet_Subdivision import *
from Add_Post import *


base = Abrir_DataSet('DataSet_Main.json')

#print(len(base))
doiDict = all_DOI_path(base)
pdDict = all_PublishDates(base)     
kwDict = all_KeyWords(base) 
autDict = all_Authors(base) 



'''
a = idxPost(doiDict, pdDict, kwDict, autDict)
print(a)
'''
#print(kwDict)


ApagarPost(base, [1,2,3])
