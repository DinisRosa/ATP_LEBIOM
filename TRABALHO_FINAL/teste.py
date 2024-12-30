from projeto.Interface.main_Import_InterfaceFolder import *
import PySimpleGUI as sg
import os


base = Abrir_DataSet('DataSet_Main.json')

#print(len(base))
doiDict = all_DOI_path(base)
pdDict = all_PublishDates(base)
kwDict = all_KeyWords(base)
autDict = all_Authors(base)




print(len(base))