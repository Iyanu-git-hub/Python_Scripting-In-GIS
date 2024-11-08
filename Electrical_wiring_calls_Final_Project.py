# Created by: Iyanuoluwa Emmanuel Fatunmbi
# Created on: 04-08-2024

print ("Importing modules...")
import sys, arcpy, traceback
try:
    path = r'C:\Users\USER\Desktop\Courses\GEOG 432\Geog_432\Electrical wiring calls\Electrical wiring calls.gdb'
    arcpy.env.workspace = path
    # DECLARE THE NEIGHBORHOOD FEATURE CLASS (V1A)
    Neighbourhood_fc = 'Neighborhoods'
    # DECLARE THE SACRAMENTO FIRE DEPT FEATURE CLASS (V1B)
    Sac_Fire_Dept = 'Sacramento_Fire_Dep_Projected'
    # LEAVE THE 2 LINES BELOW. THEY DECLARE THE NAMES FOR THE 2 FEATURE CLASSES ABOVE.
    neigh_fl = 'neigh_fl'
    sac_fl = 'sac_fl'
    # USE THE 2 LINES BELOW TO CREATE THE 2 FEATURE LAYERS. JUST REPLACE THE VALUES OF V1A AND V1B.
    # NOTE: FROM NOW ON YOU WILL USE THE FEATURE LAYERS neigh_fl AND sac_fl. NOT THE FEATURE CLASSES.
    # SAMPLE CODE:
    arcpy.MakeFeatureLayer_management(Neighbourhood_fc, neigh_fl)
    arcpy.MakeFeatureLayer_management(Sac_Fire_Dept, sac_fl)

    # NOW, DECLARE AN EMPTY DICTIONARY V3; THIS DICTIONARY WILL BE USED TO STORE NEIGHBORHOOD AND COUNT INFO.
    dictionary = {}
    # CREATE A SEARCH CURSOR V4 TO READ THE NEIGHBORHOOD 'NAME' FIELD FROM THE neigh_fl.
    # NO QUERY NEEDED BECAUSE YOU ARE READING ALL THE RECORDS.
    SearchCursor = arcpy.da.SearchCursor(neigh_fl, ['NAME'])
    # FOR EACH ROW IN THE SEARCH CURSOR:
    # SAMPLE CODE: for V5 in V4:
    for aCursor in SearchCursor:
        # USE THE SAMPLE CODE LINE BELOW AS THE QUERY (V6) FOR THE SEL BY ATT CALL BELOW. REPLACE V5 WITH YOUR
        #   VARIABLE, AND THE 999 CORRESPONDS TO THE INDEX OF THE 'NAME' FIELD IN THE SEARCH CURSOR FIELDS LIST.
        # V6 = """ NAME ='""" + V5[999].replace("'", "''") + """' """
        Query = """ NAME ='""" + aCursor[0].replace("'", "''") + """' """
        # TEST: PRINT V6 AND YUU SHOULD SEE MULTIPLE LINES LIKE
        #        NAME ='Morrison Creek'
        print(Query)
        # SELECT BY ATTRIBUTE A NEIGHBORHOOD BASED ON QUERY V6.
        # SAMPLE CODE:     arcpy.SelectLayerByAttribute_management(neigh_fl, 'NEW_SELECTION', V6)
        arcpy.SelectLayerByAttribute_management(neigh_fl, 'NEW_SELECTION', Query)
        # SELECT BY LOCATION FEATURES IN SAC FIRE DEP (sac_fl) THAT ARE INTERSECTED BY THE NEIGH FEATURE LAYER.
        # NOTE: NO NEED TO HAVE A VARIABLE ON THE LEFT. sac_fl IS A FEATURE LAYER SO IT WILL KEEP THE SELECTION.
        arcpy.management.SelectLayerByLocation(sac_fl, "INTERSECT", neigh_fl)
        # USE THE GetCount FUNCTION (CHAP 5 EXTENDED MATERIAL) TO FIND OUT HOW MANY FEATURES ARE SELECTED
        #   IN THE sac_fl FEATURE LAYER. SAVE THIS COUNT IN V7
        theCount = int(arcpy.GetCount_management(sac_fl).getOutput(0))
        print(f'Number of features selected: {theCount}')
        # if V7 > 0:      # IF TRUE THEN THERE IS FIRE DEPT DATA TO LOOK INTO.
        if theCount > 0:
            # CREATE A QUERY (V8) TO SELECT FROM THE SAC FIRE DEP DATA (Incident_T FIELD) THAT HAVE THE
            #   SPECIFIC VALUE OF '440 Electrical  wiring/equipment problem, other'
            # WE ARE LOOKING FOR CASES WITH THAT SPECIFIC VALUE. USE ARCGIS PRO TO BUILD THE SQL QUERY.
            New_Query = "Incident_T = '440 Electrical  wiring/equipment problem, other'"
            # SELECT BY ATTRIBUTE FROM SAC FIRE DEP FEAT LAYER (sac_fl) USING V8; THIS IS A SUBSET SELECTION PROCESS.
            # NOTE: NO NEED TO HAVE A VARIABLE ON THE LEFT. sac_fl IS A FEATURE LAYER SO IT WILL KEEP THE SELECTION.
            arcpy.SelectLayerByAttribute_management(sac_fl, 'SUBSET_SELECTION', New_Query)
            # USE THE GetCount FUNCTION (CHAP 5 EXTENDED MATERIAL) TO FIND OUT HOW MANY FEATURES ARE SELECTED
            #   IN THE sac_fl FEATURE LAYER. SAVE THIS COUNT IN V9
            New_Count = int(arcpy.GetCount_management(sac_fl).getOutput(0))
            print(f'Number of features selected: {New_Count}')
            # IF THE COUNT IN V9 IS > 0 THEN:   (IF TRUE, THERE ARE '440 Electrical  wiring/equipment problem, other' CASES.)
            if New_Count > 0:
                # ADD TO THE DICTIONARY V3 THE NEIGHBORHOOD NAME (ROW[999]) AS THE KEY
                #   AND THE LAST COUNT AS THE VALUE.
                # SAMPLE CODE: V3[ V5[999] ] = V9
                dictionary[aCursor[0]] = New_Count
    # USE A FOR LOOP TO SHOW THE KEY:VALUE PAIRS FROM THE DICTIONARY. TO SORT THE DICTIONARY YOU CAN DO
    #   SOMETHING LIKE THE SAMPLE CODE BELOW:
    # for aKey in sorted(V3):
    for aKey in sorted(dictionary):
    #    # LINE TO PRINT THE NEIGH AND THE COUNT HERE
    #     print (f'Neighborhood: {aKey}, Count: {V3[aKey]}')
        print(f'Neighbourhood: {aKey}, Count: {dictionary[aKey]}')
    # THE PRINT FUNCTION FROM THIS FOR LOOP WILL SHOW MULTIPLE LINES LIKE THE ONES BELOW:
    # Neighborhood: Valley Hi / North Laguna, Count: 3
    # Neighborhood: Wills Acres, Count: 3

    # THIS IS THE END OF THE PSEUDOCODE.

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
