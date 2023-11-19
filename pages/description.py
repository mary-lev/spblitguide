import streamlit as st

from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

st.markdown(
    """
    [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10086515.svg)](https://doi.org/10.5281/zenodo.10086515) [![Data License](https://img.shields.io/badge/Data%20License-CC%20By%20NC%204.0-red.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

    ```bibtex
    @dataset{levchenko_2023_10086515,
        author       = {Levchenko, Maria},
        title        = {{Literary Events in Saint Petersburg (1999-2019) 
                        from SPbLitGuide Newsletters}},
        month        = nov,
        year         = 2023,
        publisher    = {Zenodo},
        version      = {1.0},
        doi          = {10.5281/zenodo.10086515},
        url          = {https://doi.org/10.5281/zenodo.10086515}
    }
    ```

    The dataset originates from **SPbLitGuide**, a long-standing newsletter maintained by Daria Sukhovey since May 1999, 
    focusing on the primary events of St. Petersburg's literary life. The newsletter has undergone several hosting changes 
    over the years: it was initially published on http://levin.rinet.ru, moved to the Krupskaya Book Fair website from 2010 to 2015, 
    and has since been hosted by the ["One's Own Publishing House" website](https://isvoe.ru/spblitgid/). For the past two decades, 
    subscribers have received multiple announcements of literary events in St. Petersburg each month. 
    The data set at hand comprises 1255 issues of this newsletter, spanning a 20-year period until October 2019. 
    The primary aim is to extract and analyze event announcements through text processing methodologies, including Python scripts, 
    regular expressions, and machine learning algorithms.

    The dataset contains:

    - 14 498 literary events
    - 862 venues
    - 817 unique addresses

    ### Limitations

    The dataset is subject to several limitations:

    - Perspective Bias: The data predominantly reflects Dar'ia Sukhovei's perspective, initially focusing on events that interested her and her literary circle, although later expanding in scope. This perspective has shaped the newsletter since its inception.
    - Event Coverage: Despite the author's deep integration into St. Petersburg's literary community and her attention to detail, some events might have been inadvertently excluded. The author's active participation in the literary scene provides a rich but potentially selective representation of events.
    - Inclusivity of Cultural Events: While the newsletter covers a range of cultural activities including cinema, art, and music, alongside literary events, there is no guarantee that these spheres are represented as comprehensively as the literary events. This could result in a selection bias towards literary events.
    - Temporal and Geographical Scope: The dataset is limited to events up to a certain year and focuses primarily on St. Petersburg, which may exclude relevant regional events and recent developments.
    - Data Quality and Consistency: Variability in data collection and reporting methods over time could affect the consistency and reliability of the dataset for longitudinal studies.
    - Extraction and Cleaning Methodology: The manual and automated processes used in data cleaning and entity extraction may introduce errors or biases.
    - Unrecorded Changes: Details of events, such as venue or time changes, might not be captured if they occurred last-minute.
    


    
"""
)