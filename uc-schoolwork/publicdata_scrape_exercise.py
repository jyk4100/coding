# run script with county as well as year range and true and false (string)
# true or false whether to plot republican or democratic share

# test cases (plot attached)
# python e4_args.py "essex county" 1924 2012 true
# python e4_args.py "fairfax county" 1924 2008 false

import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("start_y") # how to defind as int?
parser.add_argument("end_y")
parser.add_argument("repub") # boolean?
args = parser.parse_args()

# option ot plot Democratic or Republican share
# intended
# print(int(bool(args.repub))) # 1
# turns out bool("false") => T and bool("") => F
# python e4_args.py "fairfax county" 1924 2008 ""
# which is kinda akward... so... length base

index_plot = 5 - len(args.repub)
plot_title_list = [" Democratic Share", " Republican Share"]
plot_y_list = ["demo share","repub share"]


# below not necessary in part 2 id_year and id_num already in memory from part 1
# only for testing program executions with options without having to download everything
# comment block part 1 and part 2 for such reason
# call id numbers and years
id_year = []
id_num = []
for line in open("ELECTION_ID"):
    id_year.append(int(line[0:4]))
    id_num.append(int(line[5:10]))
    pass

# # again comment block to prevent download everything
# # ---------------------------- part 1 --------------------------------------------------------------- #
# # function to get election id numbers and years
# def get_id():
#     id_num = []
#     id_year = []
#
#     link_id = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
#     resp = requests.get(link_id)
#     soup = BeautifulSoup(resp.content , "html.parser")
#     tags_id = soup.find_all(attrs={'id': re.compile("election-id")})
#
#     for i in range(len(tags_id)):
#         id_num.append(int(tags_id[i]["id"][12:17]))
#         id_year.append(int(tags_id[i].contents[1].string))
#         pass
#
#     return id_num, id_year
#
# # save election id and years to "ELECTION_ID" file
# id_num, id_year = get_id()
#
# with open("ELECTION_ID", "w") as out:
#     for x in zip(id_num, id_year):
#         out.write("{} {}\n".format(x[1], x[0]))

# # again comment block to prevent download everything
# # ---------------------------- part 2 --------------------------------------------------------------- #
#
# # function to make url
# def get_url(year):
#     url = "http://historical.elections.virginia.gov/elections/download/" + str(id_num[id_year.index(year)]) + "/precincts_include:0/"
#     return(url)
#
# # loop over and request to download csv files
# for year in id_year:
#     resp = requests.get(get_url(year))
#     file_name = "VA_pred_" + str(year) +".csv"
#     with open(file_name, "w") as out: out.write(resp.text)
#     pass

# ---------------------------- part 3 --------------------------------------------------------------- #

# function to clean pandas dataframe
def clean_csv(df, year):
    header = df.dropna(axis = 1)
    d = header.iloc[0].to_dict()
    d['County/City'] = 'County' # add to dictionary
    df = df[1:] # drop 1st row
    df = df.drop(df.columns[[1, 2]], axis=1)  #  drop 1st and 2nd column
    df.rename(inplace = True, columns = d)  # rename to democrat/republican
    df = df[df["County"] != "TOTALS"]
    df["Year"] = year
    return(df)

# function to get saved csv file as pandas dataframe
def get_csv_saved(year):
    file_name = "VA_pred_" + str(year) +".csv"
    df = pd.read_csv(file_name, thousands = ",")
    df = clean_csv(df, year)
    return(df)

# function to merge data frame within given year range
def merge_years(start_year=1924, end_year=2012):
    cols = ['County', 'Democratic', 'Republican','Total Votes Cast','Year']
    # justin case want Democratic as well
    df_rbind = pd.DataFrame(columns=cols, dtype='int') # int type !?!?!
    years = [x for x in id_year if x>=start_year and x<=end_year]
    # merge over years
    for year in years:
        df_rbind = df_rbind.append(get_csv_saved(year)[cols])
        pass
    # convert to integer
    df_rbind['Republican'] = df_rbind['Republican'].str.replace(",","").astype(int)
    df_rbind['Democratic'] = df_rbind['Democratic'].str.replace(",","").astype(int)
    return(df_rbind)

# function to get dataframe at county level
def get_county(df_rbind, county_name):
    # dx_county = df_rbind["County"].str.contains("(?i)county_name|recess") # regex for ignore case # nope not working
    idx_county = df_rbind["County"].str.contains(county_name, case=False) # ignore case
    df_county = df_rbind[idx_county].sort_values(by="Year").copy()  # need to make copy for column division
    df_county.index = list(range(1,len(df_county)+1)) # reset index
    df_county['repub share'] = df_county['Republican']/df_county['Total Votes Cast']
    df_county['demo share'] = df_county['Democratic']/df_county['Total Votes Cast']
    return(df_county)

# function to plot
def get_plot(df_county, plot_y):

    p = df_county.plot(x = "Year", y = plot_y, linestyle="dashed", color="blue")

    patch, label = p.get_legend_handles_labels()
    p.set_ylim(0.1, 0.8)

    # title
    title_text = df_county["County"][1] + plot_title_list[index_plot]
    plt.title(title_text, y=1.00, fontsize = 13)

    # year range
    year_beg = int(list(df_county["Year"])[0])
    year_end= int(list(df_county["Year"])[len(df_county["Year"])-1])

    # x ticks
    plt.xticks(range(year_beg,year_end+1,8))

    # legends
    legend_text = str(year_beg) + " - " + str(year_end)
    labels = [legend_text]
    leg = p.legend(patch, labels, loc=1, fontsize=10)
    leg.get_frame().set_linewidth(0.0) # no legend box boarder
    return(p)


# executions
df_rbind = merge_years(int(args.start_y), int(args.end_y))

df_county = get_county(df_rbind, args.name)

p = get_plot(df_county, plot_y_list[index_plot])

plot_name = args.name + plot_title_list[index_plot] + " from " + args.start_y + " to " + args.end_y

p.get_figure().savefig((plot_name+".png"), bbox_inches='tight')
