import sublime
import sublime_plugin
import os
import re

class RailsOpenViewCommand(sublime_plugin.WindowCommand):

	def search(self, view, text):
		word = view.substr(view.word(text))
		line = view.substr(view.line(text))
		search_str = "def[ ]+"+word+\
					 "|redirect_to[ ]+:"+word+\
					 "|redirect_to[ ]+\""+word+"\""\
					 "|redirect_to[ ]+:action[ ]*=>[ ]*:"+word+\
					 "|redirect_to[ ]+:action[ ]*=>[ ]*\""+word+"\""\
					 "|redirect_to[ ]+:action[ ]*=>[ ]*\'"+word+"\'"\
					 "|render[ ]+:"+word+\
					 "|render[ ]+\""+word+"\""\
					 "|render[ ]+:action[ ]*=>[ ]*:"+word+\
					 "|render[ ]+:action[ ]*=>[ ]*\""+word+"\""\
					 "|render[ ]+:action[ ]*=>[ ]*\'"+word+"\'"

		search_result = re.search(search_str, line)
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