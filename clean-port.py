import difflib
import json
import logging
import pandas as pd
import csv


# Constants
CUTOFF_RATIO = 0.7

ports = pd.read_excel("ports.xlsx")


def main():

    #creat input file handle
    with open('records.csv', encoding='utf8', newline='') as csvfile:

        #the file field names
        field_names = [
            'container_id',
            'hs_code',
            'description',
            'weight',
            'unit',
            'shipper_name',
            'port_of_loading',
            'port_of_discharge'
        ]

        clean_records=[]
        records = csv.reader(csvfile)
        for record in records:

            print(record)

            #clean port of loading
            clean_port = cleanse_port(record[6], ports)
            record[6] = clean_port

            #clean por of discharge
            clean_port = cleanse_port(record[7], ports)
            record[7] = clean_port

            clean_records.append(record)

            if not record[3] and record[4]:
                fetch_hs_code(record[4])

            format_hs_code(record[3])
  
        #write ouptut to file
        with open('clean.csv', 'w', newline='') as outfile:
            outfilewriter = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            outfilewriter.writerow(clean_records[1:])



def cleanse_port(port: str, lookup: pd.DataFrame) -> str:

    close_matches = difflib.get_close_matches(
        port.upper(), lookup["port"].tolist(), cutoff=CUTOFF_RATIO
    )

    #print(port)
    #print(lookup['port'].tolist())
    #print(close_matches)
    
    if len(close_matches) == 0:
        port_with_country = "Does not exist."
    else:
        lookup_row = lookup.loc[lookup["port"] == close_matches[0]]
        port = lookup_row["port"].item()
        country = lookup_row["country_code"].item().replace("\u00a0", "")
        port_with_country = f"{port}, {country}"
        
    return port_with_country


def fetch_hs_code(description: str) -> str:
    # use hs_codes file to find an hscode given a description
    # if you get multiple matches choose the most specific one
    # that is choose a 6 digit over a 4 digit
    # if you get a 4 digit and 2 6 digit then better to stick with
    # 4 digits
    return ''

def format_hs_code(hs_code: str) -> str:
    #must have and even number of digits on either side of the decimal
    #ex: 301.1 formats to 0301.10
    #cannot have more than 4 digits to the left of decimal with up to 8 decimals after
    #ex: 0801.09011127
    
    return hs_code
    
if __name__ == "__main__":
    main()
