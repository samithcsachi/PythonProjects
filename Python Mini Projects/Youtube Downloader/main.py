from sys import argv
import yt_dlp

def main():
    print("Hello from youtube-downloader!")
    

    if len(argv) < 2:
        print("Error: Please provide a YouTube link.")
        print("Usage: python main.py <url>")
        return

    link = argv[1]


    ydl_opts = {
        'format': 'best',  
        'outtmpl': '%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching video information...")

            info = ydl.extract_info(link, download=False)

            print("Title: ", info.get('title'))
            print("Number of views: ", info.get('view_count'))
            print("Length of video: ", info.get('duration'), "seconds")

            print("Downloading...")
            ydl.download([link])
            print("Download completed!")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()