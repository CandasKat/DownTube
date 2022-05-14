from pytube import YouTube
from pyfiglet import Figlet
import pyfiglet.fonts
import os

f = Figlet(font='stop')
p = Figlet(font='straight')
print()
print("***************************************************************************************************")
print("***************************************************************************************************")
print()
print(f.renderText('DownTube'))
print()
print("***************************************************************************************************")
print("***************************************************************************************************")
print(p.renderText(" "* 60+ "by Candas..."))
print()
while True:
    secenek = input("Yeni bir video indirmek icin 'D' ye,\nSadece ses dosyasini indirmek icin 'S'ye,\nProgramdan cikmak icin 'Q'ya basin: ")
    if secenek == "D" or secenek == "d":
        print()
        link = input("Linki buraya kopyalayin: ")
        yt = YouTube(link)

        print()
        print("Baslik: ", yt.title)
        print("Goruntulenme Sayisi: ", yt.views)
        print("Uzunluk: ", yt.length, "seconds")
        print("Aciklama: ", yt.description)
        print("Puan: ", yt.rating)
        print()
        print(yt.streams.filter(progressive=True))

        ys = yt.streams.get_highest_resolution()
        print()
        dizin = input("Lutfen videoyu kaydetmek istediginiz dizini girin: ")
        print()
        ys.download(dizin)
        if ys.download(dizin):
            print("Video basariyla indirildi...")
            print()
        else:
            print("Video indirilirken bir sorun olustu...")
            print()

    elif secenek == "S" or secenek == "s":
        print()
        link = input("Linki buraya kopyalayin: ")
        yt = YouTube(link)

        print()
        print("Baslik: ", yt.title)
        print("Goruntulenme Sayisi: ", yt.views)
        print("Uzunluk: ", yt.length, "seconds")
        print("Aciklama: ", yt.description)
        print("Puan: ", yt.rating)
        print()
        print(yt.streams.filter(only_audio=True))
        ys= yt.streams.get_audio_only()
        print()
        dizin = input("Lutfen ses dosyasini kaydetmek istediginiz dizini girin: ")
        print()
        out_file = ys.download(output_path=dizin)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        if out_file:
            print("Ses dosyasi basariyla indirildi...")
            print()
        else:
            print("Ses dosyasi indirilirken bir sorun olustu...")
            print()

    elif secenek == "Q" or secenek == "q":
        print("Programdan cikiliyor...")
        break
    else:
        print("Lutfen gecerli bir komut girin...")
        print()
    
        