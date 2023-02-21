import sublime
import sublime_plugin
import shutil
import os
import subprocess

class PrettyEdnFormat(sublime_plugin.TextCommand):
    def run(self, edit):
        whole_view_region = sublime.Region(0, self.view.size())
        all_text = self.view.substr(whole_view_region)

        # TODO: allow them to set babashka path via setting
        bb_exists = shutil.which("bb")
        jet_exists = shutil.which("jet")

        if not jet_exists:
        	print("jet not found!")
        	return

        #print("do something now")

        # subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None, **other_popen_kwargs)
        result = subprocess.run(
            ["jet", "--to", "edn", all_text], capture_output=True, text=True
        )
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)

        ## Possibles:
        ## - os.system('bb foo')
        ## - os.spawn
        ## - subprocess.run

class PrettyEdnMinify(sublime_plugin.TextCommand):
    def run(self, edit):
        print("FIXME: pretty EDN minify")
        one = shutil.which("cat")
        two = shutil.which("bb")

        if one:
        	print("yes to one")

        if two:
        	print("yes to two")

class PrettyEdnValidate(sublime_plugin.TextCommand):
    def run(self, edit):
        whole_view_region = sublime.Region(0, self.view.size())
        all_text = self.view.substr(whole_view_region)
        print(all_text)
        self.view.replace(edit, whole_view_region, all_text + "zzz")