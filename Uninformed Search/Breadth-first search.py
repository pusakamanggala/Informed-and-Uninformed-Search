#inisialisasi nama dan nomer gedung 
namanya = {
	1:'Gedung N', 
	2:'Business Center', 
	3:'Gedung P',
	4:'Gedung O', 
	5:'Kantin Teknik', 
	6:'Student Center', 
	7:'GSG',
	8:'TMART',
	9:'GKU'
}

cost =	{																	
	1:	{1:	0,	2:	1,	3:	1,	4:	1,	5:	0,	6:	0,	7:	0,	8:	0,	9:	0},
	2:	{1:	1,	2:	0,	3:	0,	4:	0,	5:	1,	6:	1,	7:	0,	8:	0,	9:	0},
	5:	{1:	0,	2:	1,	3:	0,	4:	0,	5:	0,	6:	0,	7:	0,	8:	0,	9:	0},
	6:	{1:	0,	2:	1,	3:	0,	4:	0,	5:	0,	6:	0,	7:	0,	8:	0,	9:	0},
	3:	{1:	1,	2:	0,	3:	0,	4:	0,	5:	0,	6:	0,	7:	1,	8:	0,	9:	0},
	7:	{1:	0,	2:	0,	3:	1,	4:	1,	5:	0,	6:	0,	7:	0,	8:	1,	9:	0},
	8:	{1:	0,	2:	0,	3:	0,	4:	0,	5:	0,	6:	0,	7:	1,	8:	0,	9:	1},
	9:	{1:	0,	2:	0,	3:	0,	4:	0,	5:	0,	6:	0,	7:	0,	8:	1,	9:	0},
	4:	{1:	1,	2:	0,	3:	0,	4:	0,	5:	0,	6:	0,	7:	1,	8:	0,	9:	0},
}

if __name__ =="__main__": 
	n = 10
	visit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #yang sedang dilewati
	visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #yang sudah dilewati
	qu = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #menampung daftar tunggu queue
	for i in range(1, 10): 
		print(f"{namanya[i]} = {i}")
	#hubungan antar gedung 
	print('Hubungan Antar Gedung\n') 
	for i in range(1, 10):
		for j in range(1, 10): 
			if cost[i][j] == 1:
				print(f'{namanya[i]} ke {namanya[j]}') 
v = int(input('\n\nMasukan Initial State: '))
s = int(input('Masukan Final State: ')) 
#metode pencarian bfs 
print(f'\nRUTE:\n{namanya[v]}')
visited[v] = 1
k = 1
front = 0
rare = 0

while(k<n and k!=s):
    for i in range(1, 10):
        if cost[v][i] != 0 and visited[i]!=1 and visit[i]!=1: 
            visit[i] = 1
            rare += 1 
            qu[rare] = i

    front += 1
    v = qu[front] 
    print(namanya[v])

    k += 1
    visit[v] = 0
    visited[v] = 1


