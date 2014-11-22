import re
import os

file_rules = 'test.txt'
file_css = 'text_source.txt'
new_css = open('new_css.css',"w")

with open(file_rules) as f:
    rules = f.readlines()

with open(file_css) as f:
    css = f.read()    

for rule in rules:
	regexp = "^" + rule.rstrip() + ".*{[\s\S]*?}"
	pattern = re.compile(regexp,re.MULTILINE)
	if re.search(pattern, css):
		a = re.search(pattern, css).group(0).strip()
		print "Remove style : " + a
		css = css.replace(a,'')

css = os.linesep.join([s for s in css.splitlines() if s])			
new_css.write(css)	
new_css.close()