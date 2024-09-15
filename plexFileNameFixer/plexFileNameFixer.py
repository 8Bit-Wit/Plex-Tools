################################################
############  Dependancies  ####################
################################################
import ffmpeg
from os import listdir
from os.path import isfile, join
from pprint import pprint
import sys


################################################
###########  Global Variables  #################
################################################

plex_movie_dir = "\\\\8BNas\\Plex_Content\\plex\\movies" #Path to Plex Media Server Movies Directory


################################################
#############  Functions  ######################
################################################

def find_media_files(file_paths): #Creates array of movie paths
    movies = []
    for i in file_paths:
        if i.endswith(".mp4") or i.endswith(".mkv"):
            movies.append(i)
    return (movies)


def get_info(path): #Fetches JSON object of movie meta data 
    try:
        probe = ffmpeg.probe(f'{plex_movie_dir}/{path}')
        pprint(probe)
    except:
        print (f'Cannot Probe Media File {path}')
        return

    try:
        title = probe['format']['tags']['title']
    except:
        title = "NOTFOUND"
    
    try:
        date = f'({probe['format']['tags']['date']})'
    except:
        date = "(NOTFOUND)"

    try:
        codec = f"{probe['streams'][0]['codec_name']}"
    except:
        codec = "NOTFOUND"

    try:
        cod_w = int(f"{probe['streams'][0]['coded_width']}")
        if cod_w == 1920:
            res = '1080'
        elif cod_w > 1920:
            res = '4K'
        elif cod_w == 1280:
            res = '720'
        elif cod_w == 854:
            res = '480'
        else: res = 'NOTFOUND'

    except:
        res = "NOTFOUND"
    
    return f'{title} {date}.{res}.{codec}'

def api_search(m_title, m_year): #Used omdb api to fetch title, year, and IMDB ID information
    return

def find_all_files(dir): #Grabs all file paths in Plex Movie Directory
    file_paths = [f for f in listdir(dir) if isfile(join(dir, f))]
    return file_paths
    

###############################################
#################  Main  ######################
###############################################



#print(get_info(get_movies(onlyfiles)))
#pprint(ffmpeg.probe(f'{dir_path}/A League of Their Own (1992).mkv'))

plex_file_paths = find_all_files(plex_movie_dir)
movie_file_paths = find_media_files(plex_file_paths)

for movie_path in movie_file_paths:
    if movie_path == movie_file_paths[0]:
        print (movie_path)
        pprint (get_info(movie_path))

