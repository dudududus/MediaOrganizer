import os
from media_processor import analyze_media
from database import init_db, insert_media

conn = init_db()
media_folder = "media"

for file in os.listdir(media_folder):
    if file.endswith((".mp3", ".wav", ".mp4", ".jpg", ".png")):
        analysis = analyze_media(file)
        print(f"{file}: {analysis}")
        insert_media(conn, file, tags=analysis, description=analysis)
