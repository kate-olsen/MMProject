import pandas as pd

# Read the CSV file
input_file = '/Users/olsen/Desktop/MMProject/IMCData/combined_data_full.csv'  # Replace with your input file name
output_file = 'filtered_data_roi1_3.csv'   # Name of the output file

# Read the CSV file
df = pd.read_csv(input_file)

# Filter the data
filtered_df = df[(df['Area'] >= 35) & (df['Area'] <= 650) & (df['DNA2'] != 0) & (df['ROI'] == '1_3') & (df['Slide_ID'] == '0AB0008')]

# Save the filtered data to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data has been saved to '{output_file}'")