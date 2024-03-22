import numpy as np
import pandas as pd
import plotly.express as px
import datetime as dt
import warnings as w
w.filterwarnings('ignore')

fact_stamps_df = pd.read_csv('data/fact_stamps.csv')
fact_transport_df = pd.read_csv('data/fact_transport.csv')
fact_ts_ipass_df = pd.read_csv('data/fact_TS_iPASS.csv')
dim_date_df = pd.read_csv('data/dim_date.csv')
dim_districts_df = pd.read_csv('data/dim_districts.csv')

fact_stamps_df.month = pd.to_datetime(fact_stamps_df.month, format = '%Y-%m-%d') 
dim_date_df.month = pd.to_datetime(dim_date_df.month, format = '%Y-%m-%d') 
fact_transport_df.month = pd.to_datetime(fact_transport_df.month, format = '%Y-%m-%d')
fact_ts_ipass_df.month = pd.to_datetime(fact_ts_ipass_df.month, format = '%d-%m-%Y')

## Making full Stamps df:
stamps_semi_merged = fact_stamps_df.merge(dim_date_df, left_on = 'month',right_on = 'month')
stamps_merged = stamps_semi_merged.merge(dim_districts_df, left_on = 'dist_code', right_on = 'dist_code')

## Making full Transports df:
transports_semi_merged = fact_transport_df.merge(dim_date_df, left_on = 'month',right_on = 'month')
transports_merged = transports_semi_merged.merge(dim_districts_df, left_on = 'dist_code', right_on = 'dist_code')

## Making full Transports df:
tsipass_semi_merged = fact_ts_ipass_df.merge(dim_date_df, left_on = 'month',right_on = 'month')
tsipass_merged = tsipass_semi_merged.merge(dim_districts_df, left_on = 'dist_code', right_on = 'dist_code')
