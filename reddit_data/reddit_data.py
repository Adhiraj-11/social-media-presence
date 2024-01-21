import praw 

def get_reddit_data(username, num_posts=1):
    client_id = 'XZd0V9uHIUS3l7D2BaYBGg'
    client_secret = 'UEEsi-4g8nupxFSCuoC7YzKD03sfEw'
    user_agent = 'SA reddit'

    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent,
    )

    user_submissions = reddit.redditor(username).submissions.new(limit=num_posts)

    top_post = None
    top_comments = []

    for submission in user_submissions:
        top_post = submission.title

        # Retrieve top-level comments for the submission
        submission.comments.replace_more(limit=1)  # Limit to one top-level comment
        for comment in submission.comments:
            top_comments.append(comment.body)

    return top_post, top_comments