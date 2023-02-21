import os
import pathlib
import shutil
import sublime
import sublime_plugin
import subprocess

class PrettyEdnFormat(sublime_plugin.TextCommand):
    def run(self, edit):
        whole_region = sublime.Region(0, self.view.size())
        all_text = self.view.substr(whole_region)

        ## TODO: allow them to set babashka path via setting
        bb_exists = shutil.which("bb")

        ## TODO: What to do here? Update status bar?
        if not bb_exists:
            print("babashka (bb) not found!")
            return

        # directory of the script being run:
        plugin_dir = pathlib.Path(__file__).parent.absolute()
        format_script = os.path.join(plugin_dir, "scripts/format_edn.clj")

        ## run ./scripts/format_edn.clj
        result = subprocess.run([format_script], input=all_text, capture_output=True, text=True)

        if result.stderr != "":
            sublime.status_message('Unable to format. Invalid EDN 👎')
        else:
            ## set the buffer with the pretty-printed result
            self.view.replace(edit, whole_region, result.stdout)
            sublime.status_message('EDN formatted')

class PrettyEdnMinify(sublime_plugin.TextCommand):
    def run(self, edit):
        whole_region = sublime.Region(0, self.view.size())
        all_text = self.view.substr(whole_region)

        ## TODO: allow them to set babashka path via setting
        bb_exists = shutil.which("bb")

        ## TODO: What to do here? Update status bar?
        if not bb_exists:
            print("babashka (bb) not found!")
            return

        # directory of the script being run:
        plugin_dir = pathlib.Path(__file__).parent.absolute()
        format_script = os.path.join(plugin_dir, "scripts/minify_edn.clj")

        ## run ./scripts/format_edn.clj
        result = subprocess.run([format_script], input=all_text, capture_output=True, text=True)

        if result.stderr != "":
            sublime.status_message('Unable to minify. Invalid EDN 👎')
        else:
            ## set the buffer with the pretty-printed result
            self.view.replace(edit, whole_region, result.stdout)
            sublime.status_message('EDN minified')

class PrettyEdnValidate(sublime_plugin.TextCommand):
    def run(self, edit):
        whole_region = sublime.Region(0, self.view.size())
        all_text = self.view.substr(whole_region)

        ## TODO: allow them to set babashka path via setting
        bb_exists = shutil.which("bb")

        ## TODO: What to do here? Update status bar?
        if not bb_exists:
            print("babashka (bb) not found!")
            return

        # directory of the script being run:
        plugin_dir = pathlib.Path(__file__).parent.absolute()
        format_script = os.path.join(plugin_dir, "scripts/minify_edn.clj")

        result = subprocess.run([format_script], input=all_text, capture_output=True, text=True)

        if result.stderr != "":
            sublime.status_message('Invalid EDN 👎')
        else:
            sublime.status_message('Invalid EDN 👍')
