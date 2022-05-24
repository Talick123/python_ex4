import re

def question2():
    log = open("atoms2.log", 'r')
    if not log:
        print("file log cannot be open")
    output_file = open("output.txt", 'w')
    txt = log.read()
    #messages = re.findall(r'[\w]+\s([0-9]+)[\w\s]+\.[A-Z\s]+([\w]+\.dat)\.\s[0-9]+\.[0-9]+[\w\s]+\.', txt)
    messages = re.findall(r'[\w]+\s([0-9]+)[A-Z\s\.]+([\w]+\.dat)\.\s[0-9]+\.[0-9]+[\w\s]+\.', txt)
    for message in messages:
        output_file.write(message[0] + " " + message[1] + "\n")
        #print(message[0] + " " + message[1])

    log.close()
    output_file.close()

'''
try:
    question1()
except:
    print("what")
'''

question2()
