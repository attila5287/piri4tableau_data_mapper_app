import xml.etree.ElementTree as ET
import pandas as pd
import re
from itertools import chain
import os

BASE_DIR = os.getcwd() # get current working directory
STATIC_FOLDER = 'TABLEU_DATA'
FILE_NAME = 'Scorecard_Manager ETS_702018.xml'
PATH_COMPILED = os.path.join(BASE_DIR, STATIC_FOLDER, FILE_NAME)
source = PATH_COMPILED

tree = ET.parse(source)
root = tree.getroot()

# Executive Summary Tab
ex_desc = []
kpi = []
tableau_version = []

dashboard_names = [
     element for element in root.iter('dashboard')
]
print('dashboard names/n',dashboard_names

workbook_names = [
    repo.get('id')for repo in root.iter('repository-location')
]


tableau_version = [
    child_element.get('original-version') for child_element in root.iter
]

#Ex_Description  #Kpi #Tableau version
for i in range(no_of_dashboards):
    ex_desc.append('')
    kpi.append('')
    for j in root.iter('workbook'):
        tableau_version.append(j.get('original-version'))




zip_list = zip(workbook_names,dashboard_names,ex_desc,kpi,tableau_version)

df_exec_sumry = pd.DataFrame(zip_list, columns = ['Workbook','Dashboard','Ex_Description','Key_Performance_Indicators',
                                                  'Tableau_Version'])

df_exec_sumry

from itertools import chain

# Data Source tab

workbook_names = []
dashboard_names = []
database_names = []
server_names = []
schema_names = []
table_names = []
custom_sql_query = []
datasource_alias = []
connection_type = []
zip_list = []

#Datasource caption
for i in root.iter('datasource'):
    
    if i.get('caption') is not None:
    
        datasource_alias.append(i.get('caption'))

datasource_alias = list(set(datasource_alias))
print(datasource_alias)

no_of_ds_alias = len(datasource_alias)
#Dashboard names
for i in root.iter('dashboard'):
    
    for k in range(no_of_ds_alias):
        
        dashboard_names.append(i.get('name'))

#print(dashboard_names)

# workbook names #Capture workbook names as many times as number of tables
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_ds_alias):
        
        workbook_names.append(i.get('id'))
    
#print(workbook_names)





#Server names  
for i in root.iter('named-connection'):
    
    for j in i.iter('connection'):
        for k in range(no_of_ds_alias):
            server_names.append(j.get('server'))
#print(server_names)

#Database names
for i in root.iter('named-connection'):
    for j in i.iter('connection'):
        for k in range(no_of_ds_alias):
            database_names.append(j.get('dbname'))
print(database_names)

#Schema name
for i in range(no_of_ds_alias):
    schema_names.append('')
#Table names

#Custom SQL query
for i in root.iter('connection'):
    
    for j in i.iter('relation'):

        # Custom SQL query
        if j.get('type') == 'text':

            print("Custom SQL exists!",'\n\n')
            for k in range(no_of_ds_alias):
                custom_sql_query.append(j.text)
            
            raw_query = j.text
            
            #sql_databases.append(re.findall('FROM . (.*) ',db_tbls,flags = re.IGNORECASE | re.MULTILINE |re.VERBOSE | re.DOTALL))
            database_names.append(re.findall('(\w).[dbo]',raw_query,flags = re.IGNORECASE | re.MULTILINE |re.VERBOSE))
            table_names.append(re.findall('[dbo].(\w)',raw_query,flags = re.IGNORECASE | re.MULTILINE))

            
            database_names = list(chain.from_iterable(database_names))
            table_names = list(chain.from_iterable(table_names))         
            
            print('Databases only: ',database_names,'\n\n')
            print('Tables only: ',database_names,'\n\n')

#Connection_Type
for i in range(no_of_ds_alias):
    
    connection_type.append('')
            
            
            

zip_list = zip(workbook_names,dashboard_names,server_names,database_names,schema_names,custom_sql_query,
               connection_type,datasource_alias)

df_datasource = pd.DataFrame(zip_list, columns = ['Workbook','Dashboard','Server_Name','Database_Name','Schema_Name',
                                                  'Custom SQL','Connection_Type','Data_Source_Alias'])

df_datasource

# Worksheet tab

worksheet_names = []
dashboard_names =[]
workbook_names = []

#Worksheet names

for i in root.iter('worksheet'):
    
    worksheet_names.append(i.get('name'))


no_of_worksheets = len(worksheet_names)


#Dashboard names
for i in root.iter('dashboard'):
    
    dashboard_names.append(i.get('name'))





"""  'Used' column missing from Python code. Use Rapidox  """
used = []
""" 'Add description once running code is completed  """
worksheet_desc = []

# workbook names #Capture workbook names as many times as number of tables
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_worksheets):
        
        workbook_names.append(i.get('id'))
    



for i in range(no_of_worksheets):
    
    used.append('')
    worksheet_desc.append('')


zip_list = zip(workbook_names,dashboard_names,worksheet_names,used,worksheet_desc)
zip_list

df_worksheet = pd.DataFrame(zip_list, columns = ['Workbook','Dashboard','Worksheet','Used','Worksheet_Description'])

df_worksheet

# Fields and Tables tab

# Datasource field names
datasource_field_names = []
tableau_field_names = []
measure_dimension = []
data_type = []
table_name = []
database_name = []
used = []
sql_calcs = []
aliases = []




for col_info in root.iter('column'):
    
    if col_info.find('calculation') is None:
        
        if col_info.get('caption') is not None or col_info.get('name') is not None:
        
            if col_info.get('caption') is not None:
            #print(col_info.get('caption'))
        #data.update({col_info.get('caption'):col_info.get('name')})
                tableau_field_names.append(col_info.get('caption'))
        
            else:
            #print(col_info.get('name'))
                tableau_field_names.append(col_info.get('name'))
        
            datasource_field_names.append(col_info.get('name'))
            
            measure_dimension.append(col_info.get('role'))
            
            data_type.append(col_info.get('datatype'))

            
no_of_fields = len(tableau_field_names)


workbook_names = []
# workbook names #Capture workbook names as many times as number of fields
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_fields):
        
        workbook_names.append(i.get('id'))


server_names = []
#Server names  
for i in root.iter('named-connection'):
    
    for j in i.iter('connection'):
    
        for k in range(no_of_fields):
            
            server_names.append(j.get('server'))

            
#Dashboard names
dashboard_names = []

for i in root.iter('dashboard'):
    
    dashboard_names.append(i.get('name'))
    

    
#
for i in range(no_of_fields):
    
    #table_name.append('')
    database_name.append('')
    used.append('')
    sql_calcs.append('')
    aliases.append('')
    

    
#Table names

for elem in root.iter('connection'):
    
    for relation_item in elem.iter('relation'):
        
        if relation_item.get('type') == 'table':
            
            table_name.append(relation_item.attrib['table'])

for i in table_name:

    if i.startswith('[Extract]'):
        table_name.remove(i)    
    
zip_list = zip(workbook_names,dashboard_names,tableau_field_names,datasource_field_names,table_name,database_name,
               server_names,data_type,used,measure_dimension,sql_calcs,aliases)

df_fields_tables = pd.DataFrame(zip_list, columns =  ['Workbook','Dashboard','Tableau_Field_Name','Datasource_Field_Name',
                                                      'Table_name','Database_Name','Server_Name','Data_Type','Used',
                                                      'Dimension_Measure','SQL_Calculations','Aliases'])

df_fields_tables = df_fields_tables.drop_duplicates()  #remove this if you want to capture data across worksheets and not just across workbook

df_fields_tables

#Calculated Fields tab


# ----------------------Capture calculated fields-------------------------------

calculated_field_names = []
calculated_field_formulas = []
measure_dimension = []
calc_ids = []
param_ids  = []
fields_used = []
used = []
calc_type = []

calc_captions = {}
param_captions = {}

#Function to unnest a list as a result of re operations and also filter unique values using set

def unnest_and_set(some_list):   
    unnested_lst = list(chain.from_iterable(some_list))

    unnested_lst_set = set(unnested_lst)

    lst_with_unique_elems = list(unnested_lst_set)
    
    return lst_with_unique_elems



#Capture contents of a calculat56ed field
for col_info in root.iter('column'):
    
    #Avoid capturing parameters along with calc fields
    if col_info.find('calculation') is not None and col_info.get('param-domain-type') is None:  

        if col_info.get('caption'):

            calculated_field_names.append(col_info.get('caption'))

        else:

            calculated_field_names.append(col_info.get('name'))


        for formula_info in col_info.iter('calculation'):

            calculated_field_formulas.append(formula_info.get('formula'))          

        measure_dimension.append(col_info.get('role'))

        
        
        
# Capture calculation ids inside of other calculations
for elems in calculated_field_formulas:
    
    calc_ids.append(re.findall('\[Calculation_.*?\]',elems))
    param_ids.append(re.findall('\[Parameter \d+\]',elems))    

calc_ids = unnest_and_set(calc_ids)
param_ids = unnest_and_set(param_ids)

#print(calc_ids,'\n\n')
#print(param_ids,'\n\n')


# Find the names of calculated fields corresponding to the calculation ids and create a dictionary off of it
for elem in calc_ids:
    
    for child in root.iter('column'):
        
        calc_name = child.get('name')
        calc_caption = child.get('caption')
        
        if calc_name == elem:
            
            calc_captions[elem] = calc_caption
          

            
# Find the names of parameters corresponding to the paramerer ids and create a dictionary off of it
for elem in param_ids:
    
    for child in root.iter('column'):
        
        param_name = child.get('name')
        param_caption = child.get('caption')
        
        if param_name == elem:
            
            param_captions[elem] = param_caption
    

#print(param_captions,'\n\n')    
    
#Replace calculation ids with actual names using list comprehensions
for key in calc_captions:

    calculated_field_formulas = [strs.replace(key,calc_captions[key]) for strs in calculated_field_formulas]  


    
for key in param_captions:
    
    calculated_field_formulas = [strs.replace(key,param_captions[key]) for strs in calculated_field_formulas]  


    
no_of_calc_fields = len(calculated_field_names)    
    
    
    
    
#Workbook names
workbook_names = []
# workbook names #Capture workbook names as many times as number of calc fields
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_calc_fields):
        
        workbook_names.append(i.get('id'))


#Dashboard names
dashboard_names = []

for i in root.iter('dashboard'):
    
    for k in range(no_of_calc_fields):
    
        dashboard_names.append(i.get('name'))


        
#
for i in range(no_of_calc_fields):
    
    fields_used.append('')
    used.append('')
    calc_type.append('')

# Use zip function to create a dictionary of all the three columns
calc_fields = zip(workbook_names,dashboard_names,calculated_field_names,measure_dimension,calculated_field_formulas,
                  fields_used,used,calc_type)

df_calc_fields = pd.DataFrame(calc_fields, columns =  ['Workbook','Dashboard','Calcuated_Field_Name','Tableau_Field_Type',
                                                       'Metric_Description','Fields_Used','Used','Calculation_Type'])

df_calc_fields = df_calc_fields.drop_duplicates()  #remove this if you want to capture data across worksheets and not just across workbook

df_calc_fields

# Filters tab

#Filter_name

filter_name_raw = []
filter_name = []
calc_ids = []
some_list = []
calc_captions = {}

for i in root.iter('filter'):
    
    for j in i.iter('groupfilter'):
        
        filter_name_raw.append(j.get('level'))
       
        
filter_name_raw = list(filter(None,filter_name_raw))  #remove None

filter_name_raw = list(set(filter_name_raw))  #remove duplicates

print(filter_name_raw)


for i in filter_name_raw:
    
    filter_name.append(re.findall(':(.*):',i,re.IGNORECASE))

filter_name = list(chain.from_iterable(filter_name))  #unnest the list

print(filter_name)


for i in filter_name:
    
    if i.startswith('Calculation'):
        
        i = '['+i+']'   #Add '[] to calculation id to match exactly while searching'
        calc_ids.append(i)

print(calc_ids)


# Find the names of calculated fields corresponding to the calculation ids and create a dictionary off of it
for elem in calc_ids:
    
    for child in root.iter('column'):
        
        calc_name = child.get('name')
        calc_caption = child.get('caption')
        
        if calc_name == elem:
            
            calc_captions[elem] = calc_caption
            
            
print(calc_captions)

for key in calc_captions:        

    calc_ids = [strs.replace(key,calc_captions[key]) for strs in calc_ids]

print(calc_ids)


#calc_captions = {k

for key in calc_captions:

    if key.startswith('['):
        
        key = key[1:-1]

print(calc_captions)
        
for key in calc_captions:        

    filter_name = [strs.replace(key,calc_captions[key]) for strs in filter_name]
    
    
print(filter_name)    
#for i in filter_name:
    
    #calc_ids.append(re.findall('\[Calculation_.*?\]',elems))
    
no_of_filters = len(filter_name)

#Workbook names
workbook_names = []
# workbook names #Capture workbook names as many times as number of calc fields
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_filters):
        
        workbook_names.append(i.get('id'))


#Dashboard names
dashboard_names = []

for i in root.iter('dashboard'):
    
    for k in range(no_of_filters):
    
        dashboard_names.append(i.get('name'))
        
zip_list = zip(workbook_names,dashboard_names,filter_name)

df_filters = pd.DataFrame(zip_list, columns =  ['Workbook','Dashboard','Filter_Name'])

df_filters = df_filters.drop_duplicates()  #remove this if you want to capture data across worksheets and not just across workbook

df_filters       

# Actions tab

action_names = []
source_sheet = []
target_sheet = []
run_action_on = []

#Action Data
for i in root.iter('action'):
    
    action_names.append(i.get('caption'))


    for j in i.iter('source'):
        
        source_sheet.append(j.get('worksheet'))
        target_sheet.append(j.get('worksheet'))
    
    for j in i.iter('activation'):
        
        run_action_on.append(j.get('type'))
    
    
no_of_actions = len(action_names)    
    
#Workbook names
workbook_names = []
# workbook names #Capture workbook names as many times as number of calc fields
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_actions):
        
        workbook_names.append(i.get('id'))
        

#Dashboard names
dashboard_names = []

for i in root.iter('dashboard'):
    
    for k in range(no_of_actions):
    
        dashboard_names.append(i.get('name'))
        
        

# Use zip function to create a dictionary of all columns
zip_list = zip(workbook_names,dashboard_names,action_names,source_sheet,target_sheet,run_action_on)

df_actions = pd.DataFrame(zip_list, columns =  ['Workbook','Dashboard','Action_Name','Source_Sheet',
                                                    'Target_Sheet','Run_Action_On'])

df_actions = df_actions.drop_duplicates()  #remove this if you want to capture data across worksheets and not just across workbook

df_actions

# Parameters

parameter_name = []
data_type = []
allowable_value_type = []
current_value = []

for param in root.iter('column'):
    
    if param.get('param-domain-type') is not None:
        
        parameter_name.append(param.get('caption'))
        data_type.append(param.get('datatype'))
        allowable_value_type.append(param.get('param-domain-type'))
    
#print(parameter_name)


no_of_params = len(parameter_name)



#Workbook names
workbook_names = []
# workbook names #Capture workbook names as many times as number of calc fields
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_params):
        
        workbook_names.append(i.get('id'))
        

#Dashboard names
dashboard_names = []

for i in root.iter('dashboard'):
    
    for k in range(no_of_params):
    
        dashboard_names.append(i.get('name'))
        
        

zip_list = zip(workbook_names, dashboard_names, parameter_name, data_type, allowable_value_type)

df_parameters = pd.DataFrame(zip_list, columns = ['Workbook','Dashboard','Parameter_Name','Data_Type',
                                                  'Allowable_Value_Type'])

df_parameters = df_parameters.drop_duplicates()

df_parameters

# Refresh Schedule tab

ref_sched = []
ref_type = []
ref_output_type = []

#Workbook names
workbook_names = []
# workbook names #Capture workbook names as many times as number of calc fields
for i in root[1].iter('repository-location'):
    
    for k in range(no_of_params):
        
        workbook_names.append(i.get('id'))

        
        
#Datasource caption
for i in root.iter('datasource'):
    
    if i.get('caption') is not None:
    
        for j in range(len(dashboard_names)):
            datasource_alias.append(i.get('caption'))
            
            
for i in range(len(workbook_names)):
    
    ref_sched.append('')
    ref_type.append('')
    ref_output_type.append('')
    
zip_list = zip(workbook_names, ref_type, ref_sched, datasource_alias, ref_output_type)

df_refresh_schedule = pd.DataFrame(zip_list, columns = ['Workbook','Refresh_Type','Refresh_Schedule','Data_Source',
                                                  'Refresh_Type'])

df_refresh_schedule = df_refresh_schedule.drop_duplicates()

df_refresh_schedule

#Unused fileds tab


#Workbook names
workbook_names = []
# workbook names #Capture workbook names as many times as number of calc fields
for i in root[1].iter('repository-location'):
    
    #for k in range(no_of_params):
        
    workbook_names.append(i.get('id'))

        


#Datasource caption
for i in root.iter('datasource'):
    
    if i.get('caption') is not None:
    
        for j in range(len(workbook_names)):
            datasource_alias.append(i.get('caption'))
            
            
            
            
#Dashboard names
dashboard_names = []

for i in root.iter('dashboard'):
    
    for k in range(len(workbook_names)):
    
        dashboard_names.append(i.get('name'))
        
        
tableau_field_name = []
field_type = []

for i in range(len(workbook_names)):
    
    tableau_field_name.append('')
    field_type.append('')
    
    
zip_list = zip(workbook_names, dashboard_names, datasource_alias, tableau_field_name, field_type)

df_unused_fields = pd.DataFrame(zip_list, columns = ['Workbook','Dashboard','Data_Source_Alias','Tableau_Field_Name',
                                                  'Field_Type_Type'])

df_unused_fields = df_unused_fields.drop_duplicates()

df_unused_fields

#----------------- Write to excel---------------------

excel_path = input("Enter path and output file name with xlsx extension: ")

#path = 'C:\\Users\\aoak799\Desktop\Python output files\'

df_exec_sumry.to_excel(excel_path, sheet_name = 'Exexutive Summary')

with pd.ExcelWriter(excel_path, engine='openpyxl', mode='a') as writer:
    df_datasource.to_excel(writer, sheet_name = 'Data Source')        #Write to specific location
    df_worksheet.to_excel(writer, sheet_name = 'Worksheet')
    df_fields_tables.to_excel(writer, sheet_name = 'Fields and Tables')
    df_calc_fields.to_excel(writer, sheet_name = 'Calculated Fields')
    df_filters.to_excel(writer, sheet_name = 'Filters')
    df_actions.to_excel(writer, sheet_name = 'Actions')
    df_parameters.to_excel(writer, sheet_name = 'Parameters')
    df_refresh_schedule.to_excel(writer, sheet_name = 'Refresh Schedule')
    df_unused_fields.to_excel(writer, sheet_name = 'Unused Fields')
    