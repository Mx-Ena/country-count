# Country Count Visualization

A web application that visualizes the distribution of countries by their starting letters across different continents.

## Features

- Interactive bar charts showing country distribution by starting letter
- Hover tooltips displaying all countries for each letter
- Clickable letters to view detailed country lists
- Dark theme UI
- Hot reloading for development

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd country-count
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Development

To run the application with hot reloading:

```bash
flask --app app.py --debug run
```

The application will be available at `http://localhost:5000`

Hot reloading features:
- Automatically reloads when Python files are modified
- Automatically reloads when template files are modified
- Shows detailed error messages in the browser
- Preserves application state during reloads

## Project Structure

```
country-count/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Main template with charts
```

## Dependencies

- Flask
- Chart.js (loaded via CDN)

## Technologies

### Backend
- Python 3.12
- Flask (Web Framework)
- JSON for data handling

### Frontend
- HTML5
- CSS3 (Custom styling)
- JavaScript (Vanilla)
  - Fetch API for AJAX requests
  - DOM manipulation for dynamic content

### Data Structure
- Organized by continents
- Comprehensive country database
- Letter-frequency mapping

## Getting Started

1. Install dependencies:
```bash
pip install flask
```

2. Run the server:
```bash
python app.py
```

3. Open your browser and navigate to: 