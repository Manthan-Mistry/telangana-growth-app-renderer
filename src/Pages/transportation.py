
import dash
from dash import dash_table
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import Input, Output, callback
from diverging_bars_final import data_bars_diverging_final

from data_processing import *
from insights import *

theme_colors = {
    '#feccd7': px.colors.sequential.RdPu[:5][::-1],
    '#C7E9C0': px.colors.sequential.Greens[:5][::-1],
    '#FDD0A2': px.colors.sequential.Oranges[:5][::-1],
    '#FCBBA1': px.colors.sequential.Reds[:5][::-1],
    '#C6DBEF': px.colors.sequential.Blues[:5][::-1],
}

dash.register_page(__name__, path = '/transportation', name = 'Transportation')


layout = dbc.Container([
    dbc.Row([ #===============================================>> Start of Page-2 Row 1.
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Col([
                        dbc.Label(['Select X axis:'],style = {'margin-top':'5px','margin-right':'5px',
                                                          'font-size':12,'font-weight':'bold'}),
                        dbc.RadioItems(
                                    id = 'radio-timeframe',
                                    class_name = 'radio-timeframe',
                                    options = [{'label': 'Year','value':'fiscal_year'},
                                               {'label': 'Month','value':'Mmm'},
                                               {'label': 'Qtr','value':'quarter'}],
                                    value = 'Mmm',
                                    inline = True,
                                    style = {'display':'flex','height':'30px',
                                             'margin-top':'5px',
                                             'font-size':12,'font-weight':'bold',
                                             'font-family':'Arial'
                                             })
                            ], width = 5, style = {'display':'flex'}),

                    dbc.Col([ 
                        dbc.Label(['Fuel_type:'],style = {'margin-top':'5px','margin-right':'5px',
                                                     'font-size':12,'font-weight':'bold'}),
                        dbc.RadioItems(
                                    id = 'radio-fueltype',
                                    options = [{'label': 'Petrol','value':'Petrol'},
                                               {'label': 'Diesel','value':'Diesel'},
                                               {'label': 'Electric','value':'Electric'}],
                                    value = 'Petrol',
                                    inline = True,
                                    style = {'display':'flex',
                                             'margin-top':'5px','height':'30px',
                                             'font-size':12,'font-weight':'bold'
                                            }) 
                            ], width = 6, style = {'display':'flex'}),
                    dbc.Col([
                        dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'info-fuel-type-line'),
                            color = 'none', outline = True,size = 'md',class_name = 'insight-btn')
                            ],width = 1,
                            style = {'margin-left':'70px','margin-top':'-5px'}),
                    
                    dbc.Tooltip( dcc.Markdown(graph_5_insignt),
                                target = 'info-fuel-type-line', placement = 'left')

                ],id = 'card-header-5',  class_name = 'header'),
                dbc.CardBody([
                    dcc.Graph(id='fuel-type-line',config = {'displayModeBar':False})
                            ], style = {'width':'100%','border-radius':'0 0 5px 5px'}),

                    ],style = {'border':'2px solid black'}, color = "dark", outline = True)
                ], width = 12, style = {'height':'100%'})
            ], style = {'display': 'flex','justiftContent':'around','margin-bottom':'20px'}),
        
    dbc.Row([ #====================================================================>> Start of Page-2 Row 2
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Col([
                        dbc.RadioItems(
                                        id = 'radio-vehtype',
                                        options = [{'label': 'MotorCar','value':'MotorCar'},
                                                   {'label': 'MotorCycle','value':'MotorCycle'},
                                                   {'label': 'AutoRickshaw','value':'AutoRickshaw'},
                                                   {'label': 'Agriculture','value':'Agriculture'}],
                                        value = 'MotorCar',
                                        inline = True,
                                        style = {'height':'30px','font-size':12,
                                                 'font-weight':'bold','font-family':'Arial',
                                                 'margin-top':'5px'
                                         }),
                            ], style = {'position':'relative'}),
                        
                        ],id = 'card-header-6',  class_name = 'header'),
                    dbc.CardBody([
                        dcc.Graph(id = 'vehtype-bar',config = {'displayModeBar':False}),
                                 ],style = {'border-radius':'0 0 5px 5px','height':'265px'}
                                ),
                         ],style = {'width': '100%','border':'2px solid black'},color = "dark", outline = True)
                ],width = 12, md = 7),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                        dbc.Col([
                            dbc.Label('Select Fuel_type: ',style = {'margin-right':'5px','margin-top':'10px'}),
                            dcc.Dropdown(
                                id='col-selector',
                                options=[
                                        {'label': 'Petrol (▲%)', 'value': 'Petrol_pct_diff'},
                                        {'label': 'Diesel (▲%)', 'value': 'Diesel_pct_diff'},
                                        {'label': 'Electric (▲%)', 'value': 'Electric_pct_diff'}
                                        ],
                                value = 'Petrol_pct_diff',
                                clearable = False,
                                style = {'width':'120px','font-size': 12,'fontWeight':'bold','margin-bottom':'5px'}
                                        )
                        ],width = 11, style = {'margin-top':'-4px','display':'flex'}),
                    
                    dbc.Col([
                        dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'datatable-fueltype'),
                            color = 'none', outline = True,size = 'md')
                            ],
                            style = {'margin-top':'-5px'}),
                    
                    dbc.Tooltip( dcc.Markdown(graph_7_insignt),
                                target = 'datatable-fueltype', placement = 'left')

                                ],id = 'card-header-7',  class_name = 'header'),
        
        dbc.CardBody([
            dbc.Col([
                dash_table.DataTable(
                                    id='datatable',columns = [],sort_action = 'native',
                                    style_cell = {'minWidth':'20','maxWidth':'100','fontSize':'12px'},
                                    style_header = {'textAlign':'center','fontWeight':'bold','background-color':'#f3f3f3'},
                                    page_size = 5,
                                    )
                    ], style = {'width':'100%','height':'235px'}),
                     ],style = {'border-radius':'0 0 5px 5px'}),
                ], style = {'width':'100%','border':'2px solid black'},color = "dark", outline = True)
        ], width = 12, md = 5, style = {'height':'100%'})
 
                
           ], style = {'display':'flex','justiftContent':'around','margin-bottom':'20px'})
], fluid = True)


# # -------------------------------  Page-2 fuel-type-line   -------------------------------

@callback(   
     Output('fuel-type-line', 'figure'),
     Input('year-selector-main', 'value'), ## Timeline,
     Input('radio-timeframe','value'), 
     Input('radio-fueltype','value'),
     Input('theme-selector-main', 'value')
)

def update_fuel_type_line_data(year_val,time_frame,fuel_type,theme_color): ## Removed year_val:
    
    if time_frame == 'Mmm':
        main_df = transports_merged[(transports_merged['fiscal_year']>= year_val[0])\
                                    &(transports_merged['fiscal_year']<= year_val[1])]\
                  .groupby([time_frame], as_index = False)\
                  .sum()[[ time_frame, 'fuel_type_petrol','fuel_type_diesel','fuel_type_electric']]

        main_df['month_num'] = pd.to_datetime(main_df['Mmm'], format = '%b').dt.month
        main_df['sort_order'] = np.where(main_df.month_num > 3,main_df.month_num - 3,main_df.month_num + 9)
        main_df.sort_values(['sort_order'], inplace = True)

    
    else:
         main_df = transports_merged[(transports_merged['fiscal_year']>= 2019)\
                                     & (transports_merged['fiscal_year']<= 2022)]\
                  .groupby([time_frame], as_index = False)\
                  .sum()[['fuel_type_petrol',time_frame,'fuel_type_diesel','fuel_type_electric']]
            
    columns = {'fuel_type_petrol': 'Petrol', 'fuel_type_diesel' : 'Diesel', 'fuel_type_electric' : 'Electric'} 
    main_df.rename(columns = columns, inplace = True )

    line = px.line(main_df,
                   x = time_frame, #^^
                   y = fuel_type,  #--->**  [Petrol,'Diesel','Electric'] ==> radioitems(fuel_type):
                   text = [f'{i}' for i in main_df[fuel_type].transform(lambda x:'{:,.4}k '.format(x/10**3))], #**
                   height = 285,
#                    width = 910,
                   custom_data = ['Petrol','Diesel','Electric'],
#                    hover_name = None, 
                   color_discrete_sequence = theme_colors[theme_color],
                   template = 'simple_white')
    
    hovertemplate = '<br>Petrol: <b>%{customdata[0]:,.0f}</b><br>' +\
        '<br>Diesel: <b>%{customdata[1]:,.0f}</b><br>' +\
        '<br>Electric: <b>%{customdata[2]:,.0f}</b><br>'

    line.update_xaxes(type = 'category', title = '')
    line.update_yaxes(visible = False)
    line.update_layout(hovermode = 'x unified',
                       hoverlabel = dict(font_size = 12),
                       xaxis = dict(showgrid = True),font = dict(size = 10),
                       margin = dict(l = 30, r = 0,t = 10,b = 0),
                       plot_bgcolor = 'rgba(0,0,0,0)'
                       )
    line.update_traces(textposition = 'bottom right', hovertemplate = hovertemplate)
    return(line)

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '910px',  # Set a maximum width for the chart
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

# -------------------------------  Vehicletype/districts-bar   -------------------------------

@callback(   
     Output('vehtype-bar', 'figure'),
     Input('year-selector-main', 'value'),
     Input('radio-vehtype','value'),
     Input('theme-selector-main', 'value')
)

## final version:
def update_veh_type_bar_data(year_val,veh_type,theme_color):
    
    pre_df = fact_transport_df.merge(dim_date_df,how = 'right',left_on = 'month',right_on = 'month')\
                              .merge(dim_districts_df,left_on = 'dist_code',right_on = 'dist_code')
    if len(year_val)>1:
        filtered_temp_2_df = pre_df[(pre_df['fiscal_year']>= year_val[0]) & (pre_df['fiscal_year']<= year_val[1])] 
    
    else:
        filtered_temp_2_df = pre_df[pre_df['fiscal_year']==(year_val[0])] # temp_2_df replaced

    columns = {'vehicleClass_MotorCar': 'MotorCar',
               'vehicleClass_MotorCycle' : 'MotorCycle',
               'vehicleClass_AutoRickshaw' : 'AutoRickshaw',
               'vehicleClass_Agriculture' : 'Agriculture'
              } 
    filtered_temp_2_df.rename(columns = columns, inplace = True )

    df = filtered_temp_2_df.groupby(['district'], as_index = False)\
                                       .sum()\
                                       .sort_values([veh_type], ascending = False)\
                                       [['district','MotorCar','MotorCycle','AutoRickshaw','Agriculture']][:5]

    veh_type_bar = px.bar(data_frame = df,
                          y = df['district'],
                          x = df[veh_type],
                          text = [f'{i}' for i in df[veh_type].transform(lambda x:'{:,.4}k '.format(x/10**3))],
                          color_discrete_sequence = theme_colors[theme_color],
#                           width = 440,
                          height = 240,
                          orientation = 'h',
                          template = 'simple_white')

    veh_type_bar.update_yaxes(title = '')
    veh_type_bar.update_xaxes(visible = False)
    veh_type_bar.update_layout(margin = dict(l = 0, r = 0,t = 10,b = 10),
                               yaxis = dict(autorange ='reversed', tickfont = dict(size = 10)),
                               plot_bgcolor = 'rgba(0,0,0,0)',## Making background transparent:
                               paper_bgcolor = 'rgba(0,0,0,0)'
                              )
    
    veh_type_bar.update_traces(width = 0.8,textposition = 'auto')## Individual bar width
    return(veh_type_bar)

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '440px',  # Set a maximum width for the chart
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

# -------------------------------  fuel_type_data-table   -------------------------------

@callback(
    Output('datatable', 'data'),
    Output('datatable','columns'),
    # Input('year-selector-main', 'value'),
    Input('col-selector', 'value'),
)
    

def feul_type_datatable(selected_col):
    temp_2_df = fact_transport_df.merge(dim_date_df,how = 'right',left_on = 'month',right_on = 'month')\
                             .merge(dim_districts_df,left_on = 'dist_code',right_on = 'dist_code')\
                             [['fiscal_year','district','fuel_type_petrol','fuel_type_diesel','fuel_type_electric']]

    columns = {'fuel_type_petrol': 'Petrol', 'fuel_type_diesel' : 'Diesel', 'fuel_type_electric' : 'Electric'} 
    temp_2_df.rename(columns = columns, inplace = True )

    transp_start_df = temp_2_df[(temp_2_df['fiscal_year'] == 2019)]## Year start
    vehicle_sale_start = transp_start_df.groupby(['district'], as_index = False).sum() 
    
    transp_end_df = temp_2_df[(temp_2_df['fiscal_year'] == 2022)]## Year start
    vehicle_sale_end = transp_end_df.groupby(['district'], as_index = False).sum()

    merged_df = vehicle_sale_start.merge(vehicle_sale_end, left_on = 'district', right_on = 'district',suffixes = ['_21',"_22"])

    merged_df['petrol_diff'] = merged_df['Petrol_22'] - merged_df['Petrol_21']
    merged_df['Petrol_pct_diff'] = round(merged_df['petrol_diff'] / merged_df['Petrol_21']*100,2)

    merged_df['diesel_diff'] = merged_df['Diesel_22'] - merged_df['Diesel_21']
    merged_df['Diesel_pct_diff'] = round(merged_df['diesel_diff'] / merged_df['Diesel_21']*100,2)

    merged_df['electric_diff'] = merged_df['Electric_22'] - merged_df['Electric_21']
    merged_df['Electric_pct_diff'] = round(merged_df['electric_diff'] / merged_df['Electric_21']*100,2) 
    
    filtered_df = merged_df[['district',selected_col]]
    
    columns = [{'name':'District','id': 'district'},
               {'name':selected_col, 'id':selected_col, 'type':'numeric'}]
#            'format': dash_table.FormatTemplate.percentage(2)} ## can use to format values as pct but then databars won't work.
              
               
    return filtered_df.to_dict('records'),columns

@callback(
    Output('datatable', 'style_data_conditional'),
    # Input('year-selector-main', 'value'),
    Input('col-selector', 'value'),
#     Input('theme-selector-main', 'value')
)
def update_data_bars(selected_col):
    temp_2_df = fact_transport_df.merge(dim_date_df,how = 'right',left_on = 'month',right_on = 'month')\
                                 .merge(dim_districts_df,left_on = 'dist_code',right_on = 'dist_code')\
                                 [['fiscal_year','district','fuel_type_petrol','fuel_type_diesel','fuel_type_electric']]

    columns = {'fuel_type_petrol': 'Petrol', 'fuel_type_diesel' : 'Diesel', 'fuel_type_electric' : 'Electric'} 
    temp_2_df.rename(columns = columns, inplace = True )

    transp_start_df = temp_2_df[(temp_2_df['fiscal_year'] == 2019)]## Year start
    vehicle_sale_start = transp_start_df.groupby(['district'], as_index = False).sum() 
    
    transp_end_df = temp_2_df[(temp_2_df['fiscal_year'] == 2022)]## Year start
    vehicle_sale_end = transp_end_df.groupby(['district'], as_index = False).sum()

    merged_df = vehicle_sale_start.merge(vehicle_sale_end, left_on = 'district', right_on = 'district',suffixes = ['_21',"_22"])

    merged_df['petrol_diff'] = merged_df['Petrol_22'] - merged_df['Petrol_21']
    merged_df['Petrol_pct_diff'] = round(merged_df['petrol_diff'] / merged_df['Petrol_21']*100,2)

    merged_df['diesel_diff'] = merged_df['Diesel_22'] - merged_df['Diesel_21']
    merged_df['Diesel_pct_diff'] = round(merged_df['diesel_diff'] / merged_df['Diesel_21']*100,2)

    merged_df['electric_diff'] = merged_df['Electric_22'] - merged_df['Electric_21']
    merged_df['Electric_pct_diff'] = round(merged_df['electric_diff'] / merged_df['Electric_21']*100,2)
    filtered_df = merged_df[['district',selected_col]]
    
    if selected_col == 'Petrol_pct_diff':
        styles = data_bars_diverging_final(filtered_df, 'Petrol_pct_diff')
        
    elif selected_col == 'Diesel_pct_diff':
        styles = data_bars_diverging_final(filtered_df, 'Diesel_pct_diff')
        
    else :
        styles = data_bars_diverging_final(filtered_df, 'Electric_pct_diff')
    return styles

@callback(
    Output('card-header-5','style'),
    Output('card-header-6','style'),
    Output('card-header-7','style'),
    Input('theme-selector-main','value'),
)

def update_color(color):
    card_header_style = {'background-color':color,'font-size':12,'font-weight':'bold',
                         'font-family':'Arial','display':'flex','border-radius':'5px 5px 0px 0px','height':'45px'}
    return card_header_style,card_header_style,card_header_style

