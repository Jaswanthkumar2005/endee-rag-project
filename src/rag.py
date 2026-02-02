from search import search

query = input("Ask a question: ")
result = search(query)

print("\nAnswer based on stored documents:\n")
print(result)
