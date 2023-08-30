import os


def delete_screenshots():

    # Path to desktop 
    
    desktop_path = '/Users/sneiden/Desktop'

    # Obtaining a list of files and folders on the desktop

    desktop_content = os.listdir(desktop_path) 

    # Obtaining a list of screenshots located on the desktop
    
    screenshot_list =  []   

    for file in desktop_content:
        if 'Screenshot' in file:
            screenshot_list.append(file)

    # Deleting all the screenshot on the desktop 

    for screenshot in screenshot_list:
        
        path = desktop_path + '/' + screenshot

        os.remove(path)




if __name__ == '__main__':

    delete_screenshots()