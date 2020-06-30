import re
import base64

# Read in the file
with open('BPG_OSCE_Sample.html', 'r') as file :
  filedata = file.read()

result = re.findall('data\:image\/png\;base64\,(.*?)\\"', filedata, re.S)

number_of_pics = 0
for b64 in result:
  png = base64.b64decode(b64)
  path = 'b64img/img'+str(number_of_pics)+'.png'
  with open(path, 'wb+') as file:
    file.write(png)

  filedata = filedata.replace("data:image/png;base64," + b64,path)
  number_of_pics += 1


# Write the file out again
with open('BPG_OSCE_Sample.html.cleaned', 'w+') as file:
  file.write(filedata)