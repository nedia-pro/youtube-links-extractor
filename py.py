import yt_dlp
import pandas as pd

df = pd.read_excel("Classeur1.xlsx")

def get_youtube_url(query):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'extract_flat': True,
        'force_generic_extractor': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            result = ydl.extract_info(f"ytsearch1:{query}", download=False)
            video = result['entries'][0]
            return f"https://www.youtube.com/watch?v={video['id']}"
        except Exception:
            return "nothing"


df['الرابط يوتيوب'] = df.apply(lambda row: get_youtube_url(f"{row['Artist']} - {row['Song']}"), axis=1)


df.to_excel("your_file_with_urls.xlsx", index=False)
