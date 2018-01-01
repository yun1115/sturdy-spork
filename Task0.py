"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def firsttext(texts):
	first = texts[0]
	incoming_number = first[0]
	answering_number = first[1]
	time = first[2]
	text = "First record of texts, {} texts {} at time {}".format(incoming_number, answering_number, time)
	return text


def lastcall(calls):
	last = calls[-1]
	incoming_number = last[0]
	answering_number = last[1]
	time = last[2]
	during = last[3]
	call = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(incoming_number, answering_number, time, during)
	return call

print(firsttext(texts))	
print(lastcall(calls))

