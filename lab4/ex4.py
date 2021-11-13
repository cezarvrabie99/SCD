import threading
import urllib.request
import time


def downloadImage(imagePath, fileName):
    print("Downloading Image from ", imagePath)
    urllib.request.urlretrieve(imagePath, fileName)
    print("Completed Download")


def executeThread(i):
    imageName = "image-" + str(i) + ".jpg"
    downloadImage("https://picsum.photos/300/300?random", imageName)


def main():
    t0 = time.time()

    threads = []

    for i in range(10):
        thread = threading.Thread(target=executeThread, args=(i,))
        threads.append(thread)
        thread.start()

    for i in threads:
        i.join()

    t1 = time.time()
    totalTime = t1 - t0
    print("Total Execution Time {}".format(totalTime))


if __name__ == '__main__':
    main()
