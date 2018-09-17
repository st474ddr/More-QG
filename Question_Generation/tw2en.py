from googletrans import Translator
translate = Translator()
flie = open('chinese_input.txt','r')
input = flie.read()
result = translate.translate(input)

chinese = open("english_input.txt",'w')
chinese.write(result.text)
print (result.text)