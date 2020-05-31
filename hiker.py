import re
class Hiker:
	def haiku(self,line):
		
		if(len(line)>202):
			raise ValueError('Haiku cannot be longer than 200 characters.invalid input line')

		if(any(x.isupper()for x in line)):
			raise ValueError('Haiku can only contain lower case letters. input contains Upper Case letters: invalid input line')
		
		if(any(x.isdigit()for x in line)):
			raise ValueError('Numbers are not allowed in a Haiku: invalid input line')	
		
		string_check= re.compile('[@_!#$%^&*()<>?\|}{~:]')
		if string_check.search(line) is not None:
			raise ValueError('No special characters: invalid input line')	
		
		lines = line.split('/')
				
		if not len(lines) == 3:
			raise ValueError('Haiku must only contain three lines. No of lines found:{}'.format(len(lines)))
		
		syl = [0,0,0]
		
		for i in range(len(lines)):
			words = lines[i].split()
			for j in range(len(words)): 
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

			if (syl[i] == 0):
				syl[i]=len(words)		
			
		
		if (syl[0] == 5 and syl[1] == 7 and syl[2] == 5):
			result = 'Yes'
		else:
			result = 'No'
		
		print("{}/{}/{},{}".format(syl[0],syl[1],syl[2],result))

		return syl[0],syl[1],syl[2],result


	if __name__ == "__main__": 
		filepath = 'test.txt'
		try:
			file = open(filepath)
			with open(filepath) as fp:	
				for cnt,line in enumerate(fp):
					haiku(cnt,line)
		except FileNotFoundError:
			pass