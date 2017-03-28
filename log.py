#/usr/bin/env python


from optparse import OptionParser
import re


parser = OptionParser(usage = "%prog -b '171027  12727' -e '171027  13727' -f '/data/mysql.log'",version = "%prog 1.0" )
parser.add_option("-b", "--begin_time",
                  action="store", type="string", dest="begin_time",default="0",help="The begin timestamp.")
parser.add_option("-e", "--end_time",
                  action="store", type="string", dest="end_time",default="99999999999",help="The end timestamp.")
parser.add_option("-f", "--file_path",
                  action="store", type="string", dest="file_path",help="The file_path of logfile.")
parser.add_option("-s", "--hintsize",
                  action="store", type="string", dest="hintsize",help="The size of memory to use.")
parser.add_option("-r", "--result_path",
                  action="store", type="string", dest="result_path",help="The file_path of result.")


(options, args) = parser.parse_args()
begin_time = options.begin_time
end_time = options.end_time
file_path = options.file_path
hintsize = options.hintsize
result_path = options.result_path

pattern_1 = re.compile(r'[\t]{2}[\d]+[\s].*')
pattern_2 = re.compile(r'[\d]{6}[\s][\s]?[\d][\d]?[:][\d]{2}[:][\d]{2}[\s].*')
pattern_3 = re.compile(r'[\d]{6}[\s][\s]?[\d][\d]?[:][\d]{2}[:][\d]{2}')



class ReadLog():

    def __init__(self):
        self.begin_time = begin_time
        self.end_time = end_time
        self.file_path = file_path
        self.hintsize = int(hintsize)
        self.result_path = result_path

    def Read(self):
        with open (self.file_path,'rb') as f:
            while True:
                data = f.readlines(self.hintsize)
                if data:
                    yield data
                else:
                    return
    def Write(self,data):
        with open (self.result_path,'a') as f:
            f.writelines(data)

    def numberical(self,date):
        if len(date.replace(' ','').replace(':','')) == 11:
            return int((date[:7] + '0' + date[7:]).replace(' ','').replace(':','').replace('unkowntime',''))
        elif date == 'unkown time':
            return 0
        else:
            return int(date.replace(' ','').replace(':','').replace('unkowntime',''))

    def RexRead(self):
        timestamp = 'unkown time'
        for i in self.Read():
            for atom in i:
                if pattern_2.match(atom):
                    timestamp = pattern_3.search(atom).group()
                    if (self.numberical(timestamp) >= self.numberical(self.begin_time) and self.numberical(timestamp) <= self.numberical(self.end_time)):
                        self.Write(atom)
                elif (pattern_1.match(atom) and self.numberical(timestamp) >= self.numberical(self.begin_time) and self.numberical(timestamp) <= self.numberical(self.end_time)):
                    atom = [timestamp+atom]
                    self.Write(atom)
                elif (self.numberical(timestamp) >= self.numberical(self.begin_time) and self.numberical(timestamp) <= self.numberical(self.end_time)):
                    self.Write(atom)
                elif self.numberical(timestamp) > self.numberical(self.end_time):
                    break



if __name__ == '__main__':
    a = ReadLog()
    a.RexRead()
