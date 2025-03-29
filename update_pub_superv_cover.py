impact = [9.6, 6.8, 6.7, 6.6, 5.4, 5.1, 4.6, 4.3, 4.0, 4.0,
          3.8, 4.3, 4.3, 4.0, 3.9, 3.9, 3.9, 3.4, 3.4, 3.4,
		  3.4, 3.4, 3.4, 3.4, 2.7, 2.6, 2.6, 2.6, 2.1, 2.1,
		  2.1, 2.6]
impact_co = [8.5, 3.9, 3.4, 3.4, 2.7, 2.3]

publications = []
supervisions = []
covers = []

print ("Impact factor:", sum(impact) + sum(impact_co), "First/corresponding:", sum(impact))
input()

for filename in ["publications.html", "supervision.html", "cover.html"]:
	flag = 0
	for line in open(filename, "r", encoding = "utf-8"):
		if flag and line.find("/table") < 1:
			if filename.find("publication") > -1:
				publications.append(line)
			else:
				if filename.find("supervision") > -1:
					supervisions.append(line)
				else:
					covers.append(line)
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

		if line.find(">Publications (") > 0 or line.find(">论文发表（") > 0:
			researchlines.append("\t\t\t<tr><td><table align=\"left\" cellpadding=\"15\">\n")
			for line in publications:
				researchlines.append("\t\t\t" + line)
			researchlines.append("\t\t\t</table></td></tr>\n\n")
			flag_publication = 1

		if line.find("Selected Supervised Master and Bachelor Theses") > 0 or line.find("指导完成的有代表性的优秀本科、硕士毕业论文") > 0:
			researchlines.append("\t\t\t\t<tr><td><table align=\"left\" cellpadding=\"15\">\n")
			for line in supervisions:
				researchlines.append("\t\t\t\t" + line)
			flag_supervision = 1

	f = open(research_filename, "w", encoding = "utf-8")
	for line in researchlines:
		f.write(line)

for art_filename in ["art.html", "artcn.html"]:
	artlines = []
	flag_art = 0
	
	for line in open(art_filename, "r", encoding = "utf-8"):
		if flag_art:
			if line.find("</table></td></tr>") > -1:
				flag_art = 0 
			else:
				continue

		artlines.append(line)

		if line.find("演歌·歌謡曲カバー選") > 0:
			artlines.append("\t\t\t\t<tr><td><table align=\"left\" cellpadding=\"15\">\n")
			for line in covers:
				artlines.append("\t\t\t\t" + line)
			#artlines.append("\t\t\t\t</table></td></tr>\n\n")
			flag_art = 1

	f = open(art_filename, "w", encoding = "utf-8")
	for line in artlines:
		f.write(line)

print("Finished building htmls.")