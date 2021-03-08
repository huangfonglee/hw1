# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061201.csv'
data = []
header = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames

   for row in mycsv:
      data.append(row)    # put row into data
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:

# Retrive all data points which station id is "C0X260" as a list.

target_data = list(filter(lambda item: (item['station_id'] == 'C0A880' or item['station_id'] == 'C0F9A0' or item['station_id'] == 'C0G640' or item['station_id'] == 'C0R190' or item['station_id'] == 'C0X260'), data))

# Retrive ten data points from the beginning.

# target_data = data[:10]

#=======================================
# Part. 4

#=======================================

# Print result

TEMP_C0A880 = 0.0
TEMP_C0F9A0 = 0.0
TEMP_C0G640 = 0.0
TEMP_C0R190 = 0.0
TEMP_C0X260 = 0.0

for i in range(len(target_data)):
   if target_data[i]['station_id'] == 'C0A880' :
      if target_data[i]['TEMP'] == '-99.000' or target_data[i]['TEMP'] == '-999.000' :
         TEMP_C0A880 = TEMP_C0A880
      else :
         if float(target_data[i]['TEMP']) > TEMP_C0A880:
            TEMP_C0A880 = float(target_data[i]['TEMP'])
   elif target_data[i]['station_id'] == 'C0F9A0' :
      if target_data[i]['TEMP'] == '-99.000' or target_data[i]['TEMP'] == '-999.000' :
         TEMP_C0F9A0 = TEMP_C0F9A0
      else :
         if float(target_data[i]['TEMP']) > TEMP_C0F9A0:
            TEMP_C0F9A0 = float(target_data[i]['TEMP'])
   elif target_data[i]['station_id'] == 'C0G640' :
      if target_data[i]['TEMP'] == '-99.000' or target_data[i]['TEMP'] == '-999.000' :
         TEMP_C0G640 = TEMP_C0G640
      else :
         if float(target_data[i]['TEMP']) > TEMP_C0G640:
            TEMP_C0G640 = float(target_data[i]['TEMP'])
   elif target_data[i]['station_id'] == 'C0R190' :
      if target_data[i]['TEMP'] == '-99.000' or target_data[i]['TEMP'] == '-999.000' :
         TEMP_C0R190 = TEMP_C0R190
      else :
         if float(target_data[i]['TEMP']) > TEMP_C0R190:
            TEMP_C0R190 = float(target_data[i]['TEMP'])
   elif target_data[i]['station_id'] == 'C0X260' :
      if target_data[i]['TEMP'] == '-99.000' or target_data[i]['TEMP'] == '-999.000' :
         TEMP_C0X260 = TEMP_C0X260
      else :
         if float(target_data[i]['TEMP']) > TEMP_C0X260:
            TEMP_C0X260 = float(target_data[i]['TEMP'])
            
if TEMP_C0A880 == 0 :
   val_C0A880 = str(None)
else :
   val_C0A880 = TEMP_C0A880
if TEMP_C0F9A0 == 0 :
   val_C0F9A0 = str(None)
else :
   val_C0F9A0 = TEMP_C0F9A0
if TEMP_C0G640 == 0 :
   val_C0G640 = str(None)
else :
   val_C0G640 = TEMP_C0G640
if TEMP_C0R190 == 0 :
   val_C0R190 = str(None)
else :
   val_C0R190 = TEMP_C0R190
if TEMP_C0X260 == 0 :
   val_C0X260 = str(None)
else :
   val_C0X260 = TEMP_C0X260


print("[['C0A880',", val_C0A880, "],", "['C0F9A0',", val_C0F9A0, "],", "['C0G640',", val_C0G640, "],", "['C0R190',", val_C0R190, "],", "['C0X260',", val_C0X260,"]]")
