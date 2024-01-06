from hfpkg.src.calculations import calculate_sma, calculate_rsi
from hfpkg.src.files import read_csv, write_to_csv

#read data from CSV file
file_path = 'orcl.csv'
close_prices = read_csv(file_path)

#calculate 5-day SMA
sma_5day = calculate_sma(close_prices, value=5)   #default value is 5

#calculate 14-day RSI
rsi = calculate_rsi(close_prices, value=14)  #default value is 14

#write results to CSV files
write_to_csv(sma_5day, 'output_sma.csv')
write_to_csv(rsi, 'output_rsi.csv')