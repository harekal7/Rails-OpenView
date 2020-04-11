import sublime
import sublime_plugin
import os
import re

class RailsOpenViewCommand(sublime_plugin.WindowCommand):

	search_expressions = (r'def +%s',
					  					r'redirect_to +:action +=> +:%s',
                      r'redirect_to +:action +=> +"%s"',
                      r"redirect_to +:action +=> +'%s'",
                      r"redirect_to +action: +'%s'",
                      r'redirect_to +"%s"',
                      r"redirect_to +'%s'",
                      r'redirect_to +:%s',
                      r'render +:action +=> +:%s',
                      r'render +:action +=> +"%s"',
                      r"render +:action +=> +'%s'",
                      r"render +action: +'%s'",
                      r'render +"%s"',
                      r"render +'%s'",
                      r"render +:%s")

	extensions = ('.html.erb', '.json.jbuilder', '.js.erb', '.slim', '.html.haml', '.js.haml')

	def search(self, view, text):
		word = view.substr(view.word(text))
		line = view.substr(view.line(text))

		search_result = any(re.search(e % word, line) for e in self.search_expressions)
		if search_result:
			self.get_view(view, text)

	def get_view(self, view, text):
		base = view.file_name().split('controllers/')

		if len(base) > 1:
			base_path = os.path.join(base[:-1])
			middle_path = base[-1].split("_controller")[0]

			file_name_sans_extension = base_path[0] + "views/" + middle_path + "/" + view.substr(view.word(text))

			for ext in self.extensions:
				file_name = file_name_sans_extension + ext
				if os.path.exists(file_name):
					break

			self.window.open_file(file_name)

	def run(self):
		view = self.window.active_view()
		sel = view.sel()
		for text in sel:
			self.search(view, text)
