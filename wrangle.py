############ INITIAL IMPORTS ###########

import os
import requests
import pandas as pd
import tabula
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

############# PREP POLA FUNCTION #############

def prep_pola(df):
    
    # Change the 2014-08-04 value to 2015-08-04
    df.iloc[97].date = '8/4/2015'
    
    # Set the date column as the datetime index
    df.date = pd.to_datetime(df.date)
    df = df.set_index('date')
 
    # Convert column values to floats
    for col in df.columns:
        df[col] = df[col].astype(float)

    return df

############ WRANGLE POLA FUNCTION ###########

def wrangle_pola():    
    """
    Reads in the POLA data. From the csv if it's already there and if not, it downloads the data from the Port of Los Angeles
    website as pdfs, converts them to dataframes, concatenates them, deletes the original pdfs, and saves the combined data
    in a csv file called 'pola.csv'
    """
    # Check if the 'pola.csv' file already exists
    if os.path.exists('pola.csv'):
        # If the file exists, read the data from the CSV file
        results_df = pd.read_csv('pola.csv')
        results_df = prep_pola(results_df)
        
    else:
        # List of URLs for the PDFs to download and process
        lst = [
            "1a8f2a5f-8d5f-4262-a1f8-2de701fc1bda/Port-of-Los-Angeles-Container-Vessel-Activity-Summary-2018",
            "517cbd39-d632-489d-bddf-87750ca1ccb5/Port-of-Los-Angeles-Container-Vessel-Activity-Summary-2017",
            "2d907886-b866-4610-9c62-b4171662ddad/Port-of-Los-Angeles-Container-Vessel-Activity-Summary-2016",
            "79aeef2f-c3e8-4277-82c3-c5eccc2492e2/Port-of-Los-Angeles-Container-Vessel-Activity-Summary-2015"
        ]

        # Loop through the list of URLs and download PDFs
        for i in lst:
            pdf_url = f"https://kentico.portoflosangeles.org/getmedia/{i}"
            # Send an HTTP GET request to the URL
            response = requests.get(pdf_url)
            # Check if the request was successful
            if response.status_code == 200:
                # Get the filename from the URL
                filename = 'pola' + pdf_url.split("/")[-1].split('-')[-1] + '.pdf'
                # Save the PDF content to a local file
                with open(filename, "wb") as pdf_file:
                    pdf_file.write(response.content)
            else:
                print("Failed to retrieve the PDF.")
        # Initialize an empty DataFrame to store the results
        results_df = pd.DataFrame()

        # Loop through years (2015-2018) to process PDFs
        for i in range(5, 9):
            # Path to the PDF file
            pdf_file_path = f'pola201{i}.pdf'

            # Extract tables from the PDF and return a list of DataFrames
            tables = tabula.read_pdf(pdf_file_path, pages='all', multiple_tables=True)

            # Initialize an empty DataFrame for each year
            df = pd.DataFrame()
            for idx, table in enumerate(tables):
                df = pd.concat([df, pd.DataFrame(table)], axis=0)

            # Drop the 'Unnamed: 0' column if present
            if 'Unnamed: 0' in df.columns:
                df = df.drop(columns='Unnamed: 0')

            # Drop null rows
            df = df.dropna()

            # Concatenate the DataFrames for different years
            results_df = pd.concat([results_df, df], axis=0)

            # Remove the processed PDF file
            os.remove(pdf_file_path)

        results_df = results_df.reset_index().drop(columns='index')

        fix_list = [124, 172]

        for i in fix_list:
            values = []
            for j in range(len(results_df.columns)):
                values.append(results_df.values[i].tolist()[j].split('\r'))

            temp_df = pd.DataFrame({
                'Date': [values[0][0], values[0][1]],
                'POLA Vessels at\rAnchor' : [values[1][0], values[1][1]],
                'POLA Vessels at\rBerth': [values[2][0], values[2][1]],
                'POLA Vessels\rDeparted': [values[3][0], values[3][1]],
                'Average Days at\rBerth': [values[4][0], values[4][1]],
                'Average Days at\rANC + Berth': [values[5][0], values[5][1]]
                })

            results_df = pd.concat([results_df.iloc[:i], temp_df, results_df[i+1:]], axis=0).reset_index(drop=True)
       
        # Rename columns for readability
        results_df = results_df.rename(columns={'Date':'date',
                   'POLA Vessels at\rAnchor':'num_at_anchor', 
                   'POLA Vessels at\rBerth':'num_at_berth',
                   'POLA Vessels\rDeparted':'departed',
                   'Average Days at\rBerth':'avg_days_at_berth',
                   'Average Days at\rANC + Berth':'avg_days_anchor_berth'})
        
        # Save the dataframe to a csv in the working directory named 'pola.csv'
        results_df.to_csv('pola.csv', index=False)
        
        results_df = prep_pola(results_df)
        
    return results_df

    
    















