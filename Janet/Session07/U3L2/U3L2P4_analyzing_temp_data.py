import weather_utils as wu

# Data set is already populated with Boston data

# Read dataset
content = wu.load_30_days()

# Pull out daily and hourly data
daily = wu.extract_daily_from_json(content)
hourly = wu.extract_hourly_from_json(content)   #SF# Why do you need hourly?

values = {
    'high_max': daily['temperatureMax'].max(),
    'low_max': daily['temperatureMax'].min(),
    'mean_max': daily['temperatureMax'].mean(),
    'median_max': daily['temperatureMax'].median(),
    'greatest_delta_max': daily['changeMax'].max(),
    'smallest_delta_max': daily['changeMax'].min(),

    'high_min': daily['temperatureMin'].max(),
    'low_min': daily['temperatureMin'].min(),
    'mean_min': daily['temperatureMin'].mean(),
    'median_min': daily['temperatureMin'].median(),
    'greatest_delta_min': daily['changeMin'].max(),
    'smallest_delta_min': daily['changeMin'].min(),
}
print "BOSTON WEATHER\n"
print "HIGHS\n" \
      "Highest high: {high_max}\n" \
      "Lowest high: {low_max}\n" \
      "Median high: {median_max}\n" \
      "Mean high: {mean_max}\n" \
      "Greatest change: {greatest_delta_max}\n" \
      "Smallest change: {smallest_delta_max}\n" \
      "\n" \
      "LOWS\n" \
      "Highest high: {high_min}\n" \
      "Lowest high: {low_min}\n" \
      "Median high: {median_min}\n" \
      "Mean high: {mean_min}\n" \
      "Greatest change: {greatest_delta_min}\n" \
      "Smallest change: {smallest_delta_min}\n".format(**values)

#SF# Also possible, name the keys directly what you want and then print the:
max_values = {
    'Highest Daily Maximum Temperature': daily['temperatureMax'].max(),
    'Lowest Daily Maximum Temperature': daily['temperatureMax'].min(),
    'Mean Daily Maximum Temperature': daily['temperatureMax'].mean(),
    'Median Daily Maximum Temperature': daily['temperatureMax'].median(),
    'Greatest Daily Maximum Temperature Change': daily['changeMax'].max(),
    'Smallest Daily Maximum Temperature Change': daily['changeMax'].min(),
    }
min_values = {
    'Highest Daily Minimum Temperature': daily['temperatureMax'].max(),
    'Lowest Daily Minimum Temperature': daily['temperatureMax'].min(),
    'Mean Daily Minimum Temperature': daily['temperatureMax'].mean(),
    'Median Daily Minimum Temperature': daily['temperatureMax'].median(),
    'Greatest Daily Minimum Temperature Change': daily['changeMax'].max(),
    'Smallest Daily Minumum Temperature Change': daily['changeMax'].min(),
    }

print "BOSTON WEATHER\n"
print "HIGHS"
for key in max_values.keys():
    print("\t{0:45s}: {1:.1f} [F]".format(key, max_values[key]))
print "LOWS"
for key in min_values.keys():
    print("\t{0:45s}: {1:.1f} [F]".format(key, min_values[key]))
