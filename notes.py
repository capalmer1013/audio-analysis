import wave
import struct
waveRead = wave.open("assets/sample.wav", "rb")

frame = waveRead.readframes(1)

samples = []
while frame != b'':
	samples.append(struct.unpack_from("<hh", frame))
	frame = waveRead.readframes(1)

unique = list(set(samples))
l = [x[0] for x in samples]
r = [x[1] for x in samples]
lunique = list(set(l))
runique = list(set(r))

freqs = []
prev = l[0]
count = 0

for each in l:
	if prev >=0 and each < 0:
		freqs.append(count)
		count = 0
	prev = each
	count += 1
freqDict = {}
for each in list(set(freqs)):
	freqDict[each] = freqs.count(each)

sorted_by_value = sorted(freqDict.items(), key=lambda kv: kv[1])
a = [x for x in freqs if x > 60]
pairs = []
prev = None
for each in a:
	if prev is None:
		prev = each
		continue
	pairs.append((prev, each))
