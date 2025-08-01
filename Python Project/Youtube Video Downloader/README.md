# 📥 YouTube Video & Playlist Downloader
This project is a Python-based YouTube downloader that allows users to download:
- 🎬 Single YouTube videos

- 📂 Entire YouTube playlists in the highest available resolution using the pytubefix library.


## 🚀 Features

- Download single videos in highest resolution

- Download complete playlists with one click

- Displays video titles before download

- Command-line interface for ease of use

## 🛠️ Requirements

- Python 3.x

- ```
  pytubefix
  ```

Install dependencies:

``` 
pip install pytubefix
```

# 📁 How to Use
### ▶️ Single Video Download
1. Run the script.

2. Paste the video link when prompted.

3. Video title will be displayed.

4. The video will be downloaded in the highest resolution.

```
Enter a Youtube Video Link : https://www.youtube.com/watch?v=dQw4w9WgXcQ
Downloading: Rick Astley - Never Gonna Give You Up
Download Completed !!!
```

### 📺 Playlist Download
_(Uncomment the Playlist section in the code to enable this feature)_

1. Paste your YouTube playlist link.

2. The script will iterate and download all videos from the playlist.

```
Enter Youtube Playlist Link: https://www.youtube.com/playlist?list=...
Downloading: My Python Tutorial Playlist
Download Complete !!!
```

## 📄 Project Structure

```
youtube_downloader.py    # Main Python script
README.md                # Project documentation
```

## ⚠️ Note

- Only public videos and playlists can be downloaded.

- Make sure the internet connection is stable to avoid errors.

## 🙌 Author
**Tejas Talole**

Built as a real-world Python utility project to automate video downloading.



