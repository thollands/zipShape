# ===========================================================================
#   Copyright:  Spatial Vision Innovations Pty Ltd 2014
# ===========================================================================
#   Contact:    Tom Hollands - (03) 9691 3000 - Tom.Hollands@spatialvision.com.au
#   Author:     Tom Hollands - (03) 9691 3000 - Tom.Hollands@spatialvision.com.au
#   Website:    www.spatialvision.com.au
#   Address:    Level 4, 575  Bourke Street, Melbourne, VIC, 3000
#   ABN:        28 092 695 951
# ===========================================================================
# Disclaimer:   This script has been developed for it's intended purpose and
#               client only. Spatial Vision does not warrant the use of this
#               script or modified version outside its intended purpose.
#               Spatial Vision accepts no responsibility for damage loss or
#               injury caused by modification or the use of this script outside
#               its intended purpose
# ===========================================================================
#   Script Name:        zipShape
#   Description:        Zips collections of shapefile files into
#   Script Version :    1.0
#   Python Version:     Python 3.4
#   Date Created:       03/05/2016
#
#   Script Version Notes:
#       Version 01.0 - (03/05/2016) is the initial build - still bugged and not adding all files
# ===========================================================================
# SCRIPT BEGINS
# ===========================================================================
#


# define folder with shapefiles
# drive letter must be lower case
folder = r"c:\scripts\zipShape\test_dir"

def zipShapeFiles(path):

    """

    :param path:
    :return:
    """

    # Import system modules
    import zipfile, os, glob

    # array of valid shapefile extensions
    shpDic = ['.shp', '.shx', '.dbf', '.prj', '.sbn', '.sbx', '.fbn', '.fbx',
              '.ain', '.aih', '.ixs', '.mxs', '.atx', '.shp.xml', '.cpg', '.qix']

    print("start")

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
            os.remove(zipName)
            print(zipName + " deleted")
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
