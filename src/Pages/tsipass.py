
import dash
from dash import dash_table
from dash import dcc
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import Input, Output, callback
from databars_from_zero_custom_color import data_bars

from data_processing import *
from insights import *

theme_colors = {
    '#feccd7': px.colors.sequential.RdPu[:5][::-1],
    '#C7E9C0': px.colors.sequential.Greens[:5][::-1],
    '#FDD0A2': px.colors.sequential.Oranges[:5][::-1],
    '#FCBBA1': px.colors.sequential.Reds[:5][::-1],
    '#C6DBEF': px.colors.sequential.Blues[:5][::-1],
}

def shorten_sector_name(sector):
        if isinstance(sector, str) and len(sector) > 25 and sector.split()[0] != sector.split()[2]:
            return sector.split()[0].strip(',') + ' ' + sector.split()[1]
        else:
            return sector

dash.register_page(__name__, path = '/tsipass', name = 'Ts-iPASS')


layout =   dbc.Container([
    dbc.Row([                 #=====================================================================>> Page 3 Row 1
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Label(['X axis:'],style = {'margin-top':'5px','margin-right':'5px'}),
                        dbc.Col([
                            dcc.Dropdown(
                                id='timeframe-dropdown',
                                options=[
                                        {'label': 'Fiscal Year', 'value': 'fiscal_year'},
                                        {'label': 'Month', 'value': 'Mmm'},
                                        {'label': 'Qtr', 'value': 'quarter'}
                                        ],
                                value='Mmm',
                                clearable = False,
                                style = {'width':'150px','font-size': 12,'margin-bottom':'5px'}
                                        )
                                ],width = 5, style = {'margin-top':'-4px'}),

                        dbc.Col([
                            dbc.Label('Sector: ', style = {'margin-right':'5px','margin-top':'10px'}),
                                dcc.Dropdown(
                                    id='sector-dropdown-inv',
                                    options=[
                                            {'label': x , 'value': x } for x in tsipass_merged['sector'].sort_values().unique()],
                                    value = 'Engineering',
                                    clearable = False,
                                    style = {'width':'200px','font-size': 12,'margin-bottom':'5px'}
                                            )
                            ],width = 5, style = {'margin-top':'-5px','display':'flex'})
                        ],id = 'card-header-8',  class_name = 'header'),
            dbc.CardBody([
                dcc.Graph(id='investment-line',config = {'displayModeBar':False}),
                        ], style = {'width':'100%','margin':'none'})
                
                ],style = {'width':'100%','border':'2px solid black'},color = "dark", outline = True)
    ],width = 12,md = 8,style = {'height':'100%'}),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                        dbc.Col([
                            dbc.Label(['Investments by:'],style = {'margin-top':'10px','margin-right':'5px'}),
                            dcc.Dropdown(
                                id='measure-dropdown',
                                options=[
                                        {'label': 'District', 'value': 'district'},
                                        {'label': 'Sector', 'value': 'sector'},
                                        ],
                                clearable = False,
                                persistence_type = 'session',
                                value='district',
                                style = {'font-size': 12,'width':'100px',
                                         'fontWeight':'bold','margin-bottom':'5px'}
                                        )
                                ], width = 10,style = {'margin-top':'-4px','display':'flex'}),
                    dbc.Col([
                        dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'invst-dist-sec-pie'),
                            color = 'none', outline = True,size = 'md',class_name = 'insight-btn')
                            ],
                            width = 1,
                            style = {'margin-top':'-5px','margin-left':'30px'}),
                    
                    dbc.Tooltip( dcc.Markdown(graph_9_insignt),
                                target = 'invst-dist-sec-pie', placement = 'left')


                            ],id = 'card-header-9',  class_name = 'header'),
    dbc.CardBody([
        dcc.Graph(id='measure-pie',config = {'displayModeBar':False}),
                ], style = {'width':'100%','border-radius':'0 0 5px 5px',
                            'padding-top':'0px'  ## Do not remove this row!!!
                            })
                     ],color = "dark", outline = True, style = {'width':'100%','border':'2px solid black'})
        ],width = 12,md = 4, style = {'height':'100%'})
        
    ], style = {'display':'flex','justiftContent':'around','margin-bottom':'20px'}), ##Page-3 Row-1 End
    
    dbc.Row([  #=========================================================>> Page 3 Row 2:
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Col([
                        dbc.Label(['Sector wise Investments in Cr.'], style = {'margin-top':'10px'}),
                        dbc.Label(['District:'],style = {'margin-right':'5px','margin-top':'10px','margin-left':'20px'}),
                            dcc.Dropdown(
                                id = 'dist-selector-6',
                                options=[{'label': x , 'value': x } for x in tsipass_merged['district'].sort_values().unique()],
                                value = 'Rangareddy',
                                clearable=False,
                                style={'width': '120px', 'font-size': 12, 'fontWeight': 'bold',
                                       'margin-bottom': '5px'}
                            ),
                        
                    ], width = 9, style = {'display':'flex','margin-top':'-5px'}),
                    
                    dbc.Col([
                        dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'dist-invts-by-sec'),
                            color = 'none', outline = True,size = 'md',class_name = 'insight-btn')
                            ],
                            width = 1,
                            style = {'margin-top':'-5px','margin-left':'115px'}),
                    
                    dbc.Tooltip( dcc.Markdown(graph_10_insignt),
                                target = 'dist-invts-by-sec', placement = 'bottom')
                ],id = 'card-header-10',  class_name = 'header'),

                    dbc.CardBody([
                        dbc.Col([
                            dcc.Graph('invst-bar',config = {'displayModeBar':False})
                        ], style={'width': '100%'})
                ], style={ 'border-radius': '0 0 5px 5px',
                      'padding': '10px','width':'100%'})
        ],color = "dark", outline = True, style={'height': '100%','border':'2px solid black'})
  ],style = {'width':'100%'}),
    dbc.Col([
        dbc.Card([
            dbc.CardHeader([
                dbc.Col([
                    dbc.Label(['#Districts Invested by sectors'], style = {'margin-top':'10px'}),
                    dbc.Label(['Select Top N:'], style = {'margin-top':'10px','margin-right':'5px','margin-left':'80px'}),
                        dbc.Col([
                            dcc.Dropdown(
                                id='select-top-n',
                                options=[
                                    {'label': '5', 'value': 5},
                                    {'label': '10', 'value': 10},
                                    {'label': 'All', 'value': 20}
                                ],
                                value=5,
                                clearable=False,
                                style={'width': '50px', 'font-size': 12, 'fontWeight': 'bold', 'margin-bottom': '5px',
                                       'margim-top':'-4px'}
                            ),
                        ]),
                
                ], width = 10, style = {'display':'flex','margin-top':'-4px'}),
                
                dbc.Col(dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'info-rel-dist'),
                            color = 'none', outline = True,size = 'md',class_name = 'insight-btn'), width = 1,
                            style = {'margin-left':'65px','margin-top':'-5px'}),
                    
                    dbc.Tooltip(dcc.Markdown(graph_11_insignt),
                                target = 'info-rel-dist', placement = 'left')

            ],id = 'card-header-11',  class_name = 'header'),

            dbc.Col([
                dbc.CardBody([
                    dash_table.DataTable(
                        id='invest_related_dist',
                        columns=[
                            {'name': 'Sector', 'id': 'sector'},
                            {'name': '#District', 'id': 'district'},
                            {'name': 'Investment(Cr)', 'id': 'investment in cr'},
                            {'name': 'Year', 'id': 'fiscal_year'}
                        ],
                        sort_action = 'native',
                        page_size = 5,  ## page_size param inside callback funct is addressed here
                        style_header = {'textAlign': 'center','fontWeight':'bold','background-color':'#f3f3f3'},
                        style_cell = {'fontSize':'12px'},
                        style_table = {'height':'185px','overflowY':'scroll'},
                        style_data_conditional=[
                            {
                                'if': {'row_index': 'odd'},
                                'height': 'auto','width':'auto'
                            },
                            {
                                'if': {'row_index': 'even'},
                                'height': 'auto','width':'auto'
                            } 
                        ]
                    )
                ], style={'padding-left':'5px',
                          'height':'100%','width':'100%',
                          'margin-left':'5px'})


            ], style={'border-radius': '0 0 5px 5px','height': '100%'})
        ],color = "dark", outline = True, style={'height':'100%','border':'2px solid black'})
        
],style = {'height':'100%','width':'100%'})
        
    ],style = {'display':'flex','justiftContent':'around','margin-bottom':'20px'})

], fluid  = True)


# # -------------------------------  Investment-line   -------------------------------

@callback(
    Output('investment-line', 'figure'),
    Input('timeframe-dropdown', 'value'),
    Input('year-selector-main','value'),
    Input('sector-dropdown-inv','value'),
    Input('theme-selector-main', 'value')
)
    
    

def investment_overtime(time_frame,year_range,sector,theme_color):
    
        
    if time_frame == 'fiscal_year':
        needed_df = tsipass_merged[(tsipass_merged['fiscal_year'] >= year_range[0])\
                                   & (tsipass_merged['fiscal_year'] <= year_range[1])\
                                   & (tsipass_merged['sector'] == sector)]\
                                      .groupby( time_frame, as_index = False)\
                                      .sum()[[time_frame,'investment in cr']]
    else:
        needed_df = tsipass_merged[(tsipass_merged['fiscal_year'] >= year_range[0])\
                                   & (tsipass_merged['fiscal_year'] <= year_range[1])\
                                   & (tsipass_merged['sector'] == sector)]\
                                      .groupby([time_frame], as_index = False)\
                                      .sum()[[time_frame,'investment in cr']]
        
    needed_df['investment in cr'] = round(needed_df['investment in cr'],1)
    line = px.line(needed_df,
               x = time_frame, 
               y = 'investment in cr',  
               text = 'investment in cr',
               height = 240,
#                width = 590,
               labels = {'Investment(Cr)':'investment in cr'},
               color_discrete_sequence = theme_colors[theme_color],
               markers = True,
               template = 'simple_white')
    
    hovertemplate = '<br>Investment: <b>%{y:,.2f} Cr</b><br>'
#     hovertemplate = 'District:%{label}<br>Investment: %{value:.2f} Bn<br>'
    
    line.update_xaxes(type = 'category', title = '')
    line.update_yaxes(visible = False)
    
    line.update_layout(hovermode = 'x unified',
                       xaxis = dict(showgrid = True),
                       font = dict(size = 10),
                       hoverlabel = dict(font_size = 12),
                       margin = dict(l = 0, r = 0,t = 0,b = 0),
                       plot_bgcolor = 'rgba(0,0,0,0)'
                       )
    line.update_traces(textposition = 'bottom right', hovertemplate = hovertemplate)
    return (line)

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '590px',  # Set a maximum width for the chart
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

# -------------------------------  inv/sec-pie   -------------------------------

@callback(
          Output('measure-pie', 'figure'),
          Input('measure-dropdown', 'value'),
          Input('year-selector-main','value'),
          Input('theme-selector-main', 'value')

         )

def update_pie_invested(measure, year_range,theme_color): ## year_val == 'value' from the input(year-seleector) dropdown and same for month value.
    df = tsipass_merged[(tsipass_merged['fiscal_year'] >= year_range[0])\
                        & (tsipass_merged['fiscal_year'] <= year_range[1]) ]\
                        .groupby(by = measure, as_index = False).sum()\
                        .sort_values(by = ['investment in cr'], ascending = False)[:5]
    df['investment in cr'] = round(df['investment in cr'],0)
                        
    
    if measure == 'district':
        pie = px.pie(data_frame = df,
                     names = 'district',
                     values = 'investment in cr',
                     hole = 0.75,
                     height = 256,
#                      width = 280,
                     labels = {'district':'District','investment in cr':'Investment'},
                     color_discrete_sequence = theme_colors[theme_color], ## List of colors of your choice:
                    )
        hovertemplate = '<b>District:</b> %{label}<br><b>Investment:</b> %{value:,.0f} Bn<br>'
        x,y = 0.75,0.5
       
    else:
        pie = px.pie(data_frame = df,
                     names = df['sector'].apply(lambda x: shorten_sector_name(x).replace('and','').replace(',Industrial','')),
                     values = 'investment in cr',
                     hole = 0.75,
                     height = 256,
#                      width = 280,
                     labels = {'sector':'Sector','investment in cr':'Investment'},
                     color_discrete_sequence = theme_colors[theme_color],
                    )
        hovertemplate = '<b>Sector:</b> %{label}<br><b>Investment:</b> %{value:,.0f} Bn<br>'
        x,y = 0.75,0.5
        
    pie.update_layout( 
                      margin = dict(l = 0, r = 0,t = 0,b = 0),
                      font_size = 10,
                      hoverlabel = dict(bgcolor = 'white',bordercolor = 'black'),
                      legend = dict(visible = True, bgcolor = 'rgba(0,0,0,0)',
                                    xanchor = 'right', yanchor = 'middle',
                                    x = x, y = y,font = dict(size = 9, color = 'black')),
                      plot_bgcolor = 'rgba(0,0,0,0)',paper_bgcolor = 'rgba(0,0,0,0)'
                     )
    
    pie.update_traces(textposition = 'outside',
                      textinfo = 'percent',
                      direction = 'clockwise',
                      hovertemplate = hovertemplate,
                      marker = dict(line = dict(color = 'black',width = 1)))
    return (pie)

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '290px',  # Set a maximum width for the chart
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

# # -------------------------------  inv(sector)-bar-by-dist   -------------------------------

@callback(
    Output('invst-bar', 'figure'),
    Input('year-selector-main', 'value'),
    Input('dist-selector-6','value'),
    Input('theme-selector-main', 'value')
)
def invst_bar(year_range,district,theme_color):
    filtered_df = tsipass_merged[(tsipass_merged['district'] == district)\
                 & (tsipass_merged['fiscal_year'] >= year_range[0])
                 & (tsipass_merged['fiscal_year'] <= year_range[1])\
                ]

    test_df = filtered_df.groupby(['district','sector'])\
                            .aggregate({'investment in cr': 'sum', 'fiscal_year': 'first'})\
                            .reset_index()\
                            .sort_values(['investment in cr'],ascending = False)[:5]


    test_df['investment in cr'] =round(test_df['investment in cr'],0)

    bar = px.bar(data_frame = test_df,
                y = test_df['sector'].apply(lambda x: shorten_sector_name(x).replace('and','')),
                x = 'investment in cr',
                text = 'investment in cr',
                orientation = 'h',
                color_discrete_sequence = theme_colors[theme_color],
                height = 230,
                width = 450,
                template = 'simple_white',
#                 title = 'Sectoral Investments(Cr.)'
                )
    bar.update_yaxes(title = '')
    bar.update_xaxes(visible = False)
    bar.update_layout( 
                       margin = dict(l = 0, r = 0,t = 0,b = 0),
                       yaxis = dict(autorange ='reversed', tickfont = dict(size = 10)),
                       plot_bgcolor = 'rgba(0,0,0,0)',## Making background transparent:
                       paper_bgcolor = 'rgba(0,0,0,0)'
                     )
    bar.update_traces(width = 0.8)
    return bar

# # -------------------------------  related-dist-datatable   -------------------------------

@callback(
    Output('invest_related_dist', 'data'),
    Input('year-selector-main', 'value'),
#     Input('theme-selector-main', 'value')
    
)
def related_dist_inv_table(year_range):
    df = tsipass_merged[['sector', 'district', 'investment in cr', 'fiscal_year']]

    main_df = df.groupby(['sector'], as_index=False)\
        .aggregate({'district': 'nunique', 'investment in cr': 'sum', 'fiscal_year': 'first'})\
        .sort_values(['district', 'investment in cr', 'fiscal_year'], ascending=False)
    main_df['investment in cr'] = round(main_df['investment in cr'], 2)

    main_df['sector'] = main_df['sector'].apply(lambda x: shorten_sector_name(x) if isinstance(x, str) else x)\
                                         .apply(lambda x: x.replace('and', '')\
                                         .replace(' Cement', '').replace(',Industrial', ''))

    filtered_df = main_df[(main_df['fiscal_year'] >= year_range[0]) & (main_df['fiscal_year'] <= year_range[1])]

    return filtered_df[['sector','district','investment in cr','fiscal_year']].to_dict('records')

@callback(
    Output('invest_related_dist', 'page_size'),
    Input('select-top-n', 'value')
)
def update_page_size(page_size):
    return page_size

@callback(
    Output('invest_related_dist', 'style_data_conditional'),
    Input('year-selector-main', 'value'),
    Input('theme-selector-main', 'value')
)
def update_data_bars(year_range, theme_color):
    filtered_df = tsipass_merged[(tsipass_merged['fiscal_year'] >= year_range[0])\
                                 & (tsipass_merged['fiscal_year'] <= year_range[1])]

#     color_scale = theme_colors.get(theme_color, px.colors.sequential.RdPu[:5][::-1])
    
    color_gradient = theme_colors.get(theme_color, px.colors.sequential.RdPu[:5][::-1])

    styles = data_bars(filtered_df, 'investment in cr',theme_color)
    return styles

@callback(
    Output('card-header-8','style'),
    Output('card-header-9','style'),
    Output('card-header-10','style'),
    Output('card-header-11','style'),
    Input('theme-selector-main','value'),
)

def update_color(color):
    card_header_style = {'background-color':color,'font-size':12,'font-weight':'bold',
                         'font-family':'Arial','display':'flex','border-radius':'5px 5px 0px 0px','height':'45px'}
    return card_header_style,card_header_style,card_header_style,card_header_style
