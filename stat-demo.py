#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
#将这里的name1,name2修改为聊天记录里面的两个人的用户名
name1 = u"name1"
name2 = u"name2"

#将这里的/path/to/chat-record改为到聊天记录的路径
record = open("/path/to/chat-record.txt", "r").read().decode('utf-8')
day = re.findall('(\d{4}-\d{2}-\d{2})',record)
times = re.findall('\d{4}-\d{2}-\d{2} (\d{2}):(\d{2}):(\d{2})  (%s|%s)' %(name1, name2), record)

if (len(times) < 1):
	print '聊天记录为空'
	exit()

avgtime1=[]
avgtime2=[]

def countTime(h1,m1,s1,h2,m2,s2):
	return (h2 - h1) * 3600 + (m2 - m1) * 60 + s2 - s1

print '聊天日期：',day[0]
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
		avgtime1.append(countTime(int(hour1),int(min1),int(second1),int(hour3),int(min3),int(second3)))		
		hour1=hour3
		min1=min3
		second1=second3
	if (time[3] == name2):
		avgtime2.append(countTime(int(hour2),int(min2),int(second2),int(hour3),int(min3),int(second3)))		
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
