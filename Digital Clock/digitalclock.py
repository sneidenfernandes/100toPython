import sys,time
import sevenseg


try:
    while True:
        # Clear the screen by printing several newlines:
        print('\n'*60)
        
        currentTime = time.localtime()

        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = 12
        
        minutes = str(currentTime.tm_min)

        seconds = str(currentTime.tm_sec)

        hDigits = sevenseg.getSevenSegment(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevenseg.getSevenSegment(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines() 

        sDigits = sevenseg.getSevenSegment(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + '   ' + mTopRow + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)
        
        print('Press ctrl-C to quit.')

        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except:
    sys.exit()




