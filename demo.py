import useful_functions as uf
scores = [80,92,79,93,85]

mean = uf.mean(scores)

curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:",scores)
 
print("Original Mean:", mean, " New Mean:", mean_c)