# Created by: Iyanuoluwa E. Fatunmbi
# Created on: 02-01-2024
#Select By Attribute

print ("Importing modules...")
import sys, arcpy, traceback
try:
    fac_fc = r'D:\EsriPress\Python\Data\Austin-TX\facilities.shp'
    #arcpy.management.SelectLayerByAttribute(in_layer_or_view, {selection_type}, {where_clause}, {invert_where_clause})
    # FACILITY = 'RECREATION CENTER'
    query = "FACILITY = 'RECREATION CENTER'"
    fac_fl = arcpy.management.SelectLayerByAttribute(fac_fc, 'NEW_SELECTION', query)
    theCount = int(arcpy.GetCount_management(fac_fl).getOutput(0))
    print(theCount)
    #arcpy.management.CopyRows(in_rows, out_table, {config_keyword})
    out_table = r'd:\temp\demo1_output_python.dbf'
    arcpy.management.CopyRows(fac_fl, out_table)

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
