user_passward=str(raw_input('Inter your passward >'))
if 6 <= len(user_passward) and len(user_passward) < 16:
		if '$' in user_passward:
			if '2' or '9' in user_passward:
				if 'A' or 'Z' in user_passward:
					print 'passward strong hai'
		else:
			print 'passward week hai'
else:
	print 'bhai passward kam dala hai\nnahi to jada dala hai'
