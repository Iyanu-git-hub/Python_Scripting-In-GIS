# IMPLICIT RASTER CELL ITERATOR SAMPLES
# Created by: Iyanuoluwa Emmanuel Fatunmbi
# Created on: 03-30-2024

print ("Importing modules...")
import sys, arcpy, traceback, math, os
try:
    arcpy.env.overwriteOutput = True
    folder = r'D:\Geog_432\Chapter_10\Raster_Cell_Iterator\Single-band example'
    output_band_5 = folder + r'\Clipped_band5.tif'

    print('Exporting band 5 ...')
    raster_dataset = folder + r'\Original Sample Raster\multi_band_clipped.tif\Band_5'

    # arcpy.management.CopyRaster(in_raster, out_rasterdataset, {config_keyword}, {background_value},
    #   {nodata_value}, {onebit_to_eightbit}, {colormap_to_RGB}, {pixel_type}, {scale_pixel_value},
    #   {RGB_to_Colormap}, {format}, {transform}, {process_as_multidimensional}, {build_multidimensional_transpose})
    arcpy.CopyRaster_management(raster_dataset, output_band_5)
    #####################################

    print ('Getting cols and rows count...')
    desc = arcpy.da.Describe(output_band_5)
    rows, cols = None, None
    if desc['dataType'] == "RasterDataset":
        arcpy.env.workspace = output_band_5
        bands = arcpy.ListRasters()  # GET LIST OF RASTER BANDS
        for a_band in bands:
            band_desc = arcpy.da.Describe(a_band)
            cols = band_desc['width']
            rows = band_desc['height']
            print (f'{a_band}: width: {cols}, height: {rows}')
            break

    ###############################################
    # CREATING 4 PIXEL NO DATA FRAME AROUND RASTER
    ###############################################
    print()
    print('Creating copy of raster...')
    frame_width = 2     # IN PIXELS
    two_pix_frame = folder + r'\two_px_frm.tif'
    arcpy.CopyRaster_management(output_band_5, two_pix_frame)
    print(f'Creating {frame_width} pix frame raster...')
    raster_obj = arcpy.sa.Raster(two_pix_frame)
    raster_obj.readOnly = False
    for i, j in raster_obj:
        if i < frame_width or i >= rows - frame_width:
            raster_obj[i,j] = math.nan
        if j < frame_width or j >= cols - frame_width:
            raster_obj[i,j] = math.nan
    raster_obj.save()

    ################################################
    # CONVERTING VALUES > 125 TO NOT A VALUE
    ################################################
    print()
    print('Creating copy of raster...')
    Reclassify_Image = folder + r'\Reclassify_Image.tif'
    arcpy.CopyRaster_management(output_band_5, Reclassify_Image)
    print('Reclassifying Raster Image Values...')
    raster_obj = arcpy.sa.Raster(Reclassify_Image)
    raster_obj.readOnly = False
    for i, j in raster_obj:
        if raster_obj[i,j] >= 0 and raster_obj[i,j] <= 80:
            raster_obj[i,j] = math.nan      # SET VALUE TO 'NO DATA'
        elif raster_obj[i,j] > 80 and raster_obj[i,j] < 120:
            raster_obj[i,j] = 1
        elif raster_obj[i,j] >= 120:
            raster_obj[i,j] = 2
        else:
            print("I can't do this...")
    raster_obj.save()

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
