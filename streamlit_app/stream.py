import streamlit as st
import matplotlib.pyplot as plt
from sentiment_model.model import final_polarity_scores
from reddit_data.reddit_data import get_reddit_data

def main():
    st.title("SOCIAL MEDIA PRESENCE")

    username = st.text_input("Enter Reddit Username:")
    num_posts = st.slider("Number of Posts to Analyze", 1, 10, 1)

    if st.button("Analyze"):
        if not username:
            st.warning("Please enter a Reddit username.")
        else:
            top_post, top_comments = get_reddit_data(username, num_posts)
            scores = [final_polarity_scores(comment) for comment in top_comments]
            positive_scores = [score.get('roberta_pos', 0) for score in scores]
            negative_scores = [score.get('roberta_neg', 0) for score in scores]
            neutral_scores = [score.get('roberta_neu', 0) for score in scores]

            total_positive = sum(positive_scores)
            total_negative = sum(negative_scores)
            total_neutral = sum(neutral_scores)

            st.subheader("Results")
            st.write(f"Username: {username}")
            st.write(f"Top Post: {top_post}")
            st.write("Top Comments:")
            for i, comment in enumerate(top_comments):
                st.write(f"{i+1}. {comment}")

            st.subheader("Total Sentiment Score")
            st.write(f"Total Positive Score: {total_positive}")
            st.write(f"Total Neutral Score: {total_neutral}")
            st.write(f"Total Negative Score: {total_negative}")

            labels = 'Positive','Negative','Neutral'
            sizes = [total_positive,total_negative,total_neutral]
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
                    shadow=True, startangle=90)
            ax1.axis('equal')

            st.pyplot(fig1)
if __name__ == "__main__":
    main()
