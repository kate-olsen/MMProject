import pandas as pd
import matplotlib.pyplot as plt

def create_area_histogram(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Filter the data to include only areas between 0 and 400
    filtered_areas = df['Area'][(df['Area'] >= 0) & (df['Area'] <= 350)]
    
    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(filtered_areas, bins=50, edgecolor='black', range=(0, 350))
    
    # Add labels and title
    plt.xlabel('Area')
    plt.ylabel('Frequency')
    plt.title('Histogram of Areas (0-350)')
    
    # Set x-axis limits
    plt.xlim(0, 350)
    
    # Show the plot
    plt.savefig('area_histogram.png')

# Usage
file_path = '/Users/olsen/Desktop/MMProject/IMCData/combined_MM_data.csv'  # Replace with your CSV file path
create_area_histogram(file_path)