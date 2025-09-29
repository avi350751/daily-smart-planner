import streamlit as st
import random
from helper import get_weather, get_temperature, get_news, summarize_news, smart_planner





def get_random_quote():
    quotes = [
        "It’s not who I am underneath, but what I do that defines me.",
        "It is never too late to be what you might have been.",
        "You can’t use up creativity. The more you use, the more you have.",
        "Man is not made for defeat. A man can be destroyed but not defeated.",
        "Hope is a good thing, maybe the best of things. And no good thing ever dies.",
        "Champions keep playing until they get it right.",
        "It always seems impossible until it’s done.",
        "Do what you can, with what you have, where you are"
    ]
    return random.choice(quotes)

def get_random_image():
    images = [
        "https://unsplash.com/photos/photo-of-silhouette-photo-of-man-standing-on-rock-U3C79SeHa7k",
        "https://unsplash.com/photos/man-wearing-black-jacket-fzcluHBur3o",
        "https://unsplash.com/photos/brown-ceramic-mug-on-blue-and-white-ceramic-plate-nzus-1oiN0A",
        "https://unsplash.com/photos/woman-doing-yoga-meditation-on-brown-parquet-flooring-NTyBbu66_SI",
        "https://unsplash.com/photos/turned-on-always-smile-led-signage-Of7fPGRSz_4",
        "https://unsplash.com/photos/a-man-standing-next-to-a-bike-holding-a-basket-of-flowers-tRMFUu7etds"
    ]
    return random.choice(images)


def home_page():
    st.title("Welcome to YDP - Your Daily Planner")
    st.markdown("----------")
    st.subheader("Thought of the day - ")
    st.info(f'"{get_random_quote()}"')
    st.image(get_random_image(),caption="A beautiful morning to start your day!", width="stretch")
    st.markdown("----------")
    st.write("Use the sidebar on the left to get your daily updates")

def weather_news_page():
    st.header("Get weather updates of your city")
    city = st.text_input("Enter your city name: ")
    if st.button("Get Weather Updates"):
        if city:
            weather_report = get_temperature(city)
            if weather_report:
                st.subheader(f"Weather Update: {weather_report}")
                st.success("Weather updates fetched successfully!")
            else:
                st.error("Could not fetch weather data. Please try again.")
        else:
            st.warning("Please enter a city name.")
    

def interest_news_page():
    st.header("Get news updates based on your interests")
    interest = st.text_input("Enter your interests (e.g Technology, Sports, Health):", "Technology")
    if st.button("Get news on your topic of interest"):
        with st.spinner("Fetching news...."):
            if interest:
                articles = get_news(interest)
                title = []
                url = []
                image_url = []
                for i in articles:
                    title.append(i.get("title"))
                    url.append(i.get("url"))
                    image_url.append(i.get("urlToImage"))
                if not articles:
                    st.error("Could not fetch news data. Please try again.")
                col1, col2, col3, col4, col5 = st.columns(5)
                with col1:
                    st.subheader(title[0])
                    st.markdown("-------")
                    st.image(image_url[0])
                    st.markdown("-------")
                    st.write(f"Read more here: {url[0]}")
                    st.markdown("--------")
                    st.write(summarize_news(url[0]))
                with col2:
                    st.subheader(title[1])
                    st.markdown("-------")
                    st.image(image_url[1])
                    st.markdown("-------")
                    st.write(f"Read more here: {url[1]}")
                    st.markdown("--------")
                    st.write(summarize_news(url[1]))
                with col3:
                    st.subheader(title[2])
                    st.markdown("-------")
                    st.image(image_url[2])
                    st.markdown("-------")
                    st.write(f"Read more here: {url[2]}")
                    st.markdown("--------")
                    st.write(summarize_news(url[2]))
                with col4:
                    st.subheader(title[3])
                    st.markdown("-------")
                    st.image(image_url[3])
                    st.markdown("-------")
                    st.write(f"Read more here: {url[3]}")
                    st.markdown("--------")
                    st.write(summarize_news(url[3]))
                with col5:
                    st.subheader(title[4])
                    st.markdown("-------")
                    st.image(image_url[4])
                    st.markdown("-------")
                    st.write(f"Read more here: {url[4]}")
                    st.markdown("--------")
                    st.write(summarize_news(url[4]))
                st.success("News fetched successfully!")
    else:
        st.warning("Please enter your interest.")

def my_planner():
    st.header("Your Smart Planner")
    city = st.text_input("Enter your city name: ")
    if st.button("Let's Plan..."):
        if city:
            plan = smart_planner(city)
            if plan:
                st.subheader("Here's your plan for the day:")
                st.info(plan)
                st.success("Plan created successfully!")
            else:
                st.error("Could not create a plan. Please try again.")
        else:
            st.warning("Please enter a city name.")


# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
st.sidebar.markdown("---")
page_option = st.sidebar.radio("Choose a page:", ("Home", "Get Weather of your City", "News by Interest", "Smart Planner"))
st.sidebar.markdown("---")


# --- Page Routing ---
if page_option == "Home":
    home_page()
elif page_option == "Get Weather of your City":
    weather_news_page()
elif page_option == "News by Interest":
    interest_news_page()
elif page_option == "Smart Planner":
    my_planner()
    
