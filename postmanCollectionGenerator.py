import os, sys, shutil

input = sys.argv[1]
ramlPath = (input.replace("'", "")) + "/src/main/resources/api/*.raml"
appName = input.split("/")[-1]

runCommand = "java -jar postman-collection-generator.jar -muleAppName " + appName + " -ramlPath " + ramlPath
print("-----------------------------------------------------")
os.system(runCommand)

# Move file to Desktop
for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
    if file.endswith(".json"):
        generatedFileName = file
sourcePath = os.path.dirname(os.path.realpath(__file__)) + "/" + generatedFileName
destinationFolder = '/Users/cbonthala/Desktop/postman-collections'
destinationPath = destinationFolder + "/" + generatedFileName

if not os.path.exists(destinationFolder):
    os.mkdir(destinationFolder)

if os.path.exists(destinationPath):
    os.remove(destinationPath)
shutil.move(sourcePath, destinationFolder)
