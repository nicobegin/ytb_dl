# Import
 
from pytube import YouTube 
import os

import urllib.request
import re
from unidecode import unidecode


# Constant

PATH_TO_DL = "/home/nicolas/Bureau"

URL_TO_DL = "https://www.youtube.com/watch?v=90M60PzmxEE"


# Code 


#Search for a term and get the url

def get_ytb_url(search_keyword):

    search_keyword=("+").join(search_keyword.split(" "))
    search_keyword_unicode = unidecode(search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword_unicode)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    ytb_url_to_dl = ("https://www.youtube.com/watch?v=" + video_ids[0])
    return ytb_url_to_dl

#From a youtube url, a song name and the path to dl the song name, download the file and return the file name
def dl_ytb_url(ytb_url_to_dl, path_to_dl, song_name):
    video = YouTube(ytb_url_to_dl)
    #video_streams = video.streams.filter(file_extension='mp3')
        # We can add the line above if we want to dl the video 
    try :
        audio_stream = video.streams.filter(only_audio=True).first()
    except : 
        pass
    try : 
        out_file = audio_stream.download(path_to_dl)
    except : 
        pass
        #Next part is to rename it properly
    base, ext = os.path.splitext(out_file)
    path = os.path.dirname(out_file)
    new_file = path + "/" + song_name + '.mp3'
    os.rename(out_file, new_file)
    return new_file

def get_search_keyword_from_csv(path_to_csv):
    return


def get_ytb_url_from_playlist():
    # Get all the ytb url from a youtube playlist
    return

def compare_time_with_ytb_video(ytb_url):
    # Get the time (if given) of the music and compare it with the length of the youtube video
    # We need to adjust the precision of this function
    # If the length doesn't match we need to start again with the second video
    return()

def remove_accent(text):
    
    # unidecode('kožušček')
    return(text)