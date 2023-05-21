import os
import re

class VideoFile:
    def __init__(self, fileName, fileType):
        self.fileName = fileName
        self.fileType = fileType
        self.determineDestination()
    
    def determineDestination(self):
        if self.fileType == 'movie':
            self.fileDest = 'C:\\Users\\tjbre\\Desktop\\Media\\Movies'
        else:
            self.fileDest = "C:\\Users\\tjbre\\Desktop\\Media\\TV Shows"
    
    def checkIfFileExists(self):
        if self.fileName in os.listdir(self.fileDest): return True
    
    def removeExistingFile(self):
        os.rmdir(f"{self.fileDest}\{self.fileName}")
        self.makeDestDir()
    
    def makeDestDir(self):
        os.mkdir(f"{self.fileDest}\{self.fileName}")
        
    def moveFile(self, sourcePath):
        os.rename(sourcePath, f"{self.fileDest}\{self.fileName}\{self.fileName}.txt")


encodedFilePath = "C:\\Users\\tjbre\\Desktop\\handbrake\\encoded"
encodedFiles = os.listdir(encodedFilePath)

for file in encodedFiles:
    fileName = file.split(".")[0]
    
    if re.search("-[s][0-9]*[e][0-9]*", fileName):
        fileObj = VideoFile(fileName, fileType="tv")
    else:
        fileObj = VideoFile(fileName, fileType="movie")

    if fileObj.checkIfFileExists():
        fileObj.removeExistingFile()
    else:
        fileObj.makeDestDir()
    
    sourcePath = f"{encodedFilePath}\{file}"
    fileObj.moveFile(sourcePath)