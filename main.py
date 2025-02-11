from yt_dlp import YoutubeDL
import os

def download_youtube_video(url, filename, output_path ="songs"):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f"{output_path}/{filename}",
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Downloaded successfully: {output_path}")
    except Exception as e:
        print(f"Error downloading video: {e}")


if __name__ == "__main__":
    # Example usage
    # link , url , director...
    download_youtube_video('https://www.youtube.com/watch?v=VdImIav4b8U', 'songname')


# required https://www.gyan.dev/ffmpeg/builds/