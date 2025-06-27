import csv
from fpdf import FPDF

# Function to read and analyze data
def analyze_csv_data(sales_datacsv):
    product_summary = {}
    total_revenue = 0

    with open("sales_data.csv", newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product = row['Product']
            units = int(row['Units Sold'])
            price = float(row['Unit Price'])
            revenue = units * price
            total_revenue += revenue

            if product not in product_summary:
                product_summary[product] = {'units': 0, 'revenue': 0}
            product_summary[product]['units'] += units
            product_summary[product]['revenue'] += revenue

    return total_revenue, product_summary

# Function to generate PDF report
def generate_pdf_report(total_revenue, product_summary, output_file="sales_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, "Sales Report", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Total Revenue: ${total_revenue:.2f}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(60, 10, "Product", 1)
    pdf.cell(40, 10, "Units Sold", 1)
    pdf.cell(40, 10, "Revenue ($)", 1)
    pdf.ln()

    pdf.set_font("Arial", size=12)
    for product, stats in product_summary.items():
        pdf.cell(60, 10, product, 1)
        pdf.cell(40, 10, str(stats['units']), 1)
        pdf.cell(40, 10, f"{stats['revenue']:.2f}", 1)
        pdf.ln()

    pdf.output(output_file)
    print(f"PDF report generated: {output_file}")

# Main execution
if __name__ == "__main__":
    csv_file = "sales_data.csv"
    total_revenue, product_summary = analyze_csv_data("sales_data.csv")
    generate_pdf_report(total_revenue, product_summary)
