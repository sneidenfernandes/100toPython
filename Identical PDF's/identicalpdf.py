import hashlib


def hash_file(file1,file2):

    #Initializing Hash Objects

    h1 = hashlib.sha1()
    h2 = hashlib.sha1()

    # Convert file 1 to binary

    with open(file1,'rb') as f1:

        chunk = 0
        while chunk != b'':
            chunk = f1.read(1024)
            h2.update(chunk)

    # Convert file 2 to binary

    with open(file2, 'rb') as f2:

        chunk = 0
        while chunk != b'':
            chunk = f2.read(1024)
            h2.update(chunk)

    return h1.hexdigest(), h2.hexdigest()


def check_pdf(file1,file2):

    msg1,msg2 = hash_file(file1,file2)
    
    if msg1 != msg2:
        print("Files are not identical!")

    else:
        print("Files are identical")


if __name__ == '__main__':

    check_pdf('pd1.pdf','pd2.pdf')

