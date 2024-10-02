import pandas as pd
import matplotlib.pyplot as plt

def create_area_histogram(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Filter the data to include only areas between 0 and 400
    #filtered_areas = df['Area'][(df['Area'] >= 0) & (df['Area'] <= 350)]
    filtered_areas = df['Area']
    # Create the histogram

    plt.hist(filtered_areas, bins=50, edgecolor='black')
    #plt.xlim(0, 500)

    
    # Add labels and title
    #plt.xlabel('Area')
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.title('Histogram of Areas')
    
    # Set x-axis limits
    #plt.xlim(0, 350)
    
    # Show the plot
    plt.savefig('area_histogram_full_v2.png')

# Usage
file_path = '/Users/olsen/Desktop/MMProject/IMCData/combined_data_full.csv'  # Replace with your CSV file path
#file_path = '/Users/olsen/Desktop/MMProject/1_3_v2.csv'
create_area_histogram(file_path)