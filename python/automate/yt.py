import pytube

a = input(str("please enter the url of the video you want to download\n   "))

youtube = pytube.YouTube(a)

streams = youtube.streams.all()
for i in streams:
    print(i)

# video = youtube.streams.get_by_res(480)

# video.download(Users/harshbhanushali/Desktop/youtube)

# print(done)

