# Name: Lasercut53.exe
# MD5: FCE2E1E847287FD862BCB5DB858C0C1A

import msvcrt as m

offset = 0x96910
before = "6AFF6888BF500064A100000000"
after = "B8010000009090C39090909090" # mov eax, 1, retn


def wait():
	m.getch()
	
def toArray(s):
	return bytearray.fromhex(s)

def fromArray(s):
	return ''.join('{:02X}'.format(x) for x in s)

with open('Lasercut53.exe', 'rb') as fh:
	fh.seek(offset, 0);
	inp = fh.read(13);
	bytes = fromArray(inp);
	
	fh.seek(0, 0);
	buf = fh.read()
	print(bytes)
	if (bytes == before):
		print("patch to Lasercut53_NoDongle.exe...");
		with open('Lasercut53_NoDongle.exe', 'wb') as wh:
			wh.write(buf)
			wh.seek(offset, 0);
			wh.write(toArray(after));
		
	elif (bytes == after):
		print("file is already patched!!");
	else:
		print("file is corrupt or wrong version!!");
	

print("Press any key to exit.");
wait();

