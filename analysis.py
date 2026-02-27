import pandas as pd
import matplotlib.pyplot as plt
import requests
import io
try:
    url = "https://data.cityofnewyork.us/resource/tqtj-sjs8.csv?$limit=10000"
    response = requests.get(url)
    if response.status_code == 200:
      column_types = {
          'boroughname': str,
          'PermitNumber': str,
          'ZipCode': str,
          'permitstatusid': str,
          'equipmenttypedesc': str
          }
      df = pd.read_csv(io.StringIO(response.text), dtype=column_types, low_memory=False)
      print("Successfully pulled live data from NYC Open Data!")
      print(df.head())
      print("---ALL COLUMN NAMES---")
      print(df.columns.tolist())
      df['boroughname'] = df['boroughname'].str.strip().str.upper()
      df = df.dropna(subset=['boroughname'])
      print("--- CLEANED BOROUGHS FOUND ---")
      print(df['boroughname'].unique())
      borough_counts = df['boroughname'].value_counts()
      print("---- CONSTRUCTION PERMIT COUNTS BY BOROUGH ---")
      print(borough_counts)
      top_borough = borough_counts.index[0]
      count = borough_counts.iloc[0]
      print(f"\nThe 'Construction King' is {top_borough} with {count} permits. ")
      plt.figure(figsize=(10,6))
      borough_counts.plot(kind='bar', color = 'skyblue', edgecolor='black')
      plt.title('Construction Permits by Borough',fontsize=14)
      plt.xlabel('Borough Name', fontsize=12)
      plt.ylabel('Number of Permits', fontsize=12)
      plt.xticks(rotation=45)
      plt.tight_layout()
      plt.savefig('nyc_permit_chart.png')
      plt.show()
    else:
        print(f"API ERROR: Status Code {response.status_code}")
except Exception as e:
    print(f"failed to load. Error: {e}")




        
    
