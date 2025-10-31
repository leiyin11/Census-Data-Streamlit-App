# Census-Streamlit-app

A Streamlit web application that performs analysis of U.S. Census data using the American Community Survey 5-year data (2017). The app explores socially important metrics including income inequality (Gini Index), housing vacancy, unemployment rates, and median family income at the county level.

[Medium Article detailing deployment to Azure.](https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743?source=friends_link&sk=fa59624f14261f6693bc250f396d0983)

## Features

- Real-time Census data querying using the CensusData API
- Interactive data visualizations with Seaborn and Matplotlib
- County-level analysis across the United States
- Customizable scatter plots and regression analysis
- Income quartile comparisons

## Setup and Run Instructions

### Option 1: Run Locally (Recommended for Development)

**Prerequisites:**
- Python 3.7 or higher
- pip package manager

**Steps:**

1. Clone the repository:
```bash
git clone https://github.com/leiyin11/Census-Data-Streamlit-App.git
cd Census-Data-Streamlit-App
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run census_app.py
```

5. Open your browser and navigate to:
```
http://localhost:8501
```

The app will automatically query Census data when it starts.

### Option 2: Run with Docker

**Prerequisites:**
- Docker installed on your machine

**Steps:**

1. Clone the repository (if not already done):
```bash
git clone https://github.com/leiyin11/Census-Data-Streamlit-App.git
cd Census-Data-Streamlit-App
```

2. Build the Docker image:
```bash
docker build -t census-streamlit-app .
```

3. Run the Docker container:
```bash
docker run -p 8501:80 census-streamlit-app
```

4. Open your browser and navigate to:
```
http://localhost:8501
```

### Option 3: Deploy to Streamlit Community Cloud (Free Hosting)

**Prerequisites:**
- GitHub account
- Streamlit Community Cloud account (free at [share.streamlit.io](https://share.streamlit.io))

**Steps:**

1. Fork or push this repository to your GitHub account

2. Go to [share.streamlit.io](https://share.streamlit.io)

3. Click "New app"

4. Connect your GitHub repository:
   - Repository: `your-username/Census-Data-Streamlit-App`
   - Branch: `main` (or your preferred branch)
   - Main file path: `census_app.py`

5. Click "Deploy"

Your app will be live at: `https://your-app-name.streamlit.app`

### Option 4: Deploy to Azure

Follow the detailed instructions in this [Medium Article](https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743?source=friends_link&sk=fa59624f14261f6693bc250f396d0983).

## Can I Run This on GitHub or Google Colab?

**GitHub:**
- You cannot run Streamlit apps directly on GitHub
- However, you can deploy to **Streamlit Community Cloud** (see Option 3 above), which connects to your GitHub repo for free hosting

**Google Colab:**
- Not recommended. Colab is designed for Jupyter notebooks, not web applications
- Streamlit requires a persistent web server, which Colab doesn't support natively
- You would need workarounds like ngrok tunneling, which adds complexity

**Recommended Alternatives:**
- For development: Run locally (Option 1)
- For free hosting: Streamlit Community Cloud (Option 3)
- For production: Docker (Option 2) or Azure (Option 4)

## Dependencies

- streamlit
- pandas
- numpy
- seaborn
- matplotlib
- censusdata

## Data Source

This app uses data from the American Community Survey (ACS) 5-year estimates via the [CensusData](https://pypi.org/project/CensusData/) Python package.

More information: [ACS 5-year Survey Documentation](https://www.census.gov/data/developers/data-sets/acs-5year.html)

## Troubleshooting

**Issue: Census API is slow or timing out**
- The app queries live Census data on startup, which can take 30-60 seconds
- This is normal behavior for the first load

**Issue: Import errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version (requires Python 3.7+)

**Issue: Port already in use**
- If port 8501 is busy, Streamlit will automatically try the next available port
- You can also specify a custom port: `streamlit run census_app.py --server.port 8502`
