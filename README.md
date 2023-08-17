# FoldersToTagsScript

[Github Link](https://github.com/ReessKennedy/FoldersToTagsScript)

## What ⚡
Scans a directory for all markdown files in all folders and subfolders and automatically writes tags to the top of each files based on the file's current folder location. 
## Why 🤷‍♂️
If you have been using a folder-based structure to organize your markdown files but want to try using a tag-based method, this helps--especially if you have thousands of notes. Specifically designed to help the creator experiment with using tags instead of folders inside the amazing Obsidian note taking app.  
## How 📋
Run the script in your terminal via something like `Python /path/to/script.py` or you may have to do something like `Python3 /path/to/script.py`

The script will then ask you for the path your wish to analyze and the contents of which you wish to modify. You can just drag the folder into your terminal to quickly print the path. 

Then just hit enter!
## Notes 📋
- Tags are printed to the top of your markdown files
- If a tag already exists at the top of your file (only scans first 3 lines) then the new tag representing the folder path will be prepended before this tag
- If no tag exists then the new tag will be added on a new line and push down any current contents in the file
- I have avoided imported the RegEx library for Python to keep things simple so I do a simple check to determine how to insert that tags that does not rely on RegEx but does add an additional conditional just to look for markdown h1 and h2 elements that might also be starting a file to not confuse those with tags and make sure the new tag isn't mistakenly prepended on the same line before them. 
- A nice little counter was added to show the number of new tags added after complete
- The script also checks to see whether this tag already exists in a file and does not write it again if it does and then communicates the number of files skipped because of the preexistence of the new tag already. 
- You can easily modify this to work with plaintext as well
- I had added a fancy "Processing ..." animation but it added too much complexity and the actually processing time for this simple task is quite short, even with many files, so I removed it in the interest of simplicity
