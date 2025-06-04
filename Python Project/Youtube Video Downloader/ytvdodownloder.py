## Single Video Download From yt
# from pytube import YouTube
#
# link = "https://www.youtube.com/watch?v=1i46vwdnIbw"  # enter youtube link here
# youtube_1 = YouTube(link)
#
# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)
#
# videos = youtube_1.streams.all()  # All Format
#
# videos = youtube_1.streams.all()   # Only Audio Format
#
# vid = list(enumerate(videos))
# for i in vid:
#     print(i)
# print()
# strm1 = int(input("enter : "))
# videos[strm1].download()
# print("Download Successfully !!!")



## Download Playlist From yt
# from pytube import Playlist
#
# py = Playlist("https://www.youtube.com/watch?v=y28jIn8jdi0&list=PLfP3JxW-T70FcAYcw4vAppLpiw3AdsAU-&index=3")
# print(f'Downloading : {py.title}')
#
# for video in py.videos:
#     video.streams.first().download()


#--------------------------------------------------------------------------------------------------

# ------- Single Video Download on Youtube -------
from pytubefix import YouTube
from pytubefix.cli import on_progress
link = input("Enter a Youtube Video Link : ")
yt = YouTube(link)
print(yt.title)
ys = yt.streams.get_highest_resolution()
ys.download()
print("Download Completed !!!")


# ----- Playlist Download on Youtube --------
# from pytubefix import Playlist
# from pytubefix.cli import on_progress
# link = input("Enter Youtube Playlist Link : ")
# yt = Playlist(link)
# print(yt.title)
# for video in yt.videos:
#      ys = video.streams.get_highest_resolution()
#      ys.download()
# print("Download Complete !!!")

#--------------------------------------------------------------------------------------------------








