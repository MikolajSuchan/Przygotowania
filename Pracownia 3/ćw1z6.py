text = "X-DSPAM-Confidence:0.8475"
przed=text.find(":")
wycinek=text[przed+1:]
wycienk=float(wycinek)
print(wycinek)