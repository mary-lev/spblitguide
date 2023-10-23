import streamlit as st
from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()


st.markdown(
    """
    This project is centered on the construction and initial analysis of a dataset derived from **SPbLitGuide**, 
    a newsletter founded by *Daria Sukhovey* in May 1999. The dataset comprises 1255 issues released up to October 2019 
    and focuses specifically on the announcements of literary events in St. Petersburg. 
    
    The project's principal objectives are twofold: first, to systematically organize 
    this corpus of newsletters into a structured dataset; and second, to conduct a preliminary analysis 
    that will serve as a foundation for more extensive scholarly investigations.

    ### Target Audience

    - Academic Researchers: Ideal for scholars in literary studies, cultural analysis, and social sciences, this dataset lays the groundwork for longitudinal research in understanding the literary dynamics of St. Petersburg.
    - Cultural Analysts and Historians: The preliminary analysis and structured data offer an entry point for exploring historical shifts in literary venues, themes, and community participation.

    Through methods such as text analytics and machine learning algorithms, the SPbLitGuide Data Analysis Project aims to deliver a robust dataset accompanied by a preliminary analysis. This will provide a critical foundation for various stakeholders interested in the comprehensive study of St. Petersburg's literary environment.

    ### ⇨ [Data Description](Dataset)

"""
)