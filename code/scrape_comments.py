import os
import pandas as pd
from googleapiclient.discovery import build
from dotenv import load_dotenv

# Cargar clave API desde archivo .env
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

# Cliente de YouTube API
youtube = build("youtube", "v3", developerKey=api_key)

def get_comments(video_id, max_comments=300):
    comments = []
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    )
    response = request.execute()

    while response and len(comments) < max_comments:
        for item in response["items"]:
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "comment_id": item["id"],
                "text": snippet["textDisplay"],
                "video_id": video_id,
                "video_title": snippet.get("videoTitle", "Unknown")
            })
        if "nextPageToken" in response and len(comments) < max_comments:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=response["nextPageToken"],
                textFormat="plainText"
            )
            response = request.execute()
        else:
            break
    return comments

# IDs de videos de ejemplo
video_ids = ["dQw4w9WgXcQ", "Ks-_Mh1QhMc"]

all_comments = []
for vid in video_ids:
    print(f"Scrapeando video: {vid}")
    comments = get_comments(vid)
    all_comments.extend(comments)

df = pd.DataFrame(all_comments)
df.to_csv("data/dataset.csv", index=False)
print(f"Listo. Comentarios guardados: {len(df)}")
