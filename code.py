import pandas as pd
import os

#Creating a sample dataframe through pandas library
data = {
    'Name' : ['Saransh', 'Rajat', 'Kanika'],
    'Age' : [21, 23, 20],
    'State' : ['Uttar Pradesh', 'Rajasthan', 'Maharashtra']
}

df = pd.DataFrame(data)

#---------------------------------------------------------------

#Adding new row for second version
new_row_loc = {'Name': 'Niharika', 'Age' : 22, 'State' : 'Delhi'}
df.loc[len(df.index)] = new_row_loc

#Ensuring the data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

#Define the file path
file_path = os.path.join(data_dir, 'sample_data.csv')

#Saving the dataframe to a csv file 
df.to_csv(file_path, index=False)

print("Data added successfully")


