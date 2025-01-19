from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from .forms import UploadFileForm
import seaborn as sns

def index(request):
    context = {'form': UploadFileForm()}

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            # Load data
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            context['columns'] = df.columns.tolist()

            # If plot parameters are submitted
            x_axis = request.POST.get('x_axis')
            y_axis = request.POST.get('y_axis')
            plot_type = request.POST.get('plot_type')

            if x_axis and y_axis and plot_type:
                fig = generate_plot(df, x_axis, y_axis, plot_type)
                
                # Save plot to buffer for rendering
                img_data = BytesIO()
                fig.savefig(img_data, format='png')
                img_data.seek(0)
                img_base64 = base64.b64encode(img_data.getvalue()).decode('utf-8')

                # Add detailed data summary
                summary = {
                    'column_summary': df.describe().to_dict(),
                    'null_counts': df.isnull().sum().to_dict(),
                    'unique_counts': df.nunique().to_dict(),
                }

                # Add to context
                context.update({
                    'plot': img_base64,
                    'summary': summary,
                })

    return render(request, 'visualization/index.html', context)


def generate_plot(df, x_axis, y_axis, plot_type):
    if not pd.api.types.is_numeric_dtype(df[y_axis]) and plot_type not in ["Pie Chart", "Heatmap"]:
        raise ValueError(f"The '{y_axis}' column contains non-numeric data and cannot be used for this plot type.")
    if not pd.api.types.is_numeric_dtype(df[x_axis]) and plot_type not in ["Pie Chart", "Heatmap"]:
        raise ValueError(f"The '{x_axis}' column contains non-numeric data and cannot be used for this plot type.")
    
    fig, ax = plt.subplots()

    if plot_type == "Line Plot":
        ax.plot(df[x_axis], df[y_axis])
    elif plot_type == "Bar Plot":
        ax.bar(df[x_axis], df[y_axis])
    elif plot_type == "Scatter Plot":
        ax.scatter(df[x_axis], df[y_axis])
    elif plot_type == "Histogram":
        ax.hist(df[y_axis], bins='auto')
    elif plot_type == "Box Plot":
        ax.boxplot(df[y_axis])
    elif plot_type == "Area Plot":
        ax.fill_between(df[x_axis], df[y_axis], alpha=0.5)
    elif plot_type == "Pie Chart":
        df[y_axis].value_counts().plot.pie(ax=ax, autopct='%1.1f%%', startangle=90, shadow=True)
        ax.set_ylabel('')
    elif plot_type == "Heatmap":
        correlation = df.corr()
        sns.heatmap(correlation, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    elif plot_type == "Stacked Bar Plot":
        stacked_data = df.pivot_table(index=x_axis, columns=y_axis, aggfunc='size', fill_value=0)
        stacked_data.plot(kind="bar", stacked=True, ax=ax)

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f"{plot_type}: {y_axis} vs {x_axis}")
    return fig

