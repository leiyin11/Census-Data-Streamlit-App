"""
Census Data Exploration Streamlit App

This application provides interactive exploration of U.S. Census data at the county level.
It downloads data from the American Community Survey (ACS) 5-Year dataset and provides
visualizations and statistical analysis of socioeconomic metrics.

Author: Census Data App Contributors
License: MIT
"""

import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import censusdata
import warnings

# Suppress matplotlib warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Census Data Explorer",
    page_icon="📊",
    layout="wide"
)

# Header section
st.image(image='censusimg.jpg', caption='https://pixabay.com/illustrations/magnifying-glass-human-head-faces-1607208/')

st.title('Census Data Exploration')
st.header('Explore socially important metrics')
st.write('This exploration uses data from American Community Survey 5-year data released in 2018.')
st.write('More information about the ACS 5-year survey: https://www.census.gov/data/developers/data-sets/acs-5year.html')
st.write("The data was collected using Julien Leider's CensusData pip package, which can be found at https://pypi.org/project/CensusData/ or installed with")
st.code('pip install CensusData')

st.header('County Level Summaries')
st.write('This analysis uses data aggregated on the county level for the variables: Gini Index (income inequality index), Vacant Housing, Percent Unemployed and Median Family Income.')


### SECTION 1: Querying and Cleaning Data ###

@st.cache_data(show_spinner="Fetching census data... This may take a minute.")
def ApiQuery():
    """
    Query the Census API and download county-level data.

    Returns:
        pd.DataFrame: DataFrame containing census data with renamed columns

    Raises:
        Exception: If the API query fails
    """
    try:
        with st.spinner('Downloading census data from API...'):
            # Query the data and save to a dataframe
            df = censusdata.download('acs5', 2018,
                                    censusdata.censusgeo([('state', '*'),('county', '*')]),var=
                                    ['B19083_001E','B19113_001E','B23025_003E','B23025_005E','B01001_001E','B25004_001E'])
    except Exception as e:
        st.error(f'Could not query census data: {str(e)}')
        st.info('Please check your internet connection and try refreshing the page.')
        st.stop()

    df = df.reset_index()
    df.columns = ['Location','gini_index','median_family_income','employed','unemployed','population',
                'vacant_housing']

    return df


def FindFipsId(df):
    """
    Parse the Location column to extract FIPS codes and county names.

    Args:
        df (pd.DataFrame): DataFrame with Location column containing geographic information

    Returns:
        pd.DataFrame: DataFrame with additional columns for state_fips, county_fips, fips, and county_name
    """
    # Set the Location variable as type string
    df.Location = df.Location.astype(str)

    # Drop Puerto Rico (Sorry!!!)
    df = df[df['Location'].str.contains("Puerto Rico:")==False]

    # Define a lambda expression to extract the state fips ID, and apply to the dataframe.
    state_fips = lambda a: a[a.find('state:')+6:a.find('state:')+8]
    df['state_fips'] = df['Location'].apply(state_fips)

    # Define a lambda expression to extract the county fips, and apply to the dataframe.
    county_fips = lambda a: a[a.find('county:')+7:a.find('county:')+11]
    df['county_fips'] = df['Location'].apply(county_fips)

    # Combine the two strings for the state and county fips to a single fips identifier.
    df['fips'] = df.state_fips+df.county_fips
    df.fips = df.fips.astype('int32')

    # Define a lambda expression to extract the county name, and apply to the dataframe
    county_name = lambda a: a[:a.find('County,')+6]
    df['county_name'] = df['Location'].apply(county_name)

    # Convert state fips and county fips to numeric values
    df['state_fips'] = pd.to_numeric(df.state_fips)
    df['county_fips'] = pd.to_numeric(df.county_fips)

    # Drop Location as it is has been parsed into multiple variables.
    # It is a long string, and unnecessary.
    df = df.drop('Location', axis=1)

    return df


def PctUnemployed(df):
    """
    Calculate the unemployment percentage from employed and unemployed counts.

    Args:
        df (pd.DataFrame): DataFrame containing 'employed' and 'unemployed' columns

    Returns:
        pd.DataFrame: DataFrame with additional 'percent_unemployed' column
    """
    df['percent_unemployed'] = df.unemployed / df.employed * 100

    return df


def OnlyColumns(df):
    """
    Select and rename columns needed for analysis.

    Args:
        df (pd.DataFrame): DataFrame containing all census data

    Returns:
        pd.DataFrame: DataFrame with only analysis columns and formatted names
    """
    # Return only the necessary columns for analysis
    df = df[['gini_index','vacant_housing','percent_unemployed', 'median_family_income']]
    # Rename the columns
    df.columns = ['Gini Index', 'Vacant Housing', 'Percent Unemployed', 'Median Family Income']

    return df


# Execute the data pipeline
try:
    # Execute the ApiQuery function to retrieve the data.
    df = ApiQuery()

    # Find the FIPS Id by parsing the location string column.
    df = FindFipsId(df)

    # Calculate percent unemployed.
    df = PctUnemployed(df)

    # Select only the necessary columns.
    df = OnlyColumns(df)

except Exception as e:
    st.error(f"An error occurred during data processing: {str(e)}")
    st.stop()


### SECTION 2: Display the data and visualizations ###

# Dataframe for median family income Statistics
st.subheader('Descriptive Statistics for Median Family Income')
st.write(df['Median Family Income'].describe().round())

# Histogram for median family income (using histplot instead of deprecated distplot)
st.subheader('Distribution of Median Family Income')
fig1, ax1 = plt.subplots(figsize=(10, 6))
plt.title('County Level Income Distribution')
sns.set_style('darkgrid')
sns.histplot(df['Median Family Income'], kde=True, ax=ax1, color='steelblue')
ax1.set_xlabel('Median Family Income ($)')
ax1.set_ylabel('Frequency')
st.pyplot(fig1)
plt.close()

# Create a new column based on median family income called 'Income Quartile'.
df['Income Quartile'] = pd.qcut(df['Median Family Income'], q=4, labels=False, precision=0, duplicates='raise')
# Zero-based, raise by 1
df['Income Quartile'] = df['Income Quartile'] + 1

# Scatterplot for median family income by quartile
st.subheader('Median Family Income versus Unemployment Rate')
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.set_style('darkgrid')
plt.title('Median Family Income versus Unemployment')
sns.scatterplot(x='Median Family Income', y='Percent Unemployed', data=df, hue='Income Quartile',
                palette="Dark2", ax=ax2, alpha=0.6)
ax2.set_xlabel('Median Family Income ($)')
ax2.set_ylabel('Percent Unemployed (%)')
st.pyplot(fig2)
plt.close()

# Interactive analysis section
st.subheader('Custom Variable Analysis')
st.write('Select two variables to explore their relationship across income quartiles.')

col1, col2 = st.columns(2)

with col1:
    x_axis = st.selectbox(
        'Pick an X-axis value:',
        ['Gini Index', 'Vacant Housing', 'Percent Unemployed', 'Median Family Income'])

with col2:
    y_axis = st.selectbox(
        'Pick a Y-axis value:',
        ['Percent Unemployed','Gini Index', 'Vacant Housing','Median Family Income'])

# Validate that different variables are selected
if x_axis == y_axis:
    st.warning('Please select different variables for X and Y axes for meaningful analysis.')
else:
    # Generate the lmplot
    st.subheader(f'Regression Analysis: {x_axis} vs {y_axis}')
    st.write('Each panel represents a different income quartile (1=lowest, 4=highest)')

    sns.set()
    sns.set_style('darkgrid')
    sns.set_context("paper", font_scale=1.3)

    # Create lmplot (this creates its own figure)
    g = sns.lmplot(x=x_axis, y=y_axis, data=df, hue='Income Quartile',
                   col='Income Quartile', col_wrap=2, height=4, aspect=1.2,
                   palette="Dark2", scatter_kws={'alpha':0.5})

    g.fig.suptitle(f'{x_axis} vs {y_axis} by Income Quartile', y=1.02, fontsize=14)
    st.pyplot(g.fig)
    plt.close()

# Data export option
st.subheader('Download Data')
csv = df.to_csv(index=False)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='census_data_county_level.csv',
    mime='text/csv',
)

# Footer
st.markdown('---')
st.markdown('**Data Source:** U.S. Census Bureau, American Community Survey 5-Year Data (2018)')
st.markdown('**Built with:** Streamlit, Python, Seaborn, and the CensusData package')
