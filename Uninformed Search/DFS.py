#inisialisasi nama dan nomer gedung 

namanya = {
    1:'Gedung N', 
    2:'Business Center', 
    3:'Kantin Teknik', 
    4:'Student Center', 
    5:'Gedung P',
    6:'GSG',
    7:'TMART',
    8:'GKU',
    9:'Gedung O'
}

#inisialisasi hubungan antar tempat menggunakan dictionary
cost =	{																	
    1:	{1:	0,	2:	1,	3:	0,	4:	0,	5:	1,	6:	0,	7:	0,	8:	0,	9:	1},
    2:	{1:	1,	2:	0,	3:	1,	4:	1,	5:	0,	6:	0,	7:	0,	8:	0,	9:	0},
    3:	{1:	0,	2:	1,	3:	0,	4:	0,	5:	0,	6:	0,	7:	0,	8:	0,	9:	0},
    4:	{1:	0,	2:	1,	3:	0,	4:	0,	5:	0,	6:	0,	7:	0,	8:	0,	9:	0},
    5:	{1:	1,	2:	0,	3:	0,	4:	0,	5:	0,	6:	1,	7:	0,	8:	0,	9:	0},
    6:	{1:	0,	2:	0,	3:	0,	4:	0,	5:	1,	6:	0,	7:	1,	8:	0,	9:	1},
    7:	{1:	0,	2:	0,	3:	0,	4:	0,	5:	0,	6:	1,	7:	0,	8:	1,	9:	0},
    8:	{1:	0,	2:	0,	3:	0,	4:	0,	5:	0,	6:	0,	7:	1,	8:	0,	9:	0},
    9:	{1:	1,	2:	0,	3:	0,	4:	0,	5:	0,	6:	1,	7:	0,	8:	0,	9:	0},
}

n = 10
visit = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #inisialisasi tempat yang sedang dilewati menggunakan dictionary
visited = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #inisialisasi tempat yang sudah dilewati menggunakan dictionary
stk = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #inisialisasi Stack menggunakan dictionary
for i in range(1, n):
  print(f"{namanya[i]} = {i}") #Print hubungan antar gedung print('\nHubungan Antar Gedung:') for i in range(1, n):
print('\nHubungan Antar Gedung: ')
for i in range(1, n):
  for j in range(1, n): 
    if cost[i][j] == 1:
      print(f'{namanya[i]} ke {namanya[j]}')
  #Input rute
v = int(input('\nMasukan Initial State: ')) 
s = int(input('Masukan Final State: ')) #Hasil Rute yang dilewati print(f'\nRute:\n{namanya[v]}')
  #DFS
print('\n')
visited[v] = 1
k = 1
top = 0
while(k<n and k!=s):
  for i in range(n-1, 0, -1):
    if cost[v][i] != 0 and visited[i] != 1 and visit[i]!= 1:
      visit[i] = 1 
      stk[top] = i 
      top += 1
  top -= 1
  v = stk[top]
  #Menampilkan rute yang dilewati   
  print(namanya[v])
  k += 1
  visit[v] = 0
  visited[v] = 1


