import pandas as pd
from openpyxl import load_workbook
import numpy as np

#Read Excel file
def read_archive(fil):    
    reader = pd.read_excel(fil, sheet_name=None, index_col=0)#, sheet_name="aula")#estudiante,aula, docente,curso,programa,departamento
    #sheets=reader.sheet_names
    #print(sheets)
    return reader

#deletes the duplicated rows in file
def del_duplicated(in_f,out_f):
    list_l = []
    count = 0
    with open(in_f,'r') as f:#, open(out_f,'w') as f_out:
        reader = pd.read_csv(f)
        for row in reader.iterrows(): #in reader
            print("ROW: {} END ROW!!!".format(row)) 
            count += 1
            if row in list_l:
                continue

            else:
                list_l.append(row)
                #f_out.write(row)#writer.writerow(row)
    print(count)
    print(len(list_l))

#delete the blank rows in file
def del_blank_rows(data):
    print(data)
    data.dropna(thresh=2, inplace=True)#how='all'
    print(data)
    data.ffill(inplace=True)
    return data

#delete the blank cols in file
def del_blank_cols(data):
    data.dropna(how='all', inplace=True, axis='columns')#how='all'
    data.ffill(inplace=True)
    return data

#All first letters mayusc
def capitali(data):
    types=data.dtypes
    data=pd.concat([data[col].astype(str).str.capitalize() for col in data.columns], axis=1)
    data=data.astype(dtype=types)
    
    return data

#first name letter mayusc
def name_mayusc(data):
    
    nam='nombre_est'
    nam2='nombre_docente'
    if {nam}.issubset(data.columns):
        data[nam]=data[nam].astype(str).str.title()
    else:
        if {nam2}.issubset(data.columns):
            data[nam2]=data[nam2].astype(str).str.title()

    return data

#remove accents
def remove_accents(data):
    cols = data.select_dtypes(include=[np.object]).columns
    data[cols] = data[cols].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
    return data
    #return unidecode.unidecode(data.decode('utf-8'))

#clean file
def clean(fil):
    worksheet=read_archive(fil)
    for sheet in worksheet:
        data=worksheet[sheet]
        data=del_blank_cols(data)
        data=del_blank_rows(data)
        data=capitali(data)
        data=name_mayusc(data)
        data=remove_accents(data)
        worksheet[sheet]=data
        #new_sheet(fil,sheet,data)
    return worksheet

#creates new sheet in an existing excel file
def new_sheet(fil,sheet,data):
    sheetnam='{}_clean'.format(sheet)
    print(sheetnam)

    book = load_workbook(fil)
    writer = pd.ExcelWriter(fil, engine='openpyxl')
    writer.book = book
    data.to_excel(writer,sheet_name=sheetnam)
    writer.save()   

#Creates new workspread with clean data
def new_workspread(out_file, worksheet):
    writer = pd.ExcelWriter(out_file, engine='openpyxl')
    for sheet in worksheet:
        worksheet[sheet].to_excel(writer,sheet_name=sheet)

    writer.save()


if __name__ == '__main__':
    in_f = 'Resources/Gobierno.csv'
    in_f2 = 'Resources/Fundacion.csv'
    in_f3 = r'C:/COURSERA/Analisis de datos/tabla_estudiante.xlsx'
    out_f3 = r'C:/COURSERA/Analisis de datos/tabla_estudiante_clean.xlsx'
    
    worksheet=clean(in_f3)
    new_workspread(out_f3,worksheet)
    #print(data.dtypes)
    #del_duplicated(in_f,out_f)