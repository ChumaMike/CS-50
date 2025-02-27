stt = input("input: ").strip()

vowels = "aeiouAEIOU"
new = ""
for word in stt:
    if word not in vowels:
        new += word

print(new)