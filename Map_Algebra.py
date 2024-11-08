# Map Algebra Demo

# Created by: Iyanuoluwa Emmanuel Fatunmbi
# Created on: 03-28-2024

print ("Importing modules...")
import sys, arcpy, traceback
try:
    if arcpy.CheckExtension('Spatial') == 'Available':
        r_dataset = r'D:\EsriPress\Python\Data\Colorado\elevation'
        arcpy.CheckOutExtension('Spatial')  #Check out extension before the code line that runs the analysis
        r_object = arcpy.Raster(r_dataset)  #To create the raster tool in memory
        new_raster = r_object * 3.2808399
        new_raster.save(r'D:\temp\elevation_feet.tif')
        arcpy.CheckInExtension('Spatial')   #Remember to check in the extension after running the analysis
    else:
        print('Spatial analyst extension not found')


except:
    # (SYS MODULE) Exception info. THIRD ELEMENT OF TUPLE: (0:type of the exception, 1:the exception itself, 2:traceback object)
    tb = sys.exc_info()[2]
    # (TRACEBACK MODULE) ATTRIBUTES: filename, lineno, name, and stack trace line
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])
    # GetMessages OPTIONS: 0:informative + warning + error messages, 1:warning messages, 2:error messages
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)
    print (msgs)
    print (pymsg)

    arcpy.AddMessage(arcpy.GetMessages(1))
    print (arcpy.GetMessages(1))
