from difflib import SequenceMatcher
text1 = "My Name is Valeh Amirbekov"
text2 = "Hi, My Name is Valeh Amirbekov"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")