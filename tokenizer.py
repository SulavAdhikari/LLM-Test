import gpt3_tokenizer

def test():
	a_string = "This might not be your job. It's mine."
	encoded = gpt3_tokenizer.encode(a_string) 
	decoded = gpt3_tokenizer.decode(encoded) 

	print(encoded)
	print(decoded)


tokenize = lambda s  : gpt3_tokenizer.encode(s)
revert = lambda t : gpt3_tokenizer.decode(t)


import os
# assign directory
directory = 'data'

def get_training_data():
	print("[*]getting data")
	data = []
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)
   		# checking if it is a file
		if os.path.isfile(f):
			print(f)
			file = open(f, 'rt')
			data.append(tokenize(file.read()))
	return sum(data, [])


def main():
	data = get_training_data()
	print("data length: " + str(len(data)))
	print("token count: " + str(gpt3_tokenizer.count_tokens(revert(data))))

if __name__ == "__main__":
	test()
	main()

