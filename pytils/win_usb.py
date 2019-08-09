import win32file

def locate_usb():
	drive_list = []
	drivebits = win32file.GetLogicalDrives()
	for d in range(1,26):
		mask = 1 << d
		if drivebits & mask:
			drive_name = '{}:\\'.format(chr(ord('A')+d))
			drive_type = win32file.GetDriveType(drive_name)			
			if drive_type == win32file.DRIVE_REMOVABLE:
				drive_list.append(drive_name)
	return drive_list

if __name__ == '__main__':
	lst = locate_usb()
	print(lst)
