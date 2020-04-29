import os


def runOverFolder(workingDir, isApproved):
    isFirstRun = True
    for filename in os.listdir(workingDir):
        if filename.endswith(".mkv"):
            if pattern in filename:
                newName = filename.replace(pattern, "")
                if isApproved == False:
                    if isFirstRun == True:
                        print("Are you sure you want to change:")
                        isFirstRun = False
                    print(filename + "  -->  " + newName)
                else:
                    oldPath = os.path.join(workingDir, filename)
                    newPath = os.path.join(workingDir, newName)
                    os.rename(oldPath, newPath)
                    print(newName)


try:
    print('Enter your folder full path:')
    workingDir = input()

    print('Enter thr pattern you want to remove:')
    pattern = input()
    # ask for user approval
    runOverFolder(workingDir, False)
    print('press y to continue n to cancel')
    approval = input()
    if approval == 'y' or approval == 'Y':
        runOverFolder(workingDir, True)


except IOError:
    print('folder not found')
