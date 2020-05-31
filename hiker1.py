class hiker:
	def haiku(self,line):
		
				print("line{}".format(line))
				lines = line.split('/')
				print("no of lines {}".format (len(lines)))
				if not len(lines)<3:
					raise ValueError('Haiku should contain three lines. No of lines found:{}'.format(len(lines)))
					return
				syl = [0,0,0]
				for i in range(len(lines)):
					words = lines[i].split()
					print("line no {}: no of words  {}".format (i, len(words)))
					
					for j in range(len(words)):
						#print("word no {}.{}".format (j,words[j]))
						is_vow = False
						cur_word = words[j]
						
						for k in range(len(cur_word)):
							letter = cur_word[k]
							if letter in ('a','e','i','o','u','y'):
								if not is_vow == True:
									syl[i] += 1
								is_vow = True
							else:
								is_vow = False
					print("no of syllable: {}".format(syl[i]))
				if (syl[0] == 5 and syl[1] == 7 and syl[2] == 5):
					result = 'Yes'
				else:
					result = 'No'
				print("{}/{}/{},{}".format(syl[0],syl[1],syl[2],result))

	if __name__ == "__main__": 
			filepath = 'test.txt'
			with open(filepath) as fp:
				for cnt,line in enumerate(fp):
					haiku(line)
