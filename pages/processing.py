import streamlit as st
from st_pages import show_pages_from_config, add_page_title

add_page_title()
show_pages_from_config()

st.markdown(
    """
    ### Data Source and Collection
    The data is sourced from electronic mail (eml) files uploaded to a Wordpress site. As of October 2019, there were 1157 issues in the mailing list.
    Exported from WordPress database into XML format the source data was something like this:

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

    So it was relatively structured: it has a a date and time, a place, a description of an event and sometimes an address of a place and a source of information about this event. But it was not very clean: there were a lot of html tags, some of the addresses were missed and messed, and there were a lot of typos.

    ### Data Cleaning and Preprocessing
    
    Initial data cleaning was aided by regular expressions and common sense filtering to omit unrelated sections such as "News" columns, book reviews, and other literary news. 
    As a result we got a data in csv format with the following columns:

    - "Event Date": date and time of the event in naive format, e.g. "05.03.15 четверг 19.00"
    - "Event Description": description of the event in text format,
    - "Info Source": short description of the source of information about the event, e.g. "соб. инф.",
    - "Issue": title if the mailing list issue, e.g. "SPbLitGuide 15-03-1",
    - "Permalink": link to the issue on the website, e.g. "https://isvoe.ru/spblitgid/2015/03/05/spblitguide-15-03-1/",
    - "Publication Date": date of the issue publication, e.g. "2015-03-05".

    After this processing we've got 44 930 records about the events, but in facts many of them were repeted in different issues, because each event can be announced several times before it happens.
    
    Pandas and difflib libraries were employed for advanced data cleaning and standardization, especially for venue names and addresses that had variations and typographical errors.

    After cleaning, the dataset contains:

    - 14 498 literary events
    - 862 venues
    - 817 unique addresses

    """
    
)

