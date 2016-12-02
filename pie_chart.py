 
def draw_pie_chart(all_history):
	error_msg = "History is empty"
	if all_history != []:
		reason_and_count = []
		all_reason = []
		reasons = []
		key_error_msg = "Invalid Input"
		try:
			for history in all_history:
				all_reason.append(history['reason'])
				if not history['reason'] in reasons :
					reasons.append(history['reason'])
		except KeyError:
			return [[key_error_msg,0]]

		for reason in reasons:
			reason_and_count.append([reason, all_reason.count(reason)])

		return reason_and_count
	else:
		return [[error_msg,0]]

		
	
	
