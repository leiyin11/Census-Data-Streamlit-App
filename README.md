# Census Data Streamlit App

A comprehensive interactive web application for exploring and analyzing U.S. Census data at the county level. Built with Streamlit, this app provides data visualization and statistical analysis of key socioeconomic indicators from the American Community Survey (ACS).

![Census Data](censusimg.jpg)

## 🎯 Features

- **Real-time Census Data**: Automatically fetches the latest county-level data from the Census Bureau API
- **Interactive Visualizations**: Explore relationships between different socioeconomic variables
- **Statistical Analysis**: View descriptive statistics and distribution plots
- **Correlation Analysis**: Compare any two variables with regression analysis by income quartile
- **Multi-Metric Dashboard**: Analyze Gini Index, vacant housing, unemployment rates, and median family income

## 📊 Analyzed Metrics

This application explores four key county-level metrics:

1. **Gini Index** - Measure of income inequality (0 = perfect equality, 1 = perfect inequality)
2. **Vacant Housing** - Number of vacant housing units
3. **Percent Unemployed** - Unemployment rate as percentage of labor force
4. **Median Family Income** - Median income for families in the county

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip (Python package manager)
- Docker (optional, for containerized deployment)

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Census-Data-Streamlit-App.git
   cd Census-Data-Streamlit-App
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run census_app.py
   ```

5. **Open your browser** to `http://localhost:8501`

### Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t census-streamlit-app .
   ```

2. **Run the container**
   ```bash
   docker run -p 80:80 census-streamlit-app
   ```

3. **Access the app** at `http://localhost`

## 📖 Usage Guide

### Dashboard Overview

1. **Descriptive Statistics**: View summary statistics for median family income across all counties
2. **Distribution Plot**: Examine the distribution of median family income using a histogram
3. **Scatterplot Analysis**: Explore the relationship between median income and unemployment, colored by income quartile
4. **Custom Analysis**: Select any two variables to generate regression plots by income quartile

### Interactive Features

- Use the dropdown menus to select X and Y axis variables
- The app automatically generates regression plots for each income quartile
- All visualizations update dynamically based on your selections

## 🏗️ Architecture

```
census_app.py           # Main Streamlit application
├── ApiQuery()          # Fetches data from Census API
├── FindFipsId()        # Parses geographic identifiers
├── PctUnemployed()     # Calculates unemployment percentage
└── OnlyColumns()       # Selects relevant columns for analysis
```

## 📦 Data Source

This application uses the **American Community Survey (ACS) 5-Year Data** via the Census Bureau API:

- **Dataset**: ACS 5-Year Estimates (2018)
- **Geographic Level**: County
- **Variables Used**:
  - `B19083_001E` - Gini Index
  - `B19113_001E` - Median Family Income
  - `B23025_003E` - Employed
  - `B23025_005E` - Unemployed
  - `B01001_001E` - Total Population
  - `B25004_001E` - Vacant Housing Units

Data is retrieved using the [CensusData](https://pypi.org/project/CensusData/) Python package.

## 🔧 Configuration

### Streamlit Configuration

The `config.toml` file includes settings for:
- Server configuration (port, headless mode)
- Browser settings
- Logging levels
- Performance options

### Environment Variables

Create a `.env` file (optional) for custom configuration:
```bash
CENSUS_API_YEAR=2018
STREAMLIT_PORT=8501
```

## 🐳 Cloud Deployment

This application is designed for easy deployment to cloud platforms:

- **Azure App Service**: [Detailed deployment guide](https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743?source=friends_link&sk=fa59624f14261f6693bc250f396d0983)
- **Heroku**: Use the included Dockerfile
- **AWS**: Deploy via ECS or Elastic Beanstalk
- **Google Cloud**: Deploy via Cloud Run

## 🤝 Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [U.S. Census Bureau](https://www.census.gov/) for providing open access to census data
- [Julien Leider](https://pypi.org/project/CensusData/) for the CensusData Python package
- [Streamlit](https://streamlit.io/) for the amazing web app framework
- Image credit: [Pixabay](https://pixabay.com/illustrations/magnifying-glass-human-head-faces-1607208/)

## 📚 Additional Resources

- [Census API Documentation](https://www.census.gov/data/developers/data-sets/acs-5year.html)
- [ACS 5-Year Estimates](https://www.census.gov/data/developers/data-sets/acs-5year.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [CensusData Package Documentation](https://jtleider.github.io/censusdata/)

## 📞 Support

For questions or issues, please [open an issue](https://github.com/yourusername/Census-Data-Streamlit-App/issues) on GitHub.

---

**Built with ❤️ using Streamlit and U.S. Census Data**
