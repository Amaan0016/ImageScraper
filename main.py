from datetime import datetime
import instaloader

L = instaloader.Instaloader()

search = input("Enter Hashtag: ")
limit = int(input("How many posts to download: "))

hashtag = instaloader.Hashtag.from_name(L.context, search)

no_of_downloads = 0
for post in hashtag.get_posts():
    if no_of_downloads == limit:
        break
    print(f"Downloading post {post.url}")
    L.download_post(post, target="#"+search)
    no_of_downloads += 1

print(f"Downloaded {no_of_downloads} posts with the hashtag #{search}")
