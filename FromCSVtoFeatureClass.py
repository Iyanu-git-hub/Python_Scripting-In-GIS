# Chapter 8 homework

# Created by: Iyanuoluwa Emmanuel Fatunmbi
# Created on: 03-19-2024
# Read from CSV to Featureclass

print ("Importing modules...")
import sys, arcpy, traceback
try:
    arcpy.env.workspace = r'D:\Geog_432\Chapter_8\Homework Chap8\Libraries.gdb'
    FC = "IL_libraries"
    arcpy.AddField_management(FC, "LOGINS", 'LONG')
    arcpy.AddField_management(FC, "LOANS", 'LONG')

    Data_File = r"D:\Geog_432\Chapter_8\Homework Chap8\new_data.csv"
    aFile = "new_data.csv"
    Open_aFile = open(Data_File + "\\" + "aFile")
    Counter = 1
    for afile in Open_aFile:
        if Counter > 1:
            print(afile)
            Store_Data = afile.split(",")
            if Store_Data[0] == "Franklin Park":
                print(Store_Data[1] + ", " + Store_Data[2])
                print("Updating name field of IL_Libraries...")
                Query = "NAME = '" + Store_Data[1] + "'"
                print(Query)

                Update_Cursor = arcpy.da.UpdateCursor(FC, ['LOGINS', 'LOANS'], Query)
                for arow in Update_Cursor:
                    arow[0] = Store_Data[2]
                    arow[1] = Store_Data[3]
                    Update_Cursor.updateRow(arow)
                del Update_Cursor
        Counter = Counter + 1


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
