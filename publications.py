publications = []
flag = 0
for line in open("publications.html", "r", encoding = "utf-8"):
	if flag and line.find("/table") < 1:
		publications.append(line)
	if line.find("-->") > 0:
		flag = 1

for research_filename in ["research.html", "researchcn.html"]:
	researchlines = []
	flag = 0
	for line in open(research_filename, "r", encoding = "utf-8"):
		if flag:
			if line.find("<tr><td></td></tr><tr><td></td></tr>") > -1:
				flag = 0 
			else:
				continue
		researchlines.append(line)
		if line.find(">Publications<") > 0 or line.find(">论文发表<") > 0:
			researchlines.append("\t\t\t<tr><td><table align=\"left\" cellpadding=\"15\">\n")
			for line in publications:
				researchlines.append("\t\t\t" + line)
			researchlines.append("\t\t\t</table></td></tr>\n\n")
			flag = 1

	f = open(research_filename, "w", encoding = "utf-8")
	for line in researchlines:
		f.write(line)

print("Finished building htmls.")