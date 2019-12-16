#! /usr/bin/python3

import os
# import subprocess

# Files Types Commom
files_types = {
    'image': ('.jpeg', '.gif', '.png', '.bmp', '.tiff', '.psd', '.exif', '.raw',  '.eps', '.svg', '.webp', '.jpg', '.cf2',
              '.cr2', '.crw', '.dng', '.erf', '.mef', '.mrw', '.nef', '.orf', '.pef'),
    'documents': ('.doc', '.docx', '.csv', '.msg', '.rtf', '.bat', '.cfg', '.txt', '.pdf', '.ini', '.log', '.reg', '.xls',
                  '.xlsm', '.ods', '.xlsx'),
    'audio': ('.pcm', '.wav', '.aiff', '.mp3', '.aac', '.ogg', '.wma', '.flac', '.alac', '.wma'),
    'video': ('.avi', '.mov', '.wmv', '.mp4', '.3gp', '.3g2', '.flv', '.mkv', '.rm'),
    'zip': ('.7z', '.rar', '.zip', '.tar', '.targz', '.gz', '.jar', '.bz2')
}


# Functions for process the user name.

def record_user_name():
    '''
        Only record user name in file user.txt
    '''
    os.system('whoami > ./Downloads/script/user.txt')


def read_user_name():
    ''' 
        Read user name in file user.txt, and return it.
    '''
    file_user = open('./Downloads/script/user.txt', 'r')
    user_name = file_user.readlines()
    file_user.close()
    return user_name[0]


def get_path_user():
    '''
        Call functions record and read, and return user path.
    '''
    record_user_name()
    user_name = read_user_name()
    return '/home/{}'.format(user_name)


# Functions for process files list in folder downloads.

def record_list_files(path_user):
    '''
        Record in file.txt list files in folder Downloads.
    '''
    # [0:-1] if for remove \n when the function format return.
    os.system('cd {}/Downloads \nls > {}/Downloads/script/files.txt'.format(path_user[0:-1], path_user[0:-1]))
    # os.system('cd /home/artur/Downloads \nls > /home/artur/Downloads/script/files.txt')


def read_list_files(path_user):
    '''
        Read list files in file.txt, and return file opened.
    '''
    files = open('{}/Downloads/script/files.txt'.format(path_user[0:-1]), 'r')
    return files


# Functions for move the files

def using_check(file, path_user):
    '''
        Check if the file is using, and return the process pid.
    '''
    os.system('fuser -a {}/Downloads/{} > {}/Downloads/script/check.txt'.format(path_user[0:-1], file[0:-1], path_user[0:-1]))
    check = open('{}/Downloads/script/check.txt'.format(path_user[0:-1]), 'r')
    for pid in check.readlines():
        if pid:
            return True
        else:
            return False


def move_files_to_folders(files, path_user):
    '''
        Move files to folders.
    '''
    for file in files.readlines():  # Catch each file for analyze.
        if not (using_check(file, path_user)):  # If it isn't using

            # Image
            for i in range(len(files_types['image'])):
                # if some file_type(e.g. '.txt, .png.') in file
                if (files_types['image'][i]) in file:
                    # Move all files with extension current
                    os.system('mv {}/Downloads/*{} {}/Downloads/image'.format(path_user[0:-1], files_types['image'][i], path_user[0:-1]))

            # Documents
            for i in range(len(files_types['documents'])):
                if (files_types['documents'][i]) in file:
                    os.system('mv {}/Downloads/*{} {}/Downloads/documents'.format(path_user[0:-1], files_types['documents'][i], path_user[0:-1]))

            # Audio
            for i in range(len(files_types['audio'])):
                if (files_types['audio'][i]) in file:
                    os.system('mv {}/Downloads/*{} {}/Downloads/audio'.format(path_user[0:-1], files_types['audio'][i], path_user[0:-1]))

            # Video
            for i in range(len(files_types['video'])):
                if (files_types['video'][i]) in file:
                    os.system('mv {}/Downloads/*{} {}/Downloads/video'.format(path_user[0:-1], files_types['video'][i], path_user[0:-1]))

            # Zip
            for i in range(len(files_types['zip'])):
                if (files_types['zip'][i]) in file:
                    os.system('mv {}/Downloads/*{} {}/Downloads/zip'.format(path_user[0:-1], files_types['zip'][i], path_user[0:-1]))
    else: # After, if the file not is image, doc, audio, video or zip, then it go to others folders.         
        for file in files.readlines():
            # Others
            if not (using_check(file, path_user)):  # If it isn't using
                os.system('mv {}/Downloads/*.* {}/Downloads/others'.format(path_user[0:-1], path_user[0:-1]))



if __name__ == '__main__':
    path_user = get_path_user()
    record_list_files(path_user)
    files = read_list_files(path_user)
    move_files_to_folders(files, path_user)