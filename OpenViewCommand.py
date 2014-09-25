import sublime
import sublime_plugin

class OpenViewCommand(sublime_plugin.WindowCommand):
	def run(self):
		window = self.window
		view = window.active_view()
		sel = view.sel()
		for s in sel:
			base_path = view.file_name().split('/')[:-2]
			base_path = "/".join(base_path)
			view_names = view.file_name().split('/')[-1].split('_')[:-1]
			view_name = "_".join(view_names)
			file_name = base_path+"/views/"+view_name+"/"+view.substr(s)+".html.erb"
			print (file_name)
		buffer = window.open_file(file_name)