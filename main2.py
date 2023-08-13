# FINAL CODE

import instaloader
import datetime
from PIL import Image
import os

def scrape_and_upscale_images(username):
    # Create an instance of Instaloader
    loader = instaloader.Instaloader()

    try:
        # Load the profile using the given username
        profile = instaloader.Profile.from_username(loader.context, username)

        # Create a folder for enhanced images
        enhanced_folder = f"{username}_enhanced"
        # os.makedirs(enhanced_folder, exist_ok=True)

        # Calculate the date 3 days ago
        current_date = datetime.date.today()
        days_to_subtract = datetime.timedelta(days=15) 
        date_threshold = current_date - days_to_subtract

        # Track the processed images
        processed_images = set()

        # Iterate over the profile's posts
        for post in profile.get_posts():
            # Download and enhance images
            if post.date_local.date() < date_threshold:
                break
            if not post.is_video and post.date_local.date() >= date_threshold:
                # Download the images from the post
                loader.download_post(post, target=username)

                # Get the list of downloaded image files
                image_files = [f for f in os.listdir(username) if f.endswith(".jpg")]
                print(image_files)
                # Process each image file
                for i, image_file in enumerate(image_files):
                    # Skip processing if the image has already been processed
                    if image_file in processed_images:
                        continue

                    # Rest of your code for enhancing images

                    # Add the processed image to the set
                    processed_images.add(image_file)

        print("Scraping and up-scaling completed.")
    except instaloader.exceptions.ProfileNotExistsException:
        print("Profile does not exist.")

# Scrape the profile and upscale the images
influencers = [
    "virat.kohli",
    "priyankachopra",
    "deepikapadukone",
    "ranveersingh",
    "aliaabhatt",
    "jacquelinef143",
    "nehakakkar",
    "bhuvan.bam22",
    "radhikaofficial",
    "dishapatani",
    "nakuulmehta",
    "ankushbahuguna",
    "masabagupta",
    "shreyajain26",
    "shreyagupto",
    "stylebyami",
    "dollysingh",
    "siddhantchaturvedi",
    "radhikasethh",
    "aranyajohar",
    "neetimohan18",
    "sejalkumar1195",
    "iamkirtikulhari",
    "beerbiceps",
    "srishtipatch",
    "maliniagarwal",
    "aashnashroff",
    "sonaldevraj",
    "shradha301",
    "hrithikroshan",
    "abishmathew",
    "dollysingh",
    "thatbohogirl",
    "mohanshakti",
    "giasaysthat",
    "bruisedpassports",
    "kittycatkarishma",
    "makhijadevashish",
    "nidhimohankamal",
    "radhikamerchant",
]
# print(len(influencers))
for i in influencers :
    scrape_and_upscale_images(i)