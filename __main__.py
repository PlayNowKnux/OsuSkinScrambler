import os, sys, random, datetime, shutil


def main():
    with open('path.txt', 'r') as f:
        p = f.read()
        f.close()
    try:
        s = sys.argv[1]
    except IndexError:
        s = input("Which skin do you want to scramble? :")
    path = os.path.join(p, s)
    l = get_list(path)
    copy_files(path, l)


def ext(fn):
    # Get file extension
    return fn.split(".")[-1]


def strip_ext(fn):
    # Strip file extension
    return "".join(fn.split(".")[:-1])


def get_list(path):
    # Get trajectory for files
    oldlist = []
    for i in os.listdir(path):
        oldlist.append(str(i))

    # Include only png, mp3, wav
    img = []
    audio = []
    for i in oldlist:
        if ext(i) == "png":
            img.append(i)
        elif ext(i) in ["wav", "mp3"]:
            audio.append(i)
    new_img = []
    new_audio = []
    for i in img:
        new_img.append(i)
    for i in audio:
        new_audio.append(i)
    random.shuffle(new_img)
    random.shuffle(new_audio)


    pack = [[], []]

    # Extensions don't matter to osu.
    for i in range(0, len(new_img)):
        new_img[i] = strip_ext(new_img[i])
        pack[0].append((img[i], new_img[i]))
    for i in range(0, len(new_audio)):
        new_audio[i] = strip_ext(new_audio[i])
        pack[1].append((audio[i], new_audio[i]))

    return pack


def copy_files(path, l):
    # Copy the files

    time = datetime.datetime.now()
    time_str = "-" + str(time.year) + "-" + str(time.month) + "-" + str(time.day) + "T" + str(time.hour) + "!" \
               + str(time.minute) + "!" + str(time.second)
    new_path = path + time_str
    os.mkdir(new_path)
    for i in l[0]:
        print(i)
        print(ext(i[0]))
        # os.path.join is for losers
        # Or maybe... I'm a loser because it didn't work here? Hmm...
        shutil.copyfile(path + "\\" + i[0], new_path + "\\" + i[1] + "." + ext(i[0]))
    for i in l[1]:
        print(i)
        print(ext(i[0]))
        shutil.copyfile(path + "\\" + i[0], new_path + "\\" + i[1] + "." + ext(i[0]))



if __name__ == '__main__':
    main()
