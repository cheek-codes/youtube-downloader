from pytube import YouTube

while True:

    def download():
        link = input("What are you trying to download? URL: ")
        yt = YouTube(link)

        yd = yt.streams.get_highest_resolution()
        yd.download("/Users/sandy/Downloads")

        print("Downloading:", yt.title, "... Wait for it ...")
        print("Done\n")

        i_finished = input("If you're done, just type \"done\". If not done, press any key and then ENTER ").lower()
        if i_finished == "done":
            quit()
        else:
            download()

    download()