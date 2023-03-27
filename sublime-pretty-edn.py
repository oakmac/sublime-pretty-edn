# Sublime Pretty EDN
# v0.3.0
# https://github.com/oakmac/sublime-pretty-edn
#
# Copyright (c) 2023, Chris Oakman
# Released under the ISC license
# https://github.com/oakmac/sublime-pretty-edn/blob/master/LICENSE.md

import os
import pathlib
import shutil
import sublime
import sublime_plugin
import subprocess

# TODO:
# - on plugin load, check for existence of "bb" and warn if not found
# - the babashka scripts could probably be combined (could even be just one script)

def check_for_bb():
    bb_exists = shutil.which('bb')
    if bb_exists:
        return True
    else:
        sublime.status_message('Could not find babashka (bb). Is it installed?')
        return False


class PrettyEdnFormat(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            format_script = os.path.join(plugin_dir, "scripts/format_edn.clj")
            result = subprocess.run([format_script], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Unable to format. Invalid EDN 👎')
            else:
                ## set the buffer with the pretty-printed result
                self.view.replace(edit, whole_region, result.stdout)
                sublime.status_message('EDN formatted')


class PrettyEdnMinify(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            minify_script = os.path.join(plugin_dir, "scripts/minify_edn.clj")
            result = subprocess.run([minify_script], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Unable to minify. Invalid EDN 👎')
            else:
                ## set the buffer with the pretty-printed result
                self.view.replace(edit, whole_region, result.stdout)
                sublime.status_message('EDN minified')


class PrettyEdnValidate(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            ## NOTE: the minify script doubles as the validate script
            minify_script = os.path.join(plugin_dir, "scripts/minify_edn.clj")
            result = subprocess.run([minify_script], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Invalid EDN 👎')
            else:
                sublime.status_message('Valid EDN 👍')


class PrettyEdnToJsonMinified(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            to_json_script = os.path.join(plugin_dir, "scripts/to_json.clj")
            result = subprocess.run([to_json_script, "minified"], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Invalid EDN 👎')
            else:
                ## set the buffer with the result
                self.view.replace(edit, whole_region, result.stdout)
                sublime.status_message('EDN converted to minified JSON')


class PrettyEdnToJsonPretty(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            to_json_script = os.path.join(plugin_dir, "scripts/to_json.clj")
            result = subprocess.run([to_json_script], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Invalid EDN 👎')
            else:
                ## set the buffer with the result
                self.view.replace(edit, whole_region, result.stdout)
                sublime.status_message('EDN converted to JSON')


class PrettyEdnFromJson(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            from_json_script = os.path.join(plugin_dir, "scripts/from_json.clj")
            result = subprocess.run([from_json_script], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Invalid JSON 👎')
            else:
                ## set the buffer with the result
                self.view.replace(edit, whole_region, result.stdout)
                sublime.status_message('JSON converted to EDN')


class PrettyEdnFromJsonKeywordized(sublime_plugin.TextCommand):
    def run(self, edit):
        if check_for_bb():
            whole_region = sublime.Region(0, self.view.size())
            all_text = self.view.substr(whole_region)

            plugin_dir = pathlib.Path(__file__).parent.absolute()
            from_json_script = os.path.join(plugin_dir, "scripts/from_json.clj")
            result = subprocess.run([from_json_script, "keywordize"], input=all_text, capture_output=True, text=True)

            if result.stderr != "":
                sublime.status_message('Invalid JSON 👎')
            else:
                ## set the buffer with the result
                self.view.replace(edit, whole_region, result.stdout)
                sublime.status_message('JSON converted to EDN keywordized')
