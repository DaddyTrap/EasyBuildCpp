# EasyBuildCpp
Easily build several cpp files. Only for small program but not suitable for a big project.

## Preface
Only tested in Sublime Text 3103 in Ubuntu 16.04 now.

## Installation
Well, I have not already submit this to Package Control because I think I can't meet its requirement.(Maybe I will, soon)
So, the installation seems a little difficult.

1. Open Sublime Text.
2. In the menu, Preference->Browse Package...
3. In the window, Right-click and choose "New folder"
4. Name it like "EasyBuildCpp" or other things you want
5. Copy all my files into the folder
6. Done

>At the first time I tried, Package Control removed my folder and said something about "Permission". In case of this, try "chmod 777 [folder_name]" if you don't mind.

## Usage
1.Switch the file you want to compile.
2.```Ctrl+Shift+P```(*Default*) to call the ```command palette```
3.Input "Easy Build Cpp: Build" or just "ebcb"(sublime will find the command) and execute it.

>Notice: It will add all the .cpp files together with the file in focus to the compile list. So this is a really simple plugin.
