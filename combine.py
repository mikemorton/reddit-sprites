import sys
import Image
import os
import simplejson

def CopyToLocation(targetpix, sourcepix, x, y):    
    pixdata = source.load()

    for yy in xrange(source.size[1]):
        for xx in xrange(source.size[0]):
            targetpix[x + xx, y + yy] = sourcepix[xx, yy]

def sorter(item):
    return item[2], item[3]


imagelist = open('imagelist.txt').readlines()
print imagelist
imagelist = [item.strip().split(',') for item in imagelist]
imagelist.sort(key=sorter)

count = len(imagelist)

columns = (count / 30) + 1
rows = 30

print (columns, rows)

target = Image.new("RGBA", (columns*20+columns, rows*20+rows), (255,255,255,0))
pixdata = target.load()

cssoutput = ""
redditmarkdown = ""

index = 0
for (cssclass,path,group,name) in imagelist:
    print path
    source = Image.open(path)
    source = source.convert("RGBA")
    y = (index % 30 ) * 21
    x = (index / 30) * 21

    CopyToLocation(pixdata, source.load(), x, y)

    redditmarkdown += "* [%s](http://www.reddit.com/message/compose/?to=sportslogobot&subject=logo&message=%s)\n" % (name,cssclass)

    xcss = "0"
    ycss = "0"
    if x > 0:
        xcss = "%dpx" % (x*-1)
    if y > 0:
        ycss = "%dpx" % (y*-1)

    cssoutput += ".flair-%s{background-position: %s %s;}\n" % (cssclass, xcss, ycss)
    cssoutput += ".flair-%s:hover:before{content:\"%s\";}\n" % (cssclass, name)    

    index += 1


cssfile = open('style.css', 'w')
cssfile.write(cssoutput)

markdownfile = open('markdown.txt', 'w')
markdownfile.write(redditmarkdown)

target.save('spriteimage.png')


