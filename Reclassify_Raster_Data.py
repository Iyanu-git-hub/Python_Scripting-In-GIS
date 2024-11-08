# Reclassify Demo

# Created by: Iyanuoluwa Emmanuel Fatunmbi
# Created on: 03-26-2024

print ("Importing modules...")
import sys, arcpy, traceback
try:
    # Reclassify(in_raster, reclass_field, remap, {missing_values})
    raster_obj = arcpy.Raster(r'D:\EsriPress\Python\Data\Colorado\elevation')
    rrange = arcpy.sa.RemapRange([[0, 2000, 1], [2000, 3000, 2], [3000, 4000, 3]])
    new_raster = arcpy.sa.Reclassify(raster_obj, 'Value', rrange)
    new_raster.save(r'D:\temp\reclass_demo.tif')

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
