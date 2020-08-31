def boyer_moore(text, pattern):
	t, p = len(text), len(pattern)
	comp = 0

	if p == 0:
		return 0
    # returns 0 if pattern is empty. (An empty string is a substring of any string).

	last_index = {}
	#build last index dictionary to keep track on which characters are in the pattern. 

	for i in range(p):
		last_index[pattern[i]] = i
	i = p - 1
	j = p - 1
	while i < t:
		comp += 1
		if text[i] == pattern[j]:
			if j == 0:
				return "The pattern starts at index: " + str(i) + ". Number of comparisons: " + str(comp/t)
			i -= 1
			j -= 1
		else:
			k = last_index.get(text[i], -1)
			i += p - min(j, k + 1)
			j = p - 1
	return "No match."

haystack = "abcdefghijklmnopqrstuvwxyz"
needle = "ghi"
print(boyer_moore(haystack, needle))