import streamlit as st

# Define the folder path
image_folder = r"E:\Google Playstore Analytics project\New folder\graphs"

# List of image files and descriptions
plots = [
    {"file": "app type distribution graph.png", "title": "App Type Distribution", "description": "Most apps are free, designed to attract users initially and later monetize through ads or purchases."},
    {"file": "category wise installations graph.png", "title": "Category-wise Installations", "description": "Games and social media apps have the highest number of installations."},
    {"file": "free vs paid apps ratings.png", "title": "Free vs Paid Apps Ratings", "description": "Paid apps generally receive higher ratings as users expect premium quality."},
    {"file": "impact of last updates on ratings graph.png", "title": "Impact of Updates on Ratings", "description": "Frequent updates don’t always lead to better ratings, as other factors influence user satisfaction."},
    {"file": "number of updates over years graph.png", "title": "Number of Updates Over the Years", "description": "App updates have increased over the years to keep up with user demands and platform requirements."},
    {"file": "rating distribution graph.png", "title": "Rating Distribution", "description": "Most apps receive high ratings, indicating overall user satisfaction."},
    {"file": "revenue by category graph.png", "title": "Revenue by Category", "description": "Business and productivity apps generate the most revenue through subscriptions and premium features."},
    {"file": "sentiment distribution graph.png", "title": "Sentiment Distribution", "description": "Most reviews are positive, but some negative feedback highlights user concerns."},
    {"file": "top categories graph.png", "title": "Top Categories", "description": "Tools, Entertainment, and Productivity apps dominate the Play Store."},
    {"file": "top generes graph.png", "title": "Top Genres", "description": "Popular genres include Action, Casual, Tools, Education, and Entertainment."},
]

# Streamlit App
st.title("Google Play Store Analytics")
st.header("Visualizations")

# Loop through the plots and display each with its description
for i, plot in enumerate(plots):
    st.subheader(f"Plot {i + 1}: {plot['title']}")
    st.write(plot["description"])
    
    # Load and display images
    image_path = f"{image_folder}/{plot['file']}"
    st.image(image_path, use_column_width=True)
