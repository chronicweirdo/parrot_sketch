'''
Created on Jun 20, 2012

@author: silviu
'''
import re

class TimeEntry:
    H = 1000 * 60 * 60
    M = 1000 * 60
    S = 1000
    def __init__(self, hour, minute, second, millisecond):
        hour = int(hour)
        minute = int(minute)
        second = int(second)
        self.time = int(millisecond) + second * self.S \
            + minute * self.M + hour * self.H
    def add(self, time):
        self.time += time
    def hour(self):
        return self.time / self.H
    def minute(self):
        return (self.time - self.hour() * self.H) / self.M
    def second(self):
        return (self.time - self.hour() * self.H - self.minute() * self.M) \
            / self.S
    def millisecond(self):
        return self.time % self.S
    def __str__(self):
        return str(self.hour()).zfill(2) + ':' + str(self.minute()).zfill(2)\
            + ':' + str(self.second()).zfill(2) + ','\
            + str(self.millisecond()).zfill(3)
        #return '{0:2d}:{1:2d}:{2:2d},{3:3d}'.format(self.hour(), self.minute()\
        #    , self.second(), self.millisecond())
        #return str(self.hour()) + ' ' + str(self.minute()) + ' ' +\
        #    str(self.second()) + ' ' + str(self.millisecond())
    @staticmethod
    def extract(string):
        pattern = '(\d{2}):(\d{2}):(\d{2}),(\d{3})'
        r = re.search(pattern, string);
        return TimeEntry(r.group(1), r.group(2), r.group(3), r.group(4))
    @staticmethod
    def parse(string):
        pattern = '(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'
        r = re.search(pattern, string)
        return (TimeEntry.extract(r.group(1)), TimeEntry.extract(r.group(2)))
        
def matches(line):
    return re.match('\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}', line) != None

def scan(inPath, outPath, difference):
    fileIn = open(inPath, 'r')
    fileOut = open(outPath, 'w')

    for line in fileIn:
        if matches(line):
            a, b = TimeEntry.parse(line)
            a.add(difference)
            b.add(difference)
            fileOut.write(str(a) + ' --> ' + str(b) + '\n')
        else:
            fileOut.write(line)
        
    fileIn.close()
    fileOut.close()

inPath = "C:\Users\silviu\Desktop\Michael 2011 720p BluRay x264-SONiDO.srt"
outPath = "C:\Users\silviu\Desktop\Michael 2011 correct subs.srt"
scan(inPath, outPath, -52 * 1000)

#timeP = '(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})'
#timeS = '00:03:03,183 --> 00:03:05,555'
#a, b = TimeEntry.parse(timeS)
#print a, b