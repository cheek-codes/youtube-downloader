from pytube import YouTube


def download():
    while True:
    
        link = input("What are you trying to download? URL: ")
        yt = YouTube(link)

        print(f"\nDownloading: {yt.title} ... Wait for it ...")
        
        yd = yt.streams.get_highest_resolution()
        yd.download("E:/video-downloaded")

        print("\nDone\n")

        i_finished = input("If you're done, just type \"done\". If not done, press any key and then ENTER ").lower()
        if i_finished == "done":
            quit()

download()