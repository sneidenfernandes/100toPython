import random, time, os


BAR = chr(9608)


def timeProgressBar(length):

    timeComplete = 0
    totalTime = length

    while timeComplete < totalTime:

        timeComplete += 1

        barStr = getProgressBar(timeComplete, totalTime)

        print(barStr, end='',flush=True)

        time.sleep(1)

        print('\b' * len(barStr), end='', flush=True)

    os.system('clear')

    print('Recording Complete.')
        



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

    progressBar += f'({progress} secs)'

    return progressBar





