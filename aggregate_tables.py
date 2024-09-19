import pandas as pd

def process_csv_files():
    # Define the file paths and their corresponding slide IDs
    file_info = [
        #MGUS Data
        ('/Users/olsen/Desktop/MMProject/IMCData/MGUS/0AB0008_full.csv', '0AB0008'),
        ('/Users/olsen/Desktop/MMProject/IMCData/MGUS/0AE3D05_full.csv', '0AE3D05'),
        ('/Users/olsen/Desktop/MMProject/IMCData/MGUS/0AE1405_full.csv', '0AE1405'),
        ('/Users/olsen/Desktop/MMProject/IMCData/MGUS/0B1F401_full.csv', '0B1F401'),
        ('/Users/olsen/Desktop/MMProject/IMCData/MGUS/0B24C03_full.csv', '0B24C03'),

        #NDMM Data
        ('/Users/olsen/Desktop/MMProject/IMCData/NDMM/0AAE109_full.csv', '0AAE109'),
        ('/Users/olsen/Desktop/MMProject/IMCData/NDMM/0AB4D07_full.csv', '0AB4D07'),
        ('/Users/olsen/Desktop/MMProject/IMCData/NDMM/0AB9007_full.csv', '0AB9007'),
        ('/Users/olsen/Desktop/MMProject/IMCData/NDMM/0ABD904_full.csv', '0ABD904'),
        ('/Users/olsen/Desktop/MMProject/IMCData/NDMM/0AC0E04_full.csv', '0AC0E04'),

        #RRMM Data
        ('/Users/olsen/Desktop/MMProject/IMCData/RRMM/0AAC805_full.csv', '0AAC805'),
        ('/Users/olsen/Desktop/MMProject/IMCData/RRMM/0ABB304_full.csv', '0ABB304'),
        ('/Users/olsen/Desktop/MMProject/IMCData/RRMM/0AC9D04_full.csv', '0AC9D04'),
        ('/Users/olsen/Desktop/MMProject/IMCData/RRMM/0AC9204_full.csv', '0AC9204'),

        #SMM Data
        ('/Users/olsen/Desktop/MMProject/IMCData/SMM/0ABC209_full.csv', '0ABC209'),
        ('/Users/olsen/Desktop/MMProject/IMCData/SMM/0AD8404_full.csv', '0AD8404'),
        ('/Users/olsen/Desktop/MMProject/IMCData/SMM/0ADF504_full.csv', '0ADF504'),
        ('/Users/olsen/Desktop/MMProject/IMCData/SMM/0B08F03_full.csv', '0B08F03'),
        ('/Users/olsen/Desktop/MMProject/IMCData/SMM/0B13803_full.csv', '0B13803')

        #Prostate Cancer (0)
        # ('/Users/olsen/Desktop/MMProject/IMCData/Prostate Cancer (0)/091473_full.csv', '091473'),
        # ('/Users/olsen/Desktop/MMProject/IMCData/Prostate Cancer (0)/091603_full.csv', '091603'),
        # ('/Users/olsen/Desktop/MMProject/IMCData/Prostate Cancer (0)/093284_full.csv', '093284')
    ]

    # List to store all dataframes
    all_dfs = []

    # Process each file
    for file_path, slide_id in file_info:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Add a new column 'Slide_ID' at the beginning
        df.insert(0, 'Slide_ID', slide_id)
        
        # Append to our list of dataframes
        all_dfs.append(df)

    # Concatenate all dataframes
    combined_df = pd.concat(all_dfs, ignore_index=True)

    # Save the combined dataframe to a new CSV file
    output_path = '/Users/olsen/Desktop/MMProject/IMCData/combined_MM_data.csv'
    combined_df.to_csv(output_path, index=False)

    print(f"Combined data saved to '{output_path}' with {len(combined_df)} rows.")

# Run the function
process_csv_files()