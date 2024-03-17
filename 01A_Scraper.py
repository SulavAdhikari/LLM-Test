import wikipediaapi


wiki = wikipediaapi.Wikipedia('Football (email@example.com)','en')

list_of_topic = [
	'Football',
	'La_Liga',
	'Real_Madrid',
	'Barcelona',
	'Athletic_Club',
	'Girona',
	'Atlético_Madrid',
	'Real_Sociedad',
	'Real_Betis',
	'Valencia',
	'Getafe',
	'Villarreal',
	'Osasuna',
	'Sevilla',
	'Celta_Vigo',
	'Mallorca',
	'Rayo_Vallecano',
	'Granada',
	'Premiere_League',
	'Arsenal',
	'Liverpool',
	'Man_City',
	'Manchester_City',
	'Aston_Villa',
	'Tottenham',
	'Man_United',
	'West_Ham',
	'Brighton',
	'Newcastle',
	'Chelsea',
	'Fulham',
	'Bournemount',
	'Crystal_Palace',
	'Brentford',
	'Everton',
	'Nottm_Forest',
	'UEFA_Champions_League',
	'UEFA',
	'FIFA',
	'Jude_Bellingham',
	'Robert_Lewandowski'
]


for topic in list_of_topic:
	 
	page = wiki.page(topic)
	print("[+] Starting ", topic)
	if page.exists():
		print("[*] Opening " + topic)
		filename = str("data/" + topic + ".txt")
		file = open(filename, 'wt')
		file.write(page.text)
		print()
	else:
		print("[-] " + topic + "doesnot exist in wikipedia.")
