import sublime
import sublime_plugin

class OpenViewCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.active_view()
		sel = view.sel()
		for text in sel:
			base = view.file_name().split('controllers/')
			base_path = "/".join(base[:-1])
			middle_path = base[-1].split("_controller")[0]
			file_name = base_path+"views/"+middle_path+"/"+view.substr(view.word(text))+".html.erb"
		buffer = self.window.open_file(file_name)