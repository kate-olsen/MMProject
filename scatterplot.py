import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('/Users/olsen/Desktop/MMProject/filtered_data_2.csv')

# Create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['DNA2'], df['Eccentricity'], alpha=0.5)
#plt.scatter(df['Area'], df['DNA1'], alpha=0.5)

plt.xlabel('DNA2')
plt.ylabel('Eccentricity')
plt.title('DNA2 vs Eccentricity Scatter Plot (Filtered)')

# Set the maximum value for the x-axis (Area) to 800
#plt.xlim(right=800)

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.7)

# Improve the layout
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig('/Users/olsen/Desktop/MMProject/scatterplots/DNA2_vs_Eccentricity_scatter_filtered.png', dpi=300)

# Display the plot (optional, comment out if running in a non-interactive environment)
plt.show()

print("Scatter plot has been saved as 'DNA2_vs_Eccentricity_scatter_filtered.png'")

""" import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read the CSV file
df = pd.read_csv('/Users/olsen/Desktop/MMProject/filtered_data.csv')  # Replace with your actual file name

# List of columns to compare with CD45 (excluding non-numeric columns)
columns_to_plot = [
    'Area', 'BCMA_2_clones', 'CCR4_CD194', 'CCR7', 'CD117', 'CD11c', 'CD123', 'CD127',
    'CD138_Syndecan', 'CD14', 'CD16', 'CD161', 'CD20_H1', 'CD20_SP32', 'CD223_LAG3',
    'CD25_IL2', 'CD27', 'CD28', 'CD294_and_CXCR3', 'CD3', 'CD38', 'CD4', 'CD45RA',
    'CD45_RO', 'CD56', 'CD62L', 'CD66b_CEACAM', 'CD69', 'CD8a', 'DNA1', 'DNA2',
    'Eccentricity', 'Extent', 'HLA_DR', 'PD-1', 'Solidity'
]

# Set up the plot style
sns.set_style("whitegrid")

# Calculate the grid dimensions
n = len(columns_to_plot)
cols = 4  # You can adjust this to change the number of columns in the grid
rows = int(np.ceil(n / cols))

# Create subplots
fig, axes = plt.subplots(rows, cols, figsize=(20, 5 * rows))
axes = axes.flatten()  # Flatten the 2D array of axes for easy indexing

for i, column in enumerate(columns_to_plot):
    ax = axes[i]
    
    # Create scatter plot
    sns.scatterplot(data=df, x='CD45', y=column, alpha=0.5, ax=ax)
    
    ax.set_title(f'CD45 vs {column}')
    ax.set_xlabel('CD45')
    ax.set_ylabel(column)

    # set limit max 40 (dataset max is 738 followed by 35.9)
    ax.set_xlim(left=0, right=40)

# Remove any unused subplots
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# Adjust the layout and save the plot
plt.tight_layout()
plt.savefig('/Users/olsen/Desktop/MMProject/scatterplots/CD45_vs_specific_columns_scatter.png', dpi=300, bbox_inches='tight')
plt.close()

print("Scatter plots have been saved as 'CD45_vs_specific_columns_scatter.png'")

# Calculate and print correlation coefficients
correlations = df[['CD45'] + columns_to_plot].corr()['CD45'].sort_values(ascending=False)
print("\nCorrelation coefficients with CD45:")
print(correlations) """