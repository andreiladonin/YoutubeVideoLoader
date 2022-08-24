import eel
from pytube import YouTube

SAVE_FOLDER = 'videos'

@eel.expose
def download_video(link:str, title):
    try: 
        yt = YouTube(link) 
    except: 
        return "Отсутствует интернет соедения"
    
    video = yt.streams.filter(subtype="mp4", progressive=True).order_by('resolution')[-1]
    video.download(SAVE_FOLDER, filename=f"{title}.mp4")
    return 'Видео загружено в папку videos' 

if __name__ == "__main__":
    print("init app")
    eel.init('web')
    eel.start('index.html', size=(500, 500))
