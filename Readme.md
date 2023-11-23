[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10086515.svg)](https://doi.org/10.5281/zenodo.10086515) [![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# SPbLitGuide Project

## Overview

This Streamlit project focuses on presenting and analyzing a dataset derived from SPbLitGuide, a newsletter known for its coverage of literary events in St. Petersburg. The project uses Streamlit for web app creation, enabling interactive data exploration and visualization.

## Structure

- home.py: The main script that initializes the Streamlit app. It sets up the page title and includes the primary functions for displaying different pages.
- pages/: A directory containing individual Streamlit pages. Each page likely represents a specific aspect or analysis of the dataset.
- SPbLitGuide_DataProcessing.ipynb: A Jupyter Notebook for data processing and preliminary analysis.
- requirements.txt: Lists all Python dependencies required for this project.
- .streamlit/: Configuration settings for the Streamlit app.

## Streamlit App Link

You can access the SPbLitGuide app deployed in the cloud [here](https://spblitguide.streamlit.app).

## Installation

To set up the project, follow these steps:

- Clone the repository.
- Install the required packages using:

```
pip install -r requirements.txt
```

Run the Streamlit app:

```
streamlit run home.py
```

## Usage

The app provides interactive tools to explore the SPbLitGuide dataset. Navigate through different pages to view various analyses and visualizations.

## Contributing

Contributions to enhance the functionality or analysis are welcome. Please follow standard procedures for pull requests and coding standards.
