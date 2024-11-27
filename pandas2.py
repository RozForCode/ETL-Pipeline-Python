import pandas as pd
sample_excel_data = pd.read_excel("Project-Management-Sample-Data.xlsx")
sample_excel_data.drop(index=[0,1,2,3,4],inplace=True, columns=["Unnamed: 0"])
sample_excel_data.reset_index(drop=True)
sample_excel_data.rename(columns={"index":"Index"},inplace=True)
sample_excel_data = sample_excel_data.reset_index(drop=True)

sample_excel_data = sample_excel_data[sample_excel_data.duplicated(['Unnamed: 3'],keep='first')]
print(sample_excel_data)


