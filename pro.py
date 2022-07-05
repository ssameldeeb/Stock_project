# imoprt modules
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# get the data
data = pd.read_csv("indexData.csv")


# get information about the data
print(data.shape)
print(data.dtypes)
print(data.isna().sum())
print(data.columns.values)
print(data.head())


# get information about the index_column
print(data["Index"].unique())
print(data["Index"].nunique())
print(data["Index"].value_counts())
# show countplot for Floors_num and save the image
plt.figure(figsize=(9,4))
sns.countplot(data["Index"])
plt.tight_layout()
plt.savefig('save/Index_value_counts.png')
plt.show()


# split Date column
data[["Year","Month","Day"]] = data["Date"].str.split("-",expand=True)
print(data.head())
print(data["Year"].value_counts())


# get x and y
x = data["Year"].value_counts().index
y = data["Year"].value_counts().values
# show pie and save it
plt.figure(figsize=(9,9))
plt.title("value_counts for Years")
colors = sns.color_palette('bright')[0:5]
plt.pie(y, labels = x, colors=colors, autopct='%.0f%%')
plt.tight_layout()
plt.savefig('save/pie_value_counts_for_Years.png')
plt.show()


# drop the null data from data
data = data.dropna()
print(data.isna().sum())
print(data.shape)


# drop columns are not import
data = data.drop(["Month","Day","Volume","Date","Adj Close"],axis=1)
print(data.head())


# show correlation and save it 
plt.figure(figsize=(9,4))
sns.heatmap(data.corr(), annot=True, cmap="Greens")
plt.tight_layout()
plt.savefig('save/heatmap_for_data.png')
plt.show()


# get describe for all this columns
Columns =["Open","High","Low","Close"]
for x in Columns:
    print(x.upper())
    print(data[x].describe().round(2))
    print("-"*100)



# create_columns
max_open_nya_all_year = []
min_open_nya_all_year = []

# get results among columns , show it and save it
for y in data["Year"].unique():
    print("Open")
    print("NYA")
    print(y) 
    print(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Open"].max())
    print(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Open"].min())
    max_open_nya_all_year.append(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Open"].max())
    min_open_nya_all_year.append(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Open"].min())
    print("-"*100)
    
print(len(max_open_nya_all_year))
print(len(min_open_nya_all_year))

plt.figure(figsize=(9,4))
plt.plot(max_open_nya_all_year, label="max_open_nya_all_year")
plt.legend()
plt.plot(min_open_nya_all_year, label="min_open_nya_all_year")
plt.legend()
plt.tight_layout()
plt.savefig('save/corr_between_max_and_min_in_open.png')
plt.show()



# create_columns
max_close_nya_all_year = []
min_close_nya_all_year = []

# get results among columns , show it and save it
for y in data["Year"].unique():
    print("Close")
    print("NYA")
    print(y) 
    print(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Close"].max())
    print(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Close"].min())
    max_close_nya_all_year.append(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Close"].max())
    min_close_nya_all_year.append(data[(data["Year"] == y)&(data["Index"] == "NYA")]["Close"].min())
    print("-"*100)
    
print(len(max_close_nya_all_year))
print(len(min_close_nya_all_year))

plt.figure(figsize=(9,4))
plt.plot(max_close_nya_all_year, label="max_close_nya_all_year")
plt.legend()
plt.plot(min_close_nya_all_year, label="min_close_nya_all_year")
plt.legend()
plt.tight_layout()
plt.savefig('save/corr_between_max_and_min_in_close.png')
plt.show()


    
# save the output csv file
out = pd.DataFrame({"max_open_nya_all_year":max_open_nya_all_year,"min_open_nya_all_year":min_open_nya_all_year,"max_close_nya_all_year":max_close_nya_all_year,"min_close_nya_all_year":min_close_nya_all_year})
out.to_csv("The_output.csv", index=False)



# function to show and save eny input
def show_corr(xx,yy):
    
    max = []
    min = []
    
    for y in data["Year"].unique():
        print(xx)
        print(yy)

        max.append(data[(data["Year"] == y)&(data["Index"] == xx)][yy].max())
        min.append(data[(data["Year"] == y)&(data["Index"] == xx)][yy].min())
        
    plt.figure(figsize=(9,4))
    plt.plot(max_close_nya_all_year, label="max")
    plt.legend()
    plt.plot(min_close_nya_all_year, label="min")
    plt.legend()
    plt.tight_layout()
    plt.savefig('save/corr_between_max_and_min_'+yy+'.png')
    plt.show()

# use the function
show_corr("IXIC","Close")