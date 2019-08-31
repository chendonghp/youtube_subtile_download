import datetime
import re
# https://pypi.org/project/youtube-transcript-api/
from youtube_transcript_api import YouTubeTranscriptApi
# https://pypi.org/project/python-youtube/
from pyyoutube import Api
import requests
from bs4 import BeautifulSoup
import os

api_key = 'AIzaSyBQCHkVYIrge50clXARbUU_NsYnmybVeXM'


class YTSubDownload(YouTubeTranscriptApi, Api ):
    def __init__(self, video_id=None, dir=None, video_url=None, api_key=api_key, proxies=None):
        if video_id is None:
            self.video_id = re.search(r'\?v=(.*)&', video_url).group(1)
        else:
            self.video_id = video_id
        self.dir = dir
        super().__init__(api_key=api_key, proxies=proxies)

    @property
    def video_title(self, video_id=None):
        if video_id is None:
            video_id = self.video_id
        return self.get_video_info(video_id=video_id).snippet.title

    @classmethod
    def _sec_to_HMS(cls, sec: int) -> str:
        time = str(datetime.timedelta(seconds=sec))
        return re.sub(r'(\d+:)(\d+:)(\d+)\.(\d+)',
                      lambda x: x.group(1).zfill(3) + ''.join(x.group(2, 3)) + ',' + x.group(4)[:3], time)

    def sub_download(self, video_id=None, dir=None, file_name=None):
        if video_id is None:
            video_id = self.video_id
        if file_name is None:
            file_name = self.video_title + '.srt'
        if dir is None:
            if self.dir:
                if not os.path.isdir(self.dir):
                    os.mkdir(self.dir)
                file_name = os.path.join(self.dir, file_name)
        else:
            if not os.path.isdir(dir):
                os.mkdir(dir)
            file_name = os.path.join(dir, file_name)
        subs = self.get_transcript(video_id=video_id)
        fixed_susbs = []
        for i, sub in enumerate(subs):
            # abstract the subtitles form tht dict subs
            s = ''
            s = str(i + 1) + '\n'
            s = s + self._sec_to_HMS(sub['start']) + ' --> ' + self._sec_to_HMS(sub['start'] + sub['duration']) + '\n'
            s = s + sub['text'] + '\n\n'
            fixed_susbs.append(s)
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(fixed_susbs)


class Video_ids(Api):
    youtube_playlist_url_prefix = 'https://www.youtube.com/playlist?list='

    def __init__(self, playlist_url=None, proxies=None):
        self.playlist_url = playlist_url
        super().__init__(api_key=api_key, proxies=proxies)

    @property
    def playlist_id(self, playlist_url=None):
        # resolve playlist_id
        if playlist_url is None:
            playlist_url = self.playlist_url
        playlist_id = re.search(r'\?list=(.*)?&?', playlist_url).group(1)
        return playlist_id

    @property
    def playlist_title(self, playlist_id=None):
        # get playlist_title
        if playlist_id is None:
            playlist_id = self.playlist_id
        playlist_url = Video_ids.youtube_playlist_url_prefix + playlist_id
        r = requests.get(playlist_url)
        soup = BeautifulSoup(r.content,features="html.parser")
        soup.find_all('div', id="microformat")
        playlist_title = soup.title.contents[0][:-10]
        return playlist_title

    def get_video_ids(self) -> (str, list):
        # get playlist items
        playlist_items = self.get_playlist_item(playlist_id=self.playlist_id)
        video_counts = playlist_items[1]['totalResults']
        playlist_items = self.get_playlist_item(playlist_id=self.playlist_id, count=video_counts)
        return (self.playlist_title, [playlist_items[0][i].snippet.resourceId.videoId for i in range(video_counts)])

if __name__=='__main__':
    # proxies = dict(http='socks5://127.0.0.1:1080',
    #                https='socks5://127.0.0.1:1080')
    proxies=None
    vids=Video_ids(playlist_url = 'https://www.youtube.com/playlist?list=PL5iJcUfx7xTfe4hf9wtXHY_wEcF0GWCER',
                   proxies=proxies)
    playlist_title, video_ids=vids.get_video_ids()
    [YTSubDownload(vid,dir=playlist_title,proxies=proxies).sub_download() for vid in video_ids]
