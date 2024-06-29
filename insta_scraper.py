from instagram_private_api import Client, ClientError
import json
import os
from pymongo import MongoClient

def login_instagram(username, password):
    try:
        api = Client(username, password)
        print("Login Successful ")
        return api
    except ClientError as e:
        print(f"An error occurred during login: {e}")
        return None

def get_saved_posts(api):
    try:
        max_id = ''
        posts_info = []

        while True:
            saved_feed = api.saved_feed(max_id=max_id)
            saved_posts = saved_feed['items']

            for post in saved_posts:
                media_link = ''
                if post['media']['media_type'] == 1:  # Photo
                    if 'image_versions2' in post['media']:
                        media_link = post['media']['image_versions2']['candidates'][0]['url']
                elif post['media']['media_type'] == 2:  # Video
                    if 'video_versions' in post['media']:
                        media_link = post['media']['video_versions'][0]['url']

                post_info = {
                    'id': post['media']['pk'],
                    'caption': post['media'].get('caption', {}).get('text', ''),
                    'location': post['media'].get('location', {}).get('name', ''),
                    'account_name': post['media']['user']['username'],
                    'date': post['media']['taken_at'],
                    'media_type': post['media']['media_type'],
                    'media_link': media_link
                }
                posts_info.append(post_info)

            if 'next_max_id' in saved_feed:
                max_id = saved_feed['next_max_id']
            else:
                break

        print(f"Retrieved {len(posts_info)} saved posts.")
        return posts_info

    except ClientError as e:
        print(f"An error occurred while fetching saved posts: {e}")
        return []


def update_mongodb(posts_info):
    try:
        client = MongoClient('localhost', 27017)
        db = client['saved_posts']
        collection = db['posts']

        # Update the posts in the collection
        for post in posts_info:
            collection.update_one({'id': post['id']}, {'$set': post}, upsert=True)

        print("MongoDB update successful")
    except Exception as e:
        print(f"An error occurred while updating MongoDB: {e}")


def main():
    username = 'insta_vector_bot'
    password = 'vectorrector'
    
    api = login_instagram(username, password)
    
    if api:
        saved_posts = get_saved_posts(api)
    
    # Write saved_posts to a JSON file
    file_path = 'saved_posts.json'
    
    with open(file_path, 'w') as file:
        json.dump(saved_posts, file, indent=4)
        print(f'Saved posts written to {file_path}')

     # Update MongoDB with saved_posts
        update_mongodb(saved_posts)
        
if __name__ == "__main__":
    main()
