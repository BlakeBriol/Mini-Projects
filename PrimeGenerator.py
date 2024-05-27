TestV = range(7013)
TestList = []
for N in TestV:
	for V in range(2,N):
		TestList.append(int(N/V)-float(N/V))
	if 0.0 not in TestList:
		print(f"{N} Prime")
		del TestList[:]
	else:
		print(f"{N} Not Prime")
		del TestList[:]