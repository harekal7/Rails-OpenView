import sublime
import sublime_plugin
import re
import os

class OpenViewCommand(sublime_plugin.WindowCommand):
	
	def search(self, view, text):
		word = view.substr(view.word(text))
		line = view.substr(view.line(text))
		search_result = re.search("def[ ]+%s"%word, line)
		if search_result:
			self.get_view(view, text)
		else:
			search_result = re.search("redirect_to[ ]+:%s"%word, line)
			if search_result:
				self.get_view(view, text)
			else:
				search_result = re.search("redirect_to[ ]+\"%s\""%word, line)
				if search_result:
					self.get_view(view, text)
				else:
					search_result = re.search("render[ ]+\"%s\""%word, line)
					if search_result:
						self.get_view(view, text)
					else:
						search_result = re.search("render[ ]+:action[ ]+=>[ ]+:%s"%word, line)
						if search_result:
							self.get_view(view, text)
						else:
							search_result = re.search("render[ ]+:action[ ]+=>[ ]+\"%s\""%word, line)
							if search_result:
								self.get_view(view, text)

	def get_view(self, view, text):
		base = view.file_name().split('controllers/')
		if len(base)>1:
			base_path = os.path.join(base[:-1])
			print (base_path)
			middle_path = base[-1].split("_controller")[0]
			file_name = base_path[0]+"views/"+middle_path+"/"+view.substr(view.word(text))+".html.erb"
			buffer = self.window.open_file(file_name)

	def run(self):
		view = self.window.active_view()
		sel = view.sel()
		for text in sel:
			self.search(view, text)