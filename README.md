# Solar Panel Strategy Analysis
## Project Overview
This project focuses on analyzing solar farm data from Benin, Sierra Leone, and Togo to recommend optimal solar panel installation sites. The goal is to help a company become more efficient and sustainable by leveraging environmental data to determine the best locations for solar panel installations.

## Key Features
 **Data Processing**: Scripts to load, clean, and preprocess solar radiation data, including variables like Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI).
 **Exploratory Data Analysis (EDA)**:Visualization and analysis of the data to identify trends and patterns in solar radiation.
 **Time Series Analysis**:Analyzing solar radiation data over time to understand seasonal and temporal variations.
 **CI/CD Integration**: Implementing Continuous Integration/Continuous Deployment (CI/CD) pipelines using GitHub Actions.
 **Streamlit App:** An interactive web application built with Streamlit for visualizing and analyzing solar radiation data.

## Project Structure:
app/main.py                   # Main Streamlit application
data/                         # Dataset
notebooks/ data_analysis.ipynb # Jupyter notebook for data analysis
tests/ test_data_loading.py    # Tests for data loading
.gitignore                    # Git ignore file
requirements.txt              # Python dependencies
README.md                     # Project documentation


## Installation

1. **Clone the repository**:

   git clone https://github.com/EstifanosAschalew/solar-panel-strategy-analysis.git
   cd solar-panel-strategy-analysis
   

2. **Create and activate a virtual environment**:
   python -m venv project-venv
   source project-venv/bin/activate  # On Windows use `project-venv\Scripts\activate`

3. **Install the required dependencies**:
    pip install -r requirements.txt

## Usage
 **Running the Streamlit App**
    To run the Streamlit application, use the following command:
        streamlit run app/main.py
    This will launch the web app, and you can access it in your browser.

 **Running Tests**
    To run the test suite, use the following command:
        pytest tests/

## Contributing
Contributions are welcome! Please follow the steps below to contribute:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to the branch.
5. Create a pull request.

## Contact
For any questions or inquiries, feel free to contact me at [estifaschalew@gmail.com]

