import pandas as pd
import streamlit as st
from PIL import Image
from st_pages import show_pages_from_config, add_page_title

add_page_title()
show_pages_from_config()

st.markdown(
    """
    ### Data Source and Collection
    """)

image = Image.open('pipeline.png')
st.image("pipeline.png", caption='Data Pipeline')
    
st.markdown(
    """
    The data was sourced from electronic mail (eml) files uploaded to a WordPress site. 
    As of October 2019, the mailing list contained 1,157 issues. The source data, initially in the WordPress database, 
    was exported into an XML format, resembling the following structure:

    ```html
        <post>
            <id>1</id>
            <Title>SPbLitGuide 15-03-1</Title>
            <Content><![CDATA[<b><i>05.03.15 четверг 19.00 Галерея "АРТ-ЛИГА" (<span class="js-extracted-address daria-action mail-message-map-link" data-action="map-up.showAddress" data-params="address=Пушкинская 10&amp;ids=2060000005087047874">Пушкинская <span class="mail-message-map-nobreak">10</span></span>, вход с <span class="js-extracted-address daria-action mail-message-map-link" data-action="map-up.showAddress" data-params="address=Лиговского, 53&amp;ids=2060000005087047874">Лиговского, <span class="mail-message-map-nobreak">53</span></span>, парадная налево, 7 этаж)</i></b>
                Большой поэтический вечер в самом начале весны! Дмитрий Артис, Борис Кутенков (Москва),Дмитрий Шабанов, Рахман Кусимов, Серафима Сапрыкина, Ася Анистратенко.
                [соб. инф.]

                <b><i>05.03.15 четверг 19.00 Библиотека Лермонтова (<span class="js-extracted-address daria-action mail-message-map-link" data-action="map-up.showAddress" data-params="address=Литейный пр., 19&amp;ids=2060000005087047874">Литейный пр., <span class="mail-message-map-nobreak">19</span></span>)</i></b>
                "Наполеоновские войны и Кавказ - взглядом Ермолова". Читает историк, публицист, главный редактор журнала «Звезда» - Яков Аркадьевич Гордин. Герой Наполеоновских войн, проконсул Кавказа, генерал от инфантерии и артиллерии Алексей Петрович Ермолов оставил обширную переписку. Письма Ермолова — неисчерпаемый источник сведений о его взглядах и планах, которые были осуществлены или остались лишь намерениями, они дают возможность приблизиться к пониманию масштабности фигуры их автора и проникнуть в психологический климат «ермоловской эпохи», помогают пролить свет на многие сюжеты истории. Эпистолярное наследие Ермолова является объектом многолетней исследовательской работы Я. А. Гордина. Яков Аркадьевич Гордин известен независимыми историческими исследованиями и специализируется на кризисных ситуациях русской политической истории XVIII—XIX веков; автор многих статей и ряда книг, в том числе «Ермолов», «Алексей Ермолов. Солдат и его империя», "Гибель Пушкина", "Между рабством и свободой", "Дуэли и дуэлянты", "Мятеж реформаторов". Историческая беллетристика с документальной основой и эссеистика на исторические темы – основные жанры творчества Я. А. Гордина с середины 1970-х гг. Яков Аркадьевич Гордин за многие годы литературного и просветительского труда внёс неоценимый вклад в развитие просветительской мысли.
                [лермонтовка]

                <b><i>05.03.15 четверг 19.30 Антикафе "О'Лень" (БЦ «Остров», <span class="js-extracted-address daria-action mail-message-map-link" data-action="map-up.showAddress" data-params="address=Средний пр В.О. 36/40&amp;ids=2060000005087047874">Средний пр В.О. <span class="mail-message-map-nobreak">36/40</span></span>, угол Среднего и 9й линии, 3 этаж ) тариф антикафе 2р./мин</i></b>
                Космическо-эзотерическо-п<wbr />оэтический вечер Мари Stell "Трансцендентность". Погружение в мир таинственных образов и чувственных переживаний, не поддающихся контролю форм
    ```

    This data was relatively structured, containing dates and times, places, descriptions of events, and occasionally, addresses and sources of information. However, it also included a considerable amount of HTML tags, missing or inconsistent addresses, and numerous typos.

    ### Data Cleaning and Preprocessing
    
    Initial data cleaning involved using regular expressions and common sense filtering to remove unrelated sections, 
    such as news columns, book reviews, and other literary news. The cleaned data was converted into a CSV format with the following columns:

    - "Event Date": date and time of the event in naive format, e.g. "05.03.15 четверг 19.00"
    - "Event Description": description of the event in text format,
    - "Info Source": short description of the source of information about the event, e.g. "соб. инф.",
    - "Issue": title if the mailing list issue, e.g. "SPbLitGuide 15-03-1",
    - "Permalink": link to the issue on the website, e.g. "https://isvoe.ru/spblitgid/2015/03/05/spblitguide-15-03-1/",
    - "Publication Date": date of the issue publication, e.g. "2015-03-05".

    After processing, we obtained 44,930 records of events. Many events were repeated across different issues, 
    as the issues were published 3-5 times a month, and each event could be announced several times before it occurred.

    ### Duplicate Filtering
    We needed to filter out duplicates to retain only unique events. This task involved more than identifying exact duplicates due to potential slight variations in event descriptions, such as changes in dates, times, or venues. 
    Fuzzy matching algorithms were applied to identify and eliminate these duplicates, resulting in a total of 14,498 unique events.

    ## Named Entity Recognition

    Our goal was to extract and analyze various types of named entities from the records, including addresses, 
    venue names, dates. Dates, addresses, and places are typically mentioned in the first line of 
    an event's description and are often marked with HTML tags like <b><i> or <strong><em>, 
    making them relatively straightforward to extract using regular expressions.

    The Natasha library, designed for processing Russian language, was utilized to extract this information, 
    which was then placed into separate columns. The Pandas and difflib libraries were used for advanced data cleaning and standardization, 
    particularly for standardizing venue names and addresses that had variations and typographical errors.

    After cleaning, the dataset includes:

    - 14 498 literary events
    - 862 venues
    - 817 unique addresses

    ### Persons' Names Extraction

    We utilized the DeepPavlov library for extracting persons' names. Based on neural network models, this tool was effective 
    for Russian language but not without errors. It successfully extracted a comprehensive list of names and surnames, 
    which we then manually reviewed and refined for accuracy.

    For normalization of Russian names, which often vary due to grammatical cases and different writing styles 
    (e.g., Дарья Суховей, Д. Суховей, Даша Суховей), we employed the Natasha library. This tool effectively handled the variations in name forms.

    Additionally, we explored the use of Large Language Models (LLMs) like ChatGPT-3.5 and ChatGPT-4 
    for name extraction. Although these models demonstrated superior performance, they were not incorporated 
    into the final dataset version due to their slower processing speeds and higher computational resource demands. 
    A comparative analysis of these models can be found in our [Colab notebook](https://colab.research.google.com/drive/1Tu8UgakY8QVjmwLmgcV-YPd-4Zr9jlci#scrollTo=HRNbq5B71CJU).

    ### Geographical Coordinates Extraction

    We used the Yandex Geocoder API to extract geographical coordinates from addresses. After cleaning and standardizing the addresses,
    we obtained 817 unique addresses. The Yandex Geocoder API was used to extract geographical coordinates from these addresses.
    We put the latitude and longitude coordinates into separate columns.

    """
)

df = st.cache_data(pd.read_csv)("data/addresses.csv", index_col=0)
st.dataframe(df)
    


