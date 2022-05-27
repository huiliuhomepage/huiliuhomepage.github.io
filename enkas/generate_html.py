import os
dict = {"a": "あいうえお",
        "k": "かきくけこ",
        "s": "さしすせそ",
        "t": "たちつてと",
        "n": "なにぬねの",
        "h": "はにふへほ",
        "m": "まみむめも",
        "y": "やゆよ",
        "r": "らりるれろ",
        "w": "わを",
        "c": "中文",
        "e": "English"}

dirs = []
lst = os.walk('.')
for dirpath, dirnames, filenames in lst:
    for dirname in dirnames:
        dirs.append(os.path.join(dirpath, dirname))

for fulldirname in dirs:
    songs = []
    songdirs = []
    dirname = fulldirname[-1]
    for dirpath, dirnames, filenames in os.walk(fulldirname):
        for filename in filenames:
            songs.append(filename[:-4])
            songdirs.append(os.path.join(dirpath, filename))
    print (dict[dirname], songs)

    f = open(dirname + ".html", "w", encoding = "utf-8")
    f.write("<!DOCTYPE html>\n")
    f.write("<html lang=\"cn\">\n")
    f.write("<head>\n")
    f.write("<meta charset=\"utf-8\">\n")
    f.write("<title>" + dict[dirname] + " - Enka Lyrics World</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    
    f.write("<a href=\"..\indexenka.html\">Enka Category</a><br><br>\n")
    f.write("<h2>\n")
    for song in songs:
        f.write("<a href=\"#" + song + "\">" + song + "</a><br>\n")
    f.write("</h2>\n")
    f.write("<br><a href=\"..\indexenka.html\">Enka Category</a>\n")
    
    f.write("<h1>\n")
    for i in range(len(songs)):
        f.write("<br><br>\n<a id=\"" + songs[i] + "\">【" + songs[i] + "】</a>　")
        for line in open(songdirs[i], "r", encoding = "utf-8"):
            f.write(line.strip("\n").replace("「", "<ruby><rb>").replace("」", "</rb>").replace("【", "<rt>").replace("】", "</rt></ruby>") + "<br>\n")
    f.write("</h1>\n")
    f.write("<br><br><a href=\"..\indexenka.html\">Enka Category</a>")

    f.write("</body>\n")
    f.write("</html>\n")
    f.close()

print("Finished building htmls.")