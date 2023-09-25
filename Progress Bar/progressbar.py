import random, time, os


BAR = chr(9608)


def main():

    bytesDownloaded = 0
    downloadSize = 5000

    while bytesDownloaded < downloadSize:

        bytesDownloaded += random.randint(0,100)

        barStr = getProgressBar(bytesDownloaded, downloadSize)

        print(barStr, end='',flush=True)

        time.sleep(0.2)

        print('\b' * len(barStr), end='', flush=True)

    os.system('clear')

    print('Download Completed.')
        



def getProgressBar(progress, total, width=40):
    
    progressBar = ''

    progressBar +=  '['

    if progress < 0:
        progress = 0
    
    if progress > total:
        progress = total

    completeBars = int(progress/total * width)

    progressBar += completeBars * BAR

    progressBar += " " * (width - completeBars)

    progressBar += ']'

    progressBar += str()

    progressBar += f'({progress}/{total})'

    progressBar +=  ' ' + str(round(progress/total * 100,2)) + '%'

    return progressBar


main()



