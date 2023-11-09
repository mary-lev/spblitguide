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
    and has since been hosted by the ["One's Own Publishing House" website](https://isvoe.ru/spblitgid/). For the past two decades, subscribers have received multiple announcements of literary events in St. Petersburg each month. The data set at hand comprises 1255 issues of this newsletter, spanning a 20-year period until October 2019. The primary aim is to extract and analyze event announcements through text processing methodologies, including Python scripts, regular expressions, and machine learning algorithms.

    ### Data Source and Collection
    The data is sourced from electronic mail (eml) files uploaded to a Wordpress site. As of October 2019, there were 1157 issues in the mailing list. The Python programming language was used to scrape these files, particularly focusing on event announcements.

    ### Data Cleaning and Preprocessing
    Initial data cleaning was aided by regular expressions and common sense filtering to omit unrelated sections such as "News" columns, book reviews, and other literary news. Pandas and difflib libraries were employed for advanced data cleaning and standardization, especially for venue names and addresses that had variations and typographical errors.
    After cleaning, the dataset contains:

    - 14 498 literary events
    - 862 venues
    - 817 unique addresses

    ### Additional Data Representations

    - **Literary Life Map of St. Petersburg**: Geographic locations for 862 venues were identified and mapped.
    - **Graph of Characters**: A graph depicting individuals who have participated in events over the 20-year span was compiled, using named entity recognition and neural network techniques.

    ### Limitations

    The dataset lacks some textual sections like book reviews, "News" columns, and other literary reports.
    Name and address fields had to be extensively cleaned due to inconsistencies and errors, which might introduce some level of inaccuracy.

    ### Potential Applications

    The cleaned and structured dataset offers valuable insights into the literary landscape of St. Petersburg, facilitating analyses such as trends in literary events, identification of key venues, and community engagement over two decades.

    ### ⇨ [Data Model](Model)


    
"""
)