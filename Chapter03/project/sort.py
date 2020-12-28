import os
import shutil

file_list = [x for x in os.listdir(".") if x.endswith(".swf")]
src = os.getcwd() + "\\"

for y in file_list:
	shutil.move(src + y, src + "\\swf\\" + y)
