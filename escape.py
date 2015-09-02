from bs4.dammit import EntitySubstitution

esub = EntitySubstitution()
def sanitize_html(title):
	return esub.substitute_html(title)

def sanitize_irc(title):
	badchars = "\r\n\x01"
	return "".join(c for c in title if c not in badchars)

escapers = {
	"html": sanitize_html,
	"irc": sanitize_irc
}

def escape(title, mode):
	if not mode:
		mode = "irc"

	if mode == "all":
		for func in list(escapers.values()):
			title = func(title)
		return title

	return escapers.get(mode, lambda title: title)(title)