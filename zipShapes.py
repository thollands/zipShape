import zipfile, os, glob

print("start")

# define folder with shapefiles
# drive letter must be lower case
folder = r"c:\scripts\test_dir"

# distionary of valid shapefile extensions
shpDic = ['.shp', '.shx', '.dbf', '.prj', '.sbn', '.sbx', '.fbn', '.fbx',
          '.ain', '.aih', '.ixs', '.mxs', '.atx', '.shp.xml', '.cpg', '.qix']

def zipShapeFiles(path):

    # get all files in specified folder
    directory = os.listdir(path)

    # find shapefiles in folder
    fileList = glob.glob(path + "\\*.shp")
    print("shapefiles:", fileList)

    # loop over each file
    for file in directory:

        # get extension for file
        ext = os.path.splitext(file)[-1].lower()

        # check if extension is a valid shapefile
        if (ext in shpDic or '.shp' + ext in shpDic):
            print("valid: " + file)

        # if not remove it from the list of files so it is not zipped
        else:
            directory.remove(file)
            print("exclude: " + file)

    print("to zip:", directory)

    # loop over each shapefile
    for label in fileList:

        zipName = label + ".zip"
        # check if zip file exists, if it does do nothing, if not continue
        if (os.path.isfile(zipName)):
            print(zipName + " already exists")
            pass
        else:
            #  create zip file
            zipit = zipfile.ZipFile(zipName, "w")
            print("zip created: " + zipName)

            # loop over each file
            for file in directory:

                # define full file name (incl path) and split label name
                fileName = path + "\\" + os.path.splitext(file)[-2].lower()
                labelName = os.path.splitext(label)[-2].lower()

                # check is file matches zip name (ie if it belongs there), if it does add it to the zip. OR statement accounts for .shp.xml files
                if ((fileName == labelName) or (fileName[:-3].endswith('.') and os.path.splitext(fileName)[-2].lower() == labelName)):
                    zipit.write(label, file, zipfile.ZIP_STORED)
                    print(file + " > " + label + ".zip")

            # close zip
            zipit.close()

# run function
zipShapeFiles(folder)

print('end')
