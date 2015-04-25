#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
#将path/to/chat-recor改为实际路径
f = open("/path/to/chat-record", "r")
record = open("/path/to/chat-record", "r").read().decode('utf-8')

#get 2 nicknames
l = (f.readline()).split(' ')
name1 = l[3]

f.readline()
f.readline()

l = (f.readline()).split(' ')
name2 = l[3]

#转换为unicode
name1 = unicode(name1, 'utf-8')
name2 = unicode(name2, 'utf-8')

print name1,name2
day = re.findall('(\d{4}-\d{2}-\d{2})',record)
times = re.findall('\d{4}-\d{2}-\d{2} (\d{2}):(\d{2}):(\d{2})  (%s|%s)' %(name1, name2), record)

if (len(times) < 1):
	print '没有聊天内容'
	exit()

avgtime1=[]
avgtime2=[]

def countTime(h1,m1,s1,h2,m2,s2):
	return (h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1

print '聊天日期：',day[0],'到',day[len(day) - 1]
print '共', len(times),'条聊天记录'

if(times[0][3] == name1):

	hour1= times[0][0]
	min1= times[0][1]
	second1= times[0][2]

	hour2= times[1][0]
	min2= times[1][1]
	second2= times[1][2]
else:

	hour2= times[0][0]
	min2= times[0][1]
	second2= times[0][2]

	hour1= times[1][0]
	min1= times[1][1]
	second1= times[1][2]


for time in times[2:]:
	
	hour3= time[0]
	min3= time[1]
	second3= time[2]

	if (time[3] == name1):
		timeGap1 =countTime(int(hour1),int(min1),int(second1),int(hour3),int(min3),int(second3))
		if (timeGap1 > 60 * 5):
			continue

		avgtime1.append(timeGap1)		
		hour1=hour3
		min1=min3
		second1=second3
	if (time[3] == name2):
		timeGap2 =countTime(int(hour2),int(min2),int(second2),int(hour3),int(min3),int(second3))
		if (timeGap2 > 60 * 5):
			continue
		avgtime2.append(timeGap2)		
		hour2=hour3
		min2=min3
		second2=second3
				

time1 = 0
time2 = 0

i = 0
if(i < len(avgtime1)):
	time1=time1 + avgtime1[i]
	i =i+1
		
print name1,'的平均回复时间是： ', time1,' 秒'

i = 0
if(i < len(avgtime2)):
	time2=time2 + avgtime2[i]
	i =i+1
		
print name2,'的平均回复时间是： ', time2,' 秒'
