import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO

def process_file_and_generate_plot(uploaded_file):
    # Read file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx') or uploaded_file.name.endswith('.xls'):
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    elif uploaded_file.name.endswith('.json'):
        df = pd.read_json(uploaded_file)
    else:
        raise ValueError("Unsupported file format. Please upload CSV, Excel, or JSON.")

    # Generate a plot
    fig, ax = plt.subplots()
    df.describe().plot(kind='bar', ax=ax)
    plt.tight_layout()

    # Save plot to BytesIO
    imgdata = BytesIO()
    plt.savefig(imgdata, format='png')
    plt.close(fig)

    # Save processed data to Excel
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Processed Data')
    workbook = writer.book
    worksheet = writer.sheets['Processed Data']
    worksheet.insert_image('G2', 'plot.png', {'image_data': imgdata})
    writer.close()

    return df, imgdata, output
