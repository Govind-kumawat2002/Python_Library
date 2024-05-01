from fpdf import FPDF

def convert_to_pdf(input_file, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Read the Python file and write its content to the PDF
    with open(input_file, "r") as f:
        for line in f:
            pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(output_file)

# Example usage
convert_to_pdf("classification.ipynb", "example.pdf")
