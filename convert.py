import subprocess
import os
import sys
import time
import optparse 
from optparse import OptionParser

#Requirements:
#Python3.1 
#HandBrake, installed at z:\Apps\Handbrake
#  I couldn't get the path to handle the Program Files (x86) so I gave up
#  It is on the todo list to fix later

#example
#z:\Apps\Python31\python.exe z:\Apps\scripts\convert2.py -i 'Z:\Videos\TV\SomeShow' ExtraTextForSomeShow -o 'z:\Videos\ConvertedOutput'


parser = OptionParser()
parser.add_option('-i', '--input-directory',  dest='in_dirs', action='append', help='directory that has the files to be converted', metavar='IN_DIR', nargs=2, type='string')
parser.add_option('-o', '--output-directory', dest='out_dir', action='store',  help='output directory for the converted file',      metavar='OUT_DIR')
parser.add_option('-e', '--executable-path', dest='exe_path', action='store',  help='The path to the HandBrakeCLI executable',      metavar='EXE_PATH')
(options, args) = parser.parse_args()

if options.out_dir == None:
    options.out_dir = options.in_dirs[0]

for (in_dir,extra_tag) in options.in_dirs:
    dir_listing = os.listdir(in_dir)
    for in_file in dir_listing:
        (out_file, extension) = os.path.splitext(in_file)
        out_file = extra_tag + out_file
        if extension == '.avi':
            out_file = out_file + '.mp4'
            #cmd  = os.path.join('z:','Apps','Handbrake','HandBrakeCLI.exe')
            if options.exe_path:
                cmd = options.exe_path
            else:
                cmd  = 'HandBrakeCLI'
            os.path.normpath(cmd)
        
            
            in_total_path  = os.path.join(in_dir, in_file)
            out_total_path = os.path.join(options.out_dir,out_file)
            cmd += ' -i \"%s\"' % in_total_path
            cmd += ' -o \"%s\"' % out_total_path
            cmd += ' --preset=\"iPhone & iPod Touch\"'
            print ('cmd is %s\n\n' % cmd)
            #for some reason subprocess.call doesnt work here when I have the command line arguments
            #added onto the end. Weird. I changed it to an os.system call for now instead
            print(os.system(cmd))
    


#TODO
#move the output to the iTunes autoimport folder, only if it finished converting correctly
#Add different quality options
#Check if the destination file exists before converting -- this will allow doing the same folder multiple times
#Convert the movie first to a temporary file, then copy if it finished successfully

#example
#z:\Apps\Python31\python.exe z:\Apps\scripts\convert.py -i 'Z:\Videos\TV\SomeShow' ExtraTextForSomeShow -o 'z:\Videos\ConvertedOutput'
#

