text = "X-DSPAM-Confidence:    0.8475"
t=text.find(' ')
s=text[t+1:]
print(float(s))
