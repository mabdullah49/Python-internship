import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create plots directory if not exists
if not os.path.exists('plots'):
    os.makedirs('plots')

# Load dataset
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data Loaded Successfully!")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Line Plot
def plot_line(data, x_col, y_col, title, filename):
    plt.figure(figsize=(10,6))
    plt.plot(data[x_col], data[y_col], marker='o')
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.grid(True)
    plt.savefig(f'plots/{filename}')
    plt.close()

# Bar Plot
def plot_bar(data, x_col, y_col, title, filename):
    plt.figure(figsize=(10,6))
    sns.barplot(x=x_col, y=y_col, data=data)
    plt.title(title)
    plt.savefig(f'plots/{filename}')
    plt.close()

# Pie Chart
def plot_pie(data, labels_col, values_col, title, filename):
    plt.figure(figsize=(8,8))
    plt.pie(data[values_col], labels=data[labels_col], autopct='%1.1f%%', startangle=140)
    plt.title(title)
    plt.savefig(f'plots/{filename}')
    plt.close()

# Correlation Heatmap
def plot_heatmap(data, filename):
    plt.figure(figsize=(10,8))
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.savefig(f'plots/{filename}')
    plt.close()

# Generate Summary Report
def generate_summary(data, filename='Summary_Report.txt'):
    summary = data.describe().to_string()
    with open(filename, 'w') as f:
        f.write("Summary Statistics:\n")
        f.write(summary)
    print(f"Summary report saved as {filename}")

if __name__ == "__main__":
    # Replace 'sales.csv' with your actual CSV file
    data = load_data('sales.csv')

    if data is not None:
        # Example plots (replace column names with actual data columns)
        plot_line(data, 'Month', 'Revenue', 'Monthly Revenue', 'Line_Chart.png')
        plot_bar(data, 'Product', 'Sales', 'Product Sales', 'Bar_Chart.png')
        plot_pie(data, 'Market', 'Share', 'Market Share', 'Pie_Chart.png')
        plot_heatmap(data, 'Heatmap.png')
        generate_summary(data)
