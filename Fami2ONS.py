import glob
import sys
import os
import re
import chardet

same_hierarchy = (os.path.dirname(sys.argv[0]))

scenario_dir = os.path.join(same_hierarchy,'scr')

with open(os.path.join(same_hierarchy, 'default.txt')) as f:
    txt = f.read()

pathlist = glob.glob(os.path.join(scenario_dir, '*.txt'))

time = 0

for snr_path in pathlist:

    with open(snr_path, 'rb') as f:
        char_code =chardet.detect(f.read())['encoding']

    with open(snr_path, encoding=char_code, errors='ignore') as f:

        txt += ';--------------- '+ os.path.splitext(os.path.basename(snr_path))[0] +' ---------------\nend\n'
        txt = txt.replace('//', ';;;')

        for line in f:
            
            #KWNKNG_line = re.match(r'(\s*)(\S*)<KW><WinClear>',line)
            imageparts_line = re.match(r'<ImageLoad (\d+),(\w+).bmp><ImageParts (\d+),(\w+).bmp,(\d+),(\d+)><ImagePos (\d+),(\d+),(\d+)><Update Cross,(\d+)>',line)
            image_line = re.match(r'<ImageLoad (\d+),(\w+).bmp><UpDate Cross,(\d+)>',line)
            imagealpha_line = re.match(r'<ImageLoad (\d+),(\w+).bmp><ImageLoad (\d+),(\w+).bmp><UpDate Cross,(\d+)>',line)
            Label_line = re.match(r'\[(\S+)_TOP\]',line)
            Jump_line = re.match(r'<Jump\s(\w+).txt,(\S+)_TOP>',line)
            Mov_line = re.match(r'<Mov\s(\S+),(\d+)>',line)
            Soundrun_line = re.match(r'<SoundLoop (\d+),(\S+)><SoundLoad (\d+),(\S+).ogg><SoundRun (\d+),(\S+)>',line)
            Voice_line = re.match(r'<SoundLoad (\d+),(\w+).ogg><SoundRun (\d+),(\S+)>',line)
            Soundstop1_line = re.match(r'<SoundLoop (\d+),OFF><SoundRun (\d+),Stop,ON,(\d+)>',line)
            Soundstop2_line = re.match(r'<SoundRun (\d+),Stop,ON,(\d+)>',line)
            


            if imageparts_line: 

                if imageparts_line[1] == 4:#ひびき

                    line1 = 'lsp 38,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 37,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3

                elif imageparts_line[1] == 5:#ほむら

                    line1 = 'lsp 36,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 35,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3

                elif imageparts_line[1] == 6:#レイカ

                    line1 = 'lsp 34,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 33,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3

                elif imageparts_line[1] == 7:#美晴

                    line1 = 'lsp 32,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 31,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3

                elif imageparts_line[1] == 8:#クミコ

                    line1 = 'lsp 30,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 29,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3

                elif imageparts_line[1] == 9:#セナ

                    line1 = 'lsp 28,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 27,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3

                elif imageparts_line[1] == 10:#その他

                    line1 = 'lsp 26,"img\\' + imageparts_line[2] + '.png",0,0\n'
                    line2 = 'lsp 25,"img\\' + imageparts_line[4] + '.png",' + imageparts_line[5] + ',' + imageparts_line[6] + '\n'
                    line3 = 'print 10,' + imageparts_line[10] + '\n'
                    line = line1 + line2 + line3


                #print(line)

                

            elif image_line:

                HAIKEI = re.match(r'bg(\w+)',image_line[2])

                if HAIKEI:

                    if time == 0:

                        line = 'lsp 39,"img\\bg' + HAIKEI[1] + '_m.png",0,0\nprint 10,' + image_line[3] +'\n'
                    
                    elif time == 1:

                        line = 'lsp 39,"img\\bg' + HAIKEI[1] + '_d.png",0,0\nprint 10,' + image_line[3] +'\n'

                    elif time == 2:

                        line = 'lsp 39,"img\\bg' + HAIKEI[1] + '_e.png",0,0\nprint 10,' + image_line[3] +'\n'

                    elif time == 3:

                        line = 'lsp 39,"img\\bg' + HAIKEI[1] + '_n.png",0,0\nprint 10,' + image_line[3] +'\n'

                    else:

                        line = ';lsp 39,"img\\bg' + HAIKEI[1] + '.png",0,0\nprint 10,' + image_line[3] +'\n'

                    #print(line)

                else:

                    line = 'lsp 39,"img\\' + image_line[2] + '.png",0,0\nprint 10,' + image_line[3] +'\n'
                    #print(line)

            elif Label_line:

                line = '*' + Label_line[1] + '\nlookbackflush\n'
                

            elif Jump_line:

                line = 'goto *' + Jump_line[1] + '\nend'
                
            elif Mov_line:

                if Mov_line[1] == '時間帯':

                    line = 'mov %timezone,' + Mov_line[2] + '\nbackgroundtimes\n'
                    time = Mov_line[2]

                    print(time)

                else:

                    line = ';' + Mov_line[1] + ',' + Mov_line[2] + '\n'

            elif Soundrun_line:

                if Soundrun_line[2] == 'OFF':

                    line = 'dwave ' + Soundrun_line[1] + ',"snd\\' + Soundrun_line[4] + '.ogg"\n'
                    #print(line)

                elif Soundrun_line[2] == 'ON':

                    line = 'dwaveloop ' + Soundrun_line[1] + ',"snd\\' + Soundrun_line[4] + '.ogg"\n'
                    #print(line)


            elif Voice_line:

                line = 'dwave ' + Voice_line[1]  + ',"snd\\' + Voice_line[2] + '.ogg"\n'

                #print(line)

            elif Soundstop1_line:

                line = 'dwavestop ' + Soundstop1_line[1] + '\n'

            elif Soundstop2_line:

                line = 'dwavestop ' + Soundstop2_line[1] + '\n'

            elif re.match(r'([^\x01-\x7E]+)',line):

                #RUBY = re.search('')

                line = line + '\n'

            else:

                line = ';' + line + '\n'

            line = line.replace('<KW>','\\\n')
            line = line.replace('<WinClear>','')
            
            txt += line

open(os.path.join(same_hierarchy,'0.txt'), 'w', errors='ignore').write(txt)