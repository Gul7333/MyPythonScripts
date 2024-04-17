import youtube_dl

def download_subtitles(channel_url):
    ydl_opts = {
        'writesubtitles': True,
        'allsubtitles': True,
        'skip_download': True,
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

# Example usage:
channel_url = 'https://www.youtube.com/channel/alratv'
download_subtitles(channel_url)

