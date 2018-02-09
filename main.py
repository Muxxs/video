#coding=utf-8

from  moviepy.editor  import  VideoFileClip , concatenate_videoclips
import os,uniout,time
start = time.time()
def cut(name):
    clip = []
    file = []
    for rt, dirs, files in os.walk("/Users/wangjiao/Desktop/news/"):
        for f in files:
            fname = os.path.splitext(f)
            if fname[1]==name:
                file.append("/Users/wangjiao/Desktop/news/"+f)
    file.sort()
    print file
    for i in file:
        clip.append(VideoFileClip(i))
    if not clip==[]:
        final_clip  =  concatenate_videoclips(clip)
        final_clip.write_videofile("final.mp4")
name=str(raw_input("请输入文件后缀:")).replace("\n","").replace(" ","")
if name.find(".")==-1:
    name="."+name
cut(name)
end = time.time()
print "use:"+str(end-start)+"s"