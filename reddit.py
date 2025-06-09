import requests
import argparse

def fetch_top_posts(subreddit, limit=5):
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    headers = {"User-Agent": "RedditCLI/0.1 (by u/pterdactyl)"}
    params = {"limit": limit, "t": "day"}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(f"Error: Unable to fetch data (status code {response.status_code})")
        return
    
    data = response.json()
    posts = data["data"]["children"]
    
    print(f"\nTop {limit} posts from r/{subreddit}:\n")
    for idx, post in enumerate(posts, start=1):
        title = post["data"]["title"]
        comments = post["data"]["num_comments"]
        upvotes = post["data"]["ups"]
        print(f"[{idx}] {title}")
        print(f"    💬 {comments} comments | 👍 {upvotes} upvotes\n")

def main():
    parser = argparse.ArgumentParser(description="Reddit CLI Reader")
    parser.add_argument("--subreddit", type=str, required=True, help="Subreddit to fetch from")
    parser.add_argument("--limit", type=int, default=5, help="Number of posts to show")

    args = parser.parse_args()

    fetch_top_posts(args.subreddit, args.limit)

if __name__ == "__main__":
    main()