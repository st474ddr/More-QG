from googletrans import Translator
translate = Translator()
flie = open('english_result.txt','r')
input = flie.read()
result = translate.translate(input,dest='zh-TW')

chinese = open("chinese_result.txt",'w')
chinese.write(result.text)
print (result.text)