import vid
import img

def showHelp(extra,cmndd):
    if(extra!=""):
        print(extra)
    cmnds={
        "help":"  --shows this help",
        "play":"<videoname> <framedelay>         --plays video",
        "playvid":"<videoname> <framedelay>      --plays video",
        "addvid":"<video1> <video2> <framedelay  --adds two videos",
        "subvid":"<video1> <video2> <framedelay> --subtracts two videos",
        "countframes":"<videoname>               --counts the number of frames in a video",
        "countfps":"<videoname>                  --counts the number of frames/second of a video",
        "imshow":"<imagename>                    --displays the image file",
        "resizeimg":"<imagename> <w%> <h%>       --resizes an image"
            }
    print("Usage: ")
    if(cmndd==""):
        for k in cmnds:
            print(k+" "+cmnds[k])
    else:
        if cmndd in cmnds:
            print(cmndd+" "+cmnds[cmndd])

cmnd='y'
arr=[]
while(cmnd!='exit'):
    cmnd = input(">>> ")
    tokens=cmnd.split(" ")
    cmnd=tokens[0]
    if(cmnd==""):
        continue
    if(cmnd=='help'):
        showHelp("","")
    elif(cmnd=='play' or cmnd=='playvid'):
        if(len(tokens)!=3):
            showHelp("Needs two arguments.",cmnd)
        else:
            vid.play(tokens[1],int(tokens[2]))
    elif(cmnd=='addvid'):
        if(len(tokens)!=4):
            showHelp("Needs three arguments.",cmnd)
        else:
            vid.addvid(tokens[1],tokens[2],int(tokens[3]))
    elif(cmnd=='subvid'):
        if(len(tokens)!=4):
            showHelp("Needs three arguments.",cmnd)
        else:
            vid.subvid(tokens[1],tokens[2],int(tokens[3]))
    elif(cmnd=='countframes'):
        if(len(tokens)!=2):
            showHelp("Needs one arguments.",cmnd)
        else:
            count=vid.getFrameCount(tokens[1])
            print(count)
    elif(cmnd=='countfps'):
        if(len(tokens)!=2):
            showHelp("Needs one arguments.",cmnd)
        else:
            fps=vid.getFPS(tokens[1])
            print(fps)
    elif(cmnd=='imshow'):
        if(len(tokens)!=2):
            showHelp("Needs one arguments.",cmnd)
        else:
            img.imshow(tokens[1])
    elif(cmnd=='resizeimg'):
        if(len(tokens)!=4):
            showHelp("Needs 3 arguments.",cmnd)
        else:
            wPer=int(tokens[2])
            hPer=int(tokens[3])
            if(wPer<0 or wPer>100):
                print("invalid percentage value for width")
            elif(hPer<0 or hPer>100):
                print("invalid percentage value for height")
            else:
                img.resizeimg(tokens[1],wPer,hPer)
    elif(cmnd!='exit'):
        print("invalid command!")
        
