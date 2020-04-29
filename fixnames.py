import os
print('Enter your folder full path:')
workingDir = input()

print('Enter thr pattern you want to remove:')
pattern = input()


for filename in os.listdir(workingDir):
    if filename.endswith(".mkv"):
        newName = filename.replace(pattern, "")
        oldPath = os.path.join(workingDir, filename)
        newPath = os.path.join(workingDir, newName)
        os.rename(oldPath, newPath)
        print(newName)
