import subprocess
from tqdm import tqdm
folder_list=['Archive','excel','Images','PDF','PPT','Songs','Videos','Word','Json']
req_folder = [0 , 0 ,  0  ,  0  ,  0  ,  0  ,  0  ,  0  ,0]
print('Select the type of file you want to transfer \n1\tArchive(.rar,.zip)\n2\tExcel(.excel,.xlsx)\n3\tImages(.jpg,.jpeg.png)\n4\tPDF(.pdf)\n5\tPpts(.ppt)\n'
      '6\tSongs(.mp3,.m4a)\n7\tVideos(.mp4,.flv,.avi,.mkv)\n8\tWord(.word,.docx)\n9\tJson(.json)\n10\tAll above types\n0\tExit\nCan select one or more file type')
while(1):
    try:
        choice = int(input('Enter the number coresponding to your Selection-->\t'))
        if(choice == 0):
            break
        elif choice == 10:
            i = 0
            while(i<len(req_folder)):
                req_folder[i] = 1
                i = i + 1
            print('All File Format Selected')
            break
        if(req_folder[choice - 1] == 0):
            req_folder[choice - 1] = 1
            print(folder_list[choice - 1]," Selected")
        else:
            print(folder_list[choice - 1], " Already Selected")
    except:
        print('Invalid input')
sub='mi'
flag=False
Status=[]
loc='sdcard/'
available=[]
try :
    fp=open('settings.txt','r')
    for words in fp:
        if '\n' in words:
            available.append(words[:words.index('\n')])
        else:
            available.append(words)
except:
    print('Choosing Default Settings')
    available.append(loc)
for words in available:
    loc = words
    nm = ''
    i = 0
    for letters in words:
        if letters == '/' or letters == '\\':
            if i != len(words) - 1:
                nm = ''
        else:
            nm = nm + letters
        i = i + 1


    sub='Output\\'+nm
    print(sub)
    i = 0
    while(i < len(req_folder)):
        if(req_folder[i] == 1):
            x = folder_list[i]
            p1 = subprocess.run('md '+sub+'\\'+x, shell=True, capture_output=True)
            Status.append(p1.returncode)
        i = i + 1
    for stat in Status:
        print('Creating Folders  status',stat)
    print('Making Secure Connection')
    cmd='bin\\adb.exe shell ls '+ loc + ' -R'
    # print(cmd)
    lis=subprocess.run(cmd,shell=True,capture_output=True,text=True,encoding='UTF-8')
    if lis.returncode==1:
        print(lis.stderr,cmd)
    print('Initialising')
    out=lis.stdout.split('\n')
    # print(len(out))
    i=0
    ppt=[]
    list1=[]
    videos=[]
    songs=[]
    db=[]
    images=[]
    pdf=[]
    archive=[]
    word=[]
    excel=[]
    json=[]
    for items in out:
        if len(items)>0:
            if items[-1]==':':
                i=i+1
                list1.append((items,[]))
            else:
                list1[-1][1].append(items)

    # print(list1)
    # folder_list = ['Archive', 'excel', 'Images', 'PDF', 'PPT', 'Songs', 'Videos', 'Word', 'Json']
    for files in list1:
        for filename in files[1]:
            path=files[0][:-1]+'/'+filename
            if req_folder[0]:
                if '.rar' in filename or '.zip' in filename:
                    archive.append(path)
            if req_folder[1]:
                if '.excel' in filename or '.xlsx' in filename:
                    excel.append(path)
            if req_folder[2]:
                if '.jpg' in filename or '.jpeg' in filename or '.png' in filename:
                    images.append(path)
            if req_folder[3]:
                if '.pdf' in filename:
                    pdf.append(path)
            if req_folder[4]:
                if '.ppt' in filename:
                    ppt.append(path)
            if req_folder[5]:
                if '.mp3' in filename or '.m4A' in filename or '.m4a' in filename:
                    songs.append(path)
            if req_folder[6]:
                if '.mp4' in filename or'.avi' in filename or'.flv' in filename or'.mkv' in filename :
                    videos.append(path)
            if req_folder[7]:
                if '.word' in filename or '.docx' in filename:
                    word.append(path)
            if req_folder[8]:
                if '.json' in filename:
                    json.append(path)

    biglist=[[archive,'Archive','A',len(archive)],[excel,'excel','E',len(excel)],
             [images,'Images','I',len(images)],[json,'Json','J',len(json)],[pdf,'PDF','P',len(pdf)],[ppt,'PPT','PP',len(ppt)],
             [songs,'Songs','S',len(songs)],[videos,'Videos','V',len(videos)],[word,'Word','W',len(word)]]
    i = 0
    while(i < len(biglist)):
        items = biglist[i]
        if items[3] == 0:
            biglist.pop(biglist.index(items))
            i = i - 1
        i = i + 1

    tot=0

    for items in biglist:
        print(items[3],'  ',items[1],'  Found')
        tot = tot + items[3]

    print('Total files to transfer --->>\t',tot)
    print('Initiating Transfer\n')

    f=open('log'+nm+'.txt','w',encoding='UTF-8')
    f.write(str(len(songs))+'S '+str(len(videos))+'V '+str(len(images))+'I '+str(len(pdf))+'P '+str(len(db))+'DB '+str(len(archive))+'A '+str(len(word))+'W '+str(len(excel))+'E '+str(len(ppt))+'PP\n')
    for x in biglist:
        f.write(x[1]+' '+str(x[3])+'\n'+str(x[0]))
        f.write('\n')
    i=0

    for x in biglist:
        num=x[3]
        code=x[2]
        typ=x[1]

        total=len(x[0])
        suc=0
        fail=0
        failed=[]
        for items in tqdm(x[0]):
            i=i+1
            command='bin\\adb.exe pull '+'\"'+items+'\"'+' '+ sub +'/'+typ
            p1=subprocess.run(command,shell=True,capture_output=True)
            if p1.returncode==0:
                suc=suc+1
                # print('Success',suc)
            else:
                fail=fail+1
                failed.append([items,command,p1.stderr])
        if len(failed)!=0:
            fp=open('error'+nm+'.txt','a',encoding='UTF-8')
            fp.write('\n\n'+typ+' '+str(len(failed))+' out of'+str(total)+'\n'+str(failed))
print('Check the Output folder')
