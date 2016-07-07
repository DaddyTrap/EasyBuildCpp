import sublime, sublime_plugin
import os
import platform
import subprocess

plat = platform.system()

def read_all_sources(t_dir):
  rootdir = t_dir
  res = []
  for parent, dirnames, filenames in os.walk(rootdir):
    for f in filenames:
      s = f.split('.')
      if len(s) >= 2:
        # try compilation
        if s[1] == 'cpp':
          # print(plat)
          if plat == 'Windows':
            res.append(parent +'\\' + f)
          else:
            res.append(parent +'/' + f)
  return res
  # print(res)

def compile_all_sources(t_list, out_fullname):
  to_exec = 'g++ -g -std=c++11 '
  for file in t_list:
    to_exec += file + ' '
  to_exec += '-o ' + out_fullname
  print('to execute in system:\n' + to_exec)
  print(subprocess.getstatusoutput(to_exec)[1])

class CompileThisCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    # plat = platform.system()
    # self.view.insert(edit, 0, "Hello, World!")
    filename = sublime.View.file_name(self.view)
    print(filename)
    rootdir = os.path.dirname(filename)
    if plat == 'Windows':
      fullname = rootdir + '\\' + os.path.basename(filename).split('.')[0] + '.exe'
    else:
      fullname = rootdir + '/' + os.path.basename(filename).split('.')[0] + '.out'
    compile_list = read_all_sources(rootdir)
    print(compile_list)
    compile_all_sources(compile_list, fullname)