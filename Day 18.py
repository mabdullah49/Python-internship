import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

def load_data(filename):
    try:
        if filename.endswith('.csv'):
            return pd.read_csv(filename)
        elif filename.endswith('.xlsx'):
            return pd.read_excel(filename)
        else:
            raise ValueError("Unsupported file format.")
    except Exception as e:
        print(f"Error loading file: {e}")
        sys.exit(1)

def generate_report(df, output_file='report.txt'):
    try:
        df['Revenue'] = df['Units Sold'] * df['Unit Price']
        revenue_by_product = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

        with open(output_file, 'w') as f:
            f.write("📊 Sales Summary\n")
            for product, revenue in revenue_by_product.items():
                f.write(f"Product: {product} – Revenue: {int(revenue)}\n")
            f.write(f"\n🔸 Total Revenue: {int(revenue_by_product.sum())}")
            f.write(f"\n🔸 Top Product: {revenue_by_product.idxmax()}\n")
        print(f"Report saved to {output_file}")
        return revenue_by_product
    except Exception as e:
        print(f"Error generating report: {e}")
        sys.exit(1)

def plot_chart(revenue_by_product):
    try:
        revenue_by_product.plot(kind='bar', color='skyblue')
        plt.title('Revenue by Product')
        plt.ylabel('Revenue')
        plt.tight_layout()
        plt.savefig('revenue_chart.png')
        print("Chart saved as revenue_chart.png")
    except Exception as e:
        print(f"Error creating chart: {e}")

if __name__ == '__main__':
    filename = input("Enter CSV or Excel filename: ").strip()
    df = load_data(filename)
    revenue = generate_report(df)
    plot_chart(revenue)
