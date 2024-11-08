#Assignment Chapter 5 Extended

# Created by: Iyanuoluwa Emmanuel Fatunmbi
# Created on: 02-05-2024
#Intersect Tool

print ("Importing modules...")
import sys, arcpy, traceback
try:
    arcpy.env.workspace = r'D:\EsriPress\Python\Data\Austin-TX'
    Output = r"d:\temp\output_assignment.shp"
    #arcpy.analysis.Intersect(in_features, out_feature_class, {join_attributes}, {cluster_tolerance}, {output_type})
    if arcpy.Exists(Output):
        arcpy.Delete_management(Output)
    arcpy.analysis.Intersect('paths.shp', 'zip.shp', Output)
    print(arcpy.GetMessages())


except:

    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " + str(sys.exc_info()[1])

    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    print (msgs)
    print (pymsg)

    arcpy.AddMessage(arcpy.GetMessages(1))
    print (arcpy.GetMessages(1))
