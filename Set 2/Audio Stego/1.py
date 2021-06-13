import wave
audio = wave.open("1.wav", mode='rb')
frame_bytes = bytearray(list(audio.readframes(audio.getnframes())))
extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
decoded = string.split("###")[0]
print("Sucessfully decoded: "+decoded)
audio.close()	
