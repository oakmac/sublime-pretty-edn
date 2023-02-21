import sublime
import sublime_plugin

class PrettyEdnFormat(sublime_plugin.TextCommand):
    def run(self, edit):
        print("pretty EDN format 99999999")

class PrettyEdnMinify(sublime_plugin.TextCommand):
    def run(self, edit):
        print("pretty EDN minify 11111")

class PrettyEdnValidate(sublime_plugin.TextCommand):
    def run(self, edit):
        print("pretty EDN validation 22222")