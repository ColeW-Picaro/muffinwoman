# Filename: video.py
# Author: Adapted from https://github.com/joek13/py-music-bot/blob/master/src/video.py
# Desc: 

from __future__ import unicode_literals
import discord
import youtube_dl

YTDL_OPTS = {
    "default_search": "ytsearch",
    "format": "bestaudio/best",
    "quiet": True,
    "extract_flat": "in_playlist",
    'postprocessors': [{
      'key': 'FFmpegExtractAudio',
      'preferredcodec': 'mp3',
      'preferredquality': '192',
    }]
}

class Video:
  def __init__(self, url, user):
    self.url = url
    self.user = user
    with youtube_dl.YoutubeDL() as ydl:
      video = self._get_info(url)
      video_format = video["formats"][0]
      self.stream_url = video_format["url"]
      self.video_url = video["webpage_url"]
      self.title = video["title"]
      self.uploader = video["uploader"] if "uploader" in video else ""
      self.thumbnail = video["thumbnail"] if "thumbnail" in video else None
      self.user = user

  def _get_info(self, url):
      with youtube_dl.YoutubeDL(YTDL_OPTS) as ydl:
        info = ydl.extract_info(url, download=False)
        video = None
        if "_type" in info and info["_type"] == "playlist":
          return self._get_info(
            info["entries"][0]["url"])  # get info for first video
        else:
          video = info
        return video
