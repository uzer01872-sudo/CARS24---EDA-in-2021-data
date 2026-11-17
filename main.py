import pandas as pd
import matplotlib.pyplot as plt 
# THE LODEING DATA FOR THE ROW DATA AND APPLING  FOR DATFRAME function AND READ USING THAT READ csv FILE OPTION 
car_data = pd.read_csv ('CARS24.CSV')
df = pd.DataFrame(car_data)
print(df.to_string()) 
#decribe the head fuctions 
print(df.head(200).to_string()) 
# the code in which data cling option  option 
df['SELLING_PRICE'] = (
    df['SELLING_PRICE']
    .str.replace('₹', '', regex=True)
    .str.replace(',', '', regex=True)
    .str.replace('\xa0', '', regex=True)
    .str.strip()
    .astype(float)
)
print("..........total selling price average......")
print('Total Sum:', df['SELLING_PRICE'].sum())
print('Average Price:', df['SELLING_PRICE'].mean())
#THE SELLING PRICE IN WWHICH ACCODING TO transmission type 
print(df.groupby('Transmission _Type')['SELLING_PRICE'].agg(['mean', 'median', 'count']))
#THE CHECKING IN WHICH THE DATA FOR THE NULL VALUE  AND APLING FOR SUM() FUNCTION
print(df.isnull().sum())
# THIS IS THE check total full type 
print(df.FUEL_TYPE) 
df.head(200)
# POPULAR SELLING PRICE FULL TYPE AVERAGE RATE 
print(df.groupby('FUEL_TYPE')['SELLING_PRICE'].mean())
#SELLING PRICE AVERAGE RATE FOR TRANSIMAT ION TYPE 
print('.......SELLING PRICE AVERAGE RATE ACCODING TO TRANSIMATION TYPE......')
print(df.groupby('Transmission _Type')['SELLING_PRICE'].mean())
#THE AVERAGE SELLING PRICE FOR ACODING TO OWNER TYP
print("..THE AVERAGE SELLING PRICE FOR ACODING TO OWNER TYPE..")
print(df.groupby('CAR_NAME ')['SELLING_PRICE'].mean())
#THE AVERAGE SELLING PRICE FOR ACODING TO OWNER TYPE 
print("..THE AVERAGE SELLING PRICE FOR ACODING TO OWNER TYPE..")
print(df.groupby('OWNER_TYPE')['SELLING_PRICE'].mean())
   # ---------------------- FULE TYPE GRAPH -------------------------------
#avevarge fule selling price 
avg_price_by_fuel = df.groupby('FUEL_TYPE')['SELLING_PRICE'].mean()
#plotting the figure
plt.figure(figsize=(9, 5))
#bar chart 
avg_price_by_fuel.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'orange'])
#title and and lables option 
plt.xticks(rotation=0)
plt.title('Average Selling Price by Fuel Type', fontsize=14, fontweight='bold')
plt.xlabel('Fuel Type', fontsize=12)
plt.ylabel('Average Selling Price (₹)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
#grap display 
plt.show()
 # ---------------------- WONER TYPE GRAPH -------------------------------
avg_price_by_fuel = df.groupby('OWNER_TYPE')['SELLING_PRICE'].mean()
#plotting the figure
plt.figure(figsize=(9, 5))
#bar chart 
avg_price_by_fuel.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'orange'])
#title and and lables option 
plt.xticks(rotation=0)
plt.title('Average Selling Price by owner type ', fontsize=14, fontweight='bold')
plt.xlabel('owner type ', fontsize=12)
plt.ylabel('Average Selling Price (₹)', fontsize=12)
#
plt.grid(axis='y', linestyle='--', alpha=0.7) 
#grap display 
plt.show()
 # ---------------------- Transmission _Type GRAPH -------------------------------
avg_price_by_fuel = df.groupby('Transmission _Type')['SELLING_PRICE'].mean()
#plotting the figure
plt.figure(figsize=(9, 5))
#bar chart 
avg_price_by_fuel.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen', 'orange'])
#title and and lables option 
plt.xticks(rotation=0)
plt.title('Average Selling Price by Transmission _Type', fontsize=14, fontweight='bold')
plt.xlabel('Transmission _Type', fontsize=12)
plt.ylabel('Average Selling Price (₹)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7) 
#grap display 
plt.show()
 # ---------------------- CAR _Type GRAPH -------------------------------
# 1.remove the nan value for using dropna 
top_cars = df.dropna(subset=['CAR_NAME ', 'SELLING_PRICE']).head(15)
# 2. Plotting setup
plt.figure(figsize=(12, 6))
# 3. Bar chart plot karo
plt.bar(
    top_cars['CAR_NAME '].astype(str),
    top_cars['SELLING_PRICE'],
    color='cornflowerblue'
)
# 4. Title aur labels
plt.title('Selling Price of Cars (Car-wise Comparison)', fontsize=14, fontweight='bold')
plt.xlabel('Car Name', fontsize=12)
plt.ylabel('Selling Price (₹)', fontsize=12)
# 5. X-axis ke labels 
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()