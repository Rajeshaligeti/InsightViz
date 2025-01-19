# InsightViz 📈

# InsightViz

InsightViz is a web-based data visualization tool using Django, Pandas, and Matplotlib.It dynamic web application designed to help users upload datasets, visualize data, and gain meaningful insights. With interactive plots, detailed data summaries, and a user-friendly interface, InsightViz is perfect for analysts, students, and professionals looking to explore their data efficiently.

## Features

- Upload CSV or Excel files for analysis.
- Generate various types of plots:
  - Line Plot
  - Bar Plot
  - Scatter Plot
  - Histogram
  - Box Plot
  - Pie Chart etc...
- Interactive and visually appealing UI with a modern design.
- Download generated plots as PNG images.
- Data summary with column statistics, null counts, and unique value counts.

---

## Demo Screenshot
![Screenshot of InsightViz Interface](path/to/your/screenshot.png)

---

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/InsightViz.git
   cd InsightViz
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Linux/Mac
   myenv\Scripts\activate     # Windows
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run database migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## Usage
1. Upload a CSV or Excel file using the file upload form.
2. Select columns for the X-axis and Y-axis.
3. Choose the type of plot you want to generate.
4. Click "Generate Plot" to visualize the data.
5. Download the plot or view the data summary as needed.

---

## Folder Structure
```plaintext
InsightViz/
├── InsightViz/               # Django project folder
│   ├── settings.py           # Project settings
│   ├── urls.py               # URL configuration
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
│
├── visualization/            # Main app folder
│   ├── templates/            # HTML templates
│   │   └── index.html
│   ├── static/               # Static assets (CSS, JS, images)
│   │   ├── css/              # Stylesheets
│   │   ├── js/               # Scripts
│   │   └── images/           # Images
│   ├── forms.py              # Forms for file uploads
│   ├── views.py              # View logic
│   ├── urls.py               # App-specific URLs
│   └── admin.py              # Admin configurations
│
├── manage.py                 # Django management script
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Git ignore rules

```

---


## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
