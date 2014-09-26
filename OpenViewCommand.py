import sublime
import sublime_plugin
import re

class OpenViewCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.active_view()
		sel = view.sel()
		for text in sel:
			word = view.substr(view.word(text))
			line = view.substr(view.line(text))
			search_result = re.search("def[ ]+%s"%word, line)
			if search_result:
				base = view.file_name().split('controllers/')
				base_path = "/".join(base[:-1])
				middle_path = base[-1].split("_controller")[0]
				file_name = base_path+"views/"+middle_path+"/"+view.substr(view.word(text))+".html.erb"
				buffer = self.window.open_file(file_name)