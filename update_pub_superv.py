publications = []
supervisions = []

for filename in ["publications.html", "supervision.html"]:
	flag = 0
	for line in open(filename, "r", encoding = "utf-8"):
		if flag and line.find("/table") < 1:
			publications.append(line)
		if line.find("-->") > 0:
			flag = 1

for research_filename in ["research.html", "researchcn.html"]:
	researchlines = []
	flag_publication = 0
	flag_supervision = 0
	
	for line in open(research_filename, "r", encoding = "utf-8"):
		if flag_publication:
			if line.find("<tr><td></td></tr><tr><td></td></tr>") > -1:
				flag_publication = 0 
			else:
				continue

		if flag_supervision:
			if line.find("</table></td></tr>") > -1:
				flag_supervision = 0 
			else:
				continue

		researchlines.append(line)

		if line.find(">Publications<") > 0 or line.find(">论文发表<") > 0:
			researchlines.append("\t\t\t<tr><td><table align=\"left\" cellpadding=\"15\">\n")
			for line in publications:
				researchlines.append("\t\t\t" + line)
			researchlines.append("\t\t\t</table></td></tr>\n\n")
			flag_publication = 1

		if line.find("Selected Supervised Master and Bachelor Theses") > 0 or line.find("指导完成的有代表性的优秀本科、硕士毕业论文") > 0:
			researchlines.append("\t\t\t<tr><td><table align=\"left\" cellpadding=\"15\">\n")
			for line in supervisions:
				researchlines.append("\t\t\t" + line)
			researchlines.append("\t\t\t</table></td></tr>\n\n")
			flag_supervision = 1

	f = open(research_filename, "w", encoding = "utf-8")
	for line in researchlines:
		f.write(line)

print("Finished building htmls.")