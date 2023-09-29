import csv
from ytb_dl_function import get_ytb_url, dl_ytb_url

count = 0

search_keyword_array = []
with open("Spotify_playlist_dl.csv",'r') as csvfile :
    file_reader = csv.reader(csvfile)
    for row in file_reader :
        search_keyword = row[0] + " - " + row[1]
        search_keyword_array.append(search_keyword)

for keyword in search_keyword_array :
    try :
        url_test_to_dl = get_ytb_url(keyword)
    except :
        pass
    count += 1
    path_to_music = dl_ytb_url(url_test_to_dl, "/home/nicolas/Bureau/test_song", keyword)


print (str(count) + "songs downloaded and " + str(len(search_keyword)) + "songs on the file")
