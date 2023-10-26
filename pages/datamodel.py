import streamlit as st
from st_pages import show_pages_from_config, add_page_title

add_page_title()
show_pages_from_config()

st.write("# Data Model 👋")



st.markdown(
    """
    The data model leverages Django's Object-Relational Mapping (ORM) 
    to map the dataset's schema to Python classes. The model consists of four main entities: 
    Person, Address, Place, and Event. Below is a description of each entity, their fields, 
    and the relationships among them.
    """
)
st.image("data/model.svg")

st.markdown(
    """
    ## Entities and Fields

    ### Person
    - name: CharField to store the first name.
    - second_name: CharField to store the middle name.
    - family: CharField to store the last name.
    - pseudonym: CharField to store any pseudonym.

    The Person class uniquely identifies a person by their name and family.

    ### Address
    - name: CharField to store the name of the address.
    - lon: DecimalField to store longitude.
    - lat: DecimalField to store latitude.

    ### Place
    - name: CharField to store the name of the place.

    ### Event
    - description: TextField for event description.
    - date: DateTimeField for the event date and time.
    - place: ForeignKey to the Place entity.
    - address: ForeignKey to the Address entity.
    - people: ManyToManyField connecting to the Person entity.

    ### Relationships

    A Person can be associated with multiple Events through a ManyToManyField.
    An Event has one Place and one Address associated with it via ForeignKey relationships.
    A Place can have multiple associated Addresses through the Events.

    ### Constraints and Ordering

    Person is constrained to have a unique combination of name and family.
    Event entities are ordered by their date.

    ## Pandas DataFrame
    The data is stored in a single pandas DataFrame with the objective of capturing literary events, 
    their venues, and attendees in St. Petersburg. Unlike a relational database model, 
    the DataFrame consolidates all the information into one table, with each row representing a unique event.

    ### Fields

    - id: Integer to uniquely identify each event.
    - event_description: String to store the description of the event.
    - address: String for the geographical location of the venue.
    - place_name: String for the name of the place where the event is held.
    - date: DateTime type for when the event is scheduled.
    - latitude: Float for the latitude coordinate of the venue.
    - longitude: Float for the longitude coordinate of the venue.
    - persons: List of Strings to store names of people associated with the event.

    ### Characteristics

    In-Memory Storage: The DataFrame exists in memory; it's not a persistent database.
    Flat Structure: No native support for relationships. All data points are flattened into individual fields.
    Flexible Schema: Easy to add or remove fields as needed.
    Indexing: Integer-based indexing is used for quick data retrieval.

    ### Constraints

    The id field should be unique to maintain the integrity of each record.

    ### Data Types

    - id: Integer
    - event_description: Object (typically String)
    - address: Object (typically String)
    - place_name: Object (typically String)
    - date: DateTime
    - latitude: Float64
    - longitude: Float64
    - persons: Object (typically List of Strings)

    The DataFrame allows for efficient querying, filtering, and analytics, 
    albeit without the relationship management and persistence features found in traditional databases.
    """
)