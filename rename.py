# The readme for this script gives detailed instructions, refer to it if you need any help

from googleapiclient.discovery import build
import os
from fuzzywuzzy import process

def get_playlist_videos(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.playlistItems().list(
        part='snippet',
        playlistId=playlist_id,
        maxResults=50  # (50 requests is the API limit. The script will loop if more then 50 videos. CHANGE THIS IF API IS RATE LIMITING FOR SOME REASON)
    )
    response = request.execute()

    videos = []
    while request:
        response = request.execute()
        for item in response['items']:
            title = item['snippet']['title']
            videos.append(title)
        request = youtube.playlistItems().list_next(request, response)

    return videos

def rename_files(videos, directory):
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()  # Ensure files are in alphabetical order

    print("Files in directory:")
    for file in files:
        print(file)
    print()

    if not files:
        print("No files found in the directory.")
        return

    for index, video_title in enumerate(videos):
        match = process.extractOne(video_title, files)
        if match is None:
            print(f"No match found for '{video_title}'")
            continue

        best_match, score = match
        print(f"Matching: '{video_title}' with '{best_match}' (Score: {score})")  # Debug log
        if score > 80:  # Adjust the threshold as needed
            new_name = f"{index + 1} {best_match}"
            print(f"Renaming: '{best_match}' to '{new_name}'")  # Debug log
            old_path = os.path.join(directory, best_match)
            new_path = os.path.join(directory, new_name)
            print(f"Old Path: {old_path}, New Path: {new_path}")  # Debug log
            try:
                os.rename(old_path, new_path)
            except FileNotFoundError as e:
                print(f"Error: {e}")
        else:
            print(f"No suitable match found for '{video_title}' with a score above 80.")

# Example usage
api_key = 'xxxxx'  # Replace with your YouTube Data API key, look at the readme if you need help with this.
playlist_id = 'xxxxx'  # Replace with your YouTube playlist ID (the characters after 'list=', if the link ends with '&pp=iAQB' do not include those characters as the playlist ID
directory = 'xxxxx'  # Replace with the path to your downloaded videos directory (if using Windows, add an r in front of the path, r'xxxxx'

videos = get_playlist_videos(api_key, playlist_id)
rename_files(videos, directory)
