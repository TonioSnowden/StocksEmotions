import pandas as pd
import os
import re
import json
from datetime import datetime
# set the directory path
directory = "Articles"

# initialize an empty list to store the data
data = []

# loop through each directory in the Articles directory
for subdir in os.listdir(directory):
    subdir_path = os.path.join(directory, subdir)
    if os.path.isdir(subdir_path):
        # loop through each file in the directory
        for filename in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, filename)
            if os.path.isfile(file_path) and filename.endswith(".json"):
                # read the JSON file
                with open(file_path, "r") as f:
                    json_obj = json.load(f)
                # extract the relevant information from the JSON object
                _id = json_obj["_id"]
                #name of the directory is the company name
                company = subdir
                title = json_obj["title"]
                text = json_obj["text"]
                cleaned_text = re.sub(r'<p>|</p>', '', text)
                #Change to timestamp YYYY-MM-DD HH:MM:SS
                published = json_obj["published"]
                timestamp = datetime.strptime(published, '%Y-%m-%dT%H:%M:%S.%fZ')
                data.append([_id, company, title, cleaned_text, timestamp])
        
df = pd.DataFrame(data, columns=["id", "company", "title", "text", "published"])
#drop nan values
df = df.drop_duplicates(subset=['text'], keep='first')

# Find the row with the longest text within each group
df['text_length'] = df['text'].str.len()
result = df.sort_values(by=['title', 'text_length'], ascending=[True, False]).drop_duplicates(['title', 'company'])

result = result.drop(columns=['text_length'])


df = result.sort_values(['company', 'published'])
df = df.reset_index(drop=True)
del df['id']

#print company names
company_to_ticker = {
    '3M_Company': 'MMM',
    'American_Express_co': 'AXP',
    'Amgen_Inc': 'AMGN',
    'Apple_Inc': 'AAPL',
    'Boeing_Co': 'BA',
    'Caterpillar_Inc': 'CAT',
    'Chevron_Corporation': 'CVX',
    'Cisco_Systems_Inc': 'CSCO',
    'Coca_Cola_Co': 'KO',
    'Dow_Inc': 'DOW',
    'Goldman_Sachs_Group_Inc': 'GS',
    'Home_Depot_Inc': 'HD',
    'Honeywell_International_Inc': 'HON',
    'Intel_Corporation': 'INTC',
    'International_Business_Machines_Corporation': 'IBM',
    'JPMorgan_Chase_Co': 'JPM',
    'Johnson_Johnson': 'JNJ',
    'McDonald_s_Corporation': 'MCD',
    'Merck_Co_Inc': 'MRK',
    'Microsoft_Corporation': 'MSFT',
    'Nike_Inc': 'NKE',
    'Procter_Gamble_Co': 'PG',
    'Salesforce_Inc': 'CRM',
    'The_Walt_Disney_Company': 'DIS',
    'Travelers_Companies_Inc': 'TRV',
    'Unitedhealth_Group_Incorporated': 'UNH',
    'Verizon_communications_Inc': 'VZ',
    'Visa_Inc': 'V',
    'Walgreens_Boots_Alliance_Inc': 'WBA',
    'Walmart_Inc': 'WMT'
}
#Replace company names with ticker symbols
df['company'] = df['company'].replace(company_to_ticker)

#put df in csv
df.to_csv('data/news.csv', index=False)