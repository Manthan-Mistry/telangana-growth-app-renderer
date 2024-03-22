
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import html
import dash_html_components as html
from dash import Input, Output, callback

from data_processing import *
from insights import *

theme_colors = {
    '#feccd7': px.colors.sequential.RdPu[:5][::-1],
    '#C7E9C0': px.colors.sequential.Greens[:5][::-1],
    '#FDD0A2': px.colors.sequential.Oranges[:5][::-1],
    '#FCBBA1': px.colors.sequential.Reds[:5][::-1],
    '#C6DBEF': px.colors.sequential.Blues[:5][::-1],
}

dash.register_page(__name__, path = '/', name = 'Stamp registration')

layout = dbc.Container([
    dbc.Row([ #====================================================================>> Start of Row 1.
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                            dbc.Col([
                                dbc.Label(['Select Measure:'], style = {'font-size':12,'margin-right':'5px','margin-top':'5px'}),
                                dcc.Dropdown(id='radio-measure',
                                                options = [{'label': 'Doc_Reg_Rev','value':'documents_registered_rev'},
                                                           {'label': 'Estamps_Rev','value':'estamps_challans_rev'}],
                                                value= 'documents_registered_rev',
                                                multi=False,
                                                clearable=False,
                                                style = {'width':'120px','font-size': 12,'margin-top':'-2px'}
                                                 )
                                    ], width = 11, style = {'display':'flex'}),
                    dbc.Col([dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'insight-pie-1'),
                            color = 'none', outline = True,size = 'md', class_name = 'insight-btn')],
                            width = 1,
                            style = {'margin-left':'-5px','margin-top':'-5px'}),
                    
                    dbc.Tooltip([
                        dcc.Markdown(graph_1_insignt)
                    ],target = 'insight-pie-1', placement = 'bottom')
                        
                ],id = 'card-header-1', class_name = 'header'),
                    dbc.CardBody([
                        dcc.Graph(id='piechart',config = {'displayModeBar':False}),
                                ],style = {'border-radius':'0 0 5px 5px'}),
                    
                        ],color = "dark", outline = True, style = {'border':'2px solid black'})
                ], width = 12, md = 4, style = {'height':'100%','flexGrow':1}),
        
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                        dbc.Col([ html.Label(['#Estamps_challans V/s #Doc_registerations']) 
                                ], width = 6,
                                style = {'margin-top':'5px'}),
                            
                            dbc.Col([ 
                                html.Label('Year:',style = {'font-size':12,'margin-right':'5px','margin-top':'5px'}),
                                dcc.Dropdown(id='year-selector',
                                            options=[{'label': 2020, 'value': 2020},
                                                     {'label': 2021, 'value': 2021},
                                                     {'label': 2022, 'value': 2022},
                                                    ],
                                            value= 2021,
                                            multi=False,
                                            clearable=False,
                                            style = {'font-size': 12,'margin-top':'-2px','width':'100px'}
                                             )
                                 ], width = 5, style = {'display':'flex','margin-left':'10px'}),
                    dbc.Col([dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'info-multiline'),
                            color = 'none', outline = True,size = 'md',class_name = 'insight-btn')],
                            style = {'margin-left':'25px','margin-top':'-5px'}),
                    
                    dbc.Tooltip(dcc.Markdown([graph_2_insignt]),
                                target = 'info-multiline', placement = 'bottom')
                            ],id = 'card-header-2', class_name = 'header'),
                    dbc.CardBody([
                        dcc.Graph(id = 'multi-linechart',config = {'displayModeBar':False}),
                                 ], style = {'border-radius':'0 0 5px 5px'})
                    
                    ],color = "dark", outline = True,style = {'border':'2px solid black'})
                ],width = 12, md = 8, style = {'height':'100%','flexGrow': 1}),
    
           ], style = {'display':'flex','justiftContent':'around',
                       'padding':'auto 10px','margin-bottom':'20px'}),#============>> End of Row 1.
    
    dbc.Row([ #========================================================>> Start of Row 2.
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        dbc.Col([
                            dbc.RadioItems(
                                            id = 'radio',
                                            class_name = 'radio-items',
                                            options = [{'label': 'Echallan - Doc_Rev','value':'Abs-Diff'},
                                                       {'label': 'YoY_Doc_Rev_Growth','value':'Growth-Diff'}],
                                            value = 'Abs-Diff',
                                            inline = True,
                                            style = {'display':'flex','justifyContent':'left'}
                                            )
                                ], width = 8, style = {'margin-top':'5px'}),
                        dbc.Col([
                                dbc.Label(['Year:'], style = {'font-size':12,'margin-right':'5px','margin-top':'10px'}),
                                dcc.Dropdown(id='year-selector-growth-diff',
                                    options=[{'label': x, 'value': x} for x in stamps_merged['fiscal_year'].sort_values().unique()],
                                    value= 2019,
                                    multi=False,
                                    clearable=False,
                                    style = {'font-size': 12,'width':'100px'}
                                     )
                                    ], width = 4, style = {'margin-top':'-4px', 'display':'flex'}),
                        dbc.Col([dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'insight-3'),
                            color = 'none', outline = True,size = 'md',class_name = 'insight-btn')],
                            width = 1,
                            style = {'margin-top':'-5px','margin-left':'-35px'}),
                    
                        dbc.Tooltip([
                            dcc.Markdown(graph_3_insignt)
                        ],target = 'insight-3', placement = 'bottom')

                                  ],id = 'card-header-3',
                        style = {'background-color':'#FECCD7','font-size':12,
                                   'font-family':'Arial','font-weight':'bold',
                                   'border-radius':'5px 5px 0px 0px','height':'45px',
                                   'display':'flex'
                                }),
                        dbc.CardBody([
                            dcc.Graph(id='abs-diff-bar',config = {'displayModeBar':False}),
                                    ],style = {'border-radius':'0 0 5px 5px','width':'100%'})
                    
                        ],color = "dark", outline = True, style = {'border':'2px solid black'})
                 ],width = 12, md = 7,style = {'height':'100%','margin-left':'none','flexGrow': 1}),
        
        dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                    dbc.Col([
                        dbc.Label(['Segments by Estamp_Rev'],  style = {'font-size':12,'margin-top':'5px','margin-right':'10px'}),
                            ], width = 6),
                        dbc.Col([
                            dbc.Label(['Year:'], style = {'margin-right':'5px','margin-top':'10px','font-size':'12px'}),
                            dcc.Dropdown(id='year-selector-segment',
                                    options=[{'label': x, 'value': x} for x in stamps_merged['fiscal_year'].sort_values().unique()],
                                    value= 2019,
                                    multi=False,
                                    clearable=False,
                                    style = {'font-size': 12,'width':'100px'}
                                     ),
                        ], style = {'margin-top':'-4px', 'display':'flex'}),
                        
                    dbc.Col([dbc.Button(html.I(className = 'bi bi-lightbulb-fill', id = 'insight-4'),
                        color = 'none', outline = True,size = 'md',class_name = 'insight-btn')],
                        width = 1,
                        style = {'margin-top':'-5px','margin-left':'5px'}),

                    dbc.Tooltip([
                        dcc.Markdown(graph_4_insignt)
                    ],target = 'insight-4', placement = 'left'),

                    ],id = 'card-header-4',
                        style = {'width':'100%',
                                 'background-color':'#FECCD7',
                               'height':'45px','display':'flex',
                               'fontWeight':'bold','font-family':'Arial'}),
                    dbc.CardBody([
                        dcc.Graph(id = 'segment-bar',config = {'displayModeBar':False}),
                                 ],style = {'border-radius':'0 0 5px 5px'})
                    
                         ],color = "dark", outline = True,style = {'border':'2px solid black'},
                                    )
                ],width = 12, md = 5,style = {'height':'100%','flexGrow': 1,'margin':'none','padding':'none'})
    ], style = {'display':'flex','justiftContent':'around','margin-bottom':'20px'})
], fluid = True)

# Callback for pie-chart(Doc_Rev by districts):
@callback(   
     Output('piechart', 'figure'),
     Input('year-selector-main', 'value'),
     Input('radio-measure','value'),
     Input('theme-selector-main', 'value')
)
    
def update_pie_data(year_val, measure, theme_color): ## year_val == 'value' from the input(year-selector) dropdown and same for month value.
    df = stamps_merged.copy()
    dff = df[(df['fiscal_year'] >= year_val[0]) & (df['fiscal_year'] <= year_val[1])]\
            .groupby(['district'], as_index = False).sum()\
            .sort_values(['documents_registered_rev'], ascending = False)
    
    dff['doc_rev_bn'] = round(dff['documents_registered_rev'].apply(lambda x: x/10**9),2)
    dff['documents_registered_cnt_thousand'] = round(dff['documents_registered_cnt'].apply(lambda x:x/10**3),2)
    
    if measure == 'documents_registered_rev' :
        pie = px.pie(data_frame = dff[:5],
                 names = 'district',
                 values = 'doc_rev_bn',
    #              values = 'estamps_challans_rev',
                 hole = 0.75,
                 hover_data = ['documents_registered_rev'], 
                 height = 240,
#                  width = 280,
                 labels = {'district':'Districts','doc_rev_bn':'Doc_Reg_Rev',
                          'documents_registered_cnt':'Reg_Cnt'}, ## {'column_name':'Name wnat to show'}
                #  color_discrete_sequence = px.colors.sequential.RdPu[:5][::-1],
                color_discrete_sequence = theme_colors[theme_color]
                    )
        hovertemplate = 'District:%{label}<br>Doc_Registered_Revenue: %{value:.2f} Bn<br>Doc_Registration_Cnt: %{text} k'
        text = dff['documents_registered_cnt_thousand']
        
    else:
        pie = px.pie(data_frame = dff[:5],
                 names = 'district',
#                  values = 'doc_rev_bn',
                 values = 'estamps_challans_rev',
                 hole = 0.75,
                 hover_data = ['estamps_challans_rev'], 
                 height = 240,
                #  width = 240,
                 labels = {'district':'Districts','estamps_challans_rev':'Estamps_challan_Rev',
                          'estamps_challans_cnt':'Reg_Cnt'}, ## {'column_name':'Name wnat to show'}
                #  color_discrete_sequence = px.colors.sequential.RdPu[:5][::-1],
                color_discrete_sequence = theme_colors[theme_color]

                    )
        hovertemplate = 'District:%{label}<br>Estamp_challan_Rev: %{value:.2f} Bn<br>Estamp_challan_Cnt: %{text} k'
        text = dff['estamps_challans_cnt']
    
    pie.update_traces(textposition = 'outside',
                      textinfo = 'percent',
                      text = text,
                      hovertemplate = hovertemplate,
                      direction = 'clockwise',
                      marker = dict(line = dict(color = 'black',width = 1))
                      ) ##Removes line-connector bw category and legend. 
    pie.update_layout(showlegend =True, 
                      margin = dict(l = 0, r = 0,t = 0,b = 0),
                      font_size = 10,
                      hoverlabel = dict(bgcolor = 'white',bordercolor = 'black'),
                      legend = dict(bgcolor = 'rgba(0,0,0,0)', x = 0.25, y = 0.5,
                                    font = dict(size = 10)),
                      plot_bgcolor = 'rgba(0,0,0,0)',## Making background transparent:
                      paper_bgcolor = 'rgba(0,0,0,0)'
                     )

    return (pie)

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '280px',  # Set a maximum width for the chart| same as manually typed before making it dynamic(commented out)
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

# -------------------------------  Multiline-start -------------------------------

## callback for multiline chart:
@callback(   
     Output('multi-linechart', 'figure'),
     Input('year-selector', 'value'),
    Input('theme-selector-main', 'value')
)
    
def update_line_data(year_val, theme_color): ## year_val == 'value' from the input(year-seleector) dropdown and same for month value.
    
    fact_stamps_df_filteredforcnt = fact_stamps_df[fact_stamps_df['estamps_challans_cnt'] != 0 ] .copy()

    fact_stamps_df_filteredforcnt['cnt_diff'] = fact_stamps_df_filteredforcnt['estamps_challans_cnt']\
    - fact_stamps_df_filteredforcnt['documents_registered_cnt']

    ans_3a = fact_stamps_df_filteredforcnt.groupby(['month'], as_index = False)\
                                         .sum(['cnt_diff'])\
                                         .sort_values(['month'])\
                                         .merge(dim_date_df)
    
    ans_3a['month_num'] = pd.to_datetime(ans_3a['Mmm'], format = '%b').dt.month
    ans_3a['sort_order'] = np.where(ans_3a.month_num > 3,ans_3a.month_num - 3,ans_3a.month_num + 9) ## Fiscal month logic
    ans_3a.sort_values(['sort_order'], inplace = True)
    
    filtered_df = ans_3a[(ans_3a['fiscal_year'] == year_val)]
    
    rename_columns = {'estamps_challans_cnt':'Estamps_challan_cnt','documents_registered_cnt':'Doc_Rev_cnt'}
    
    filtered_df = filtered_df.rename(columns = rename_columns)
    
    multi_line = px.line(data_frame = filtered_df,
                         x = 'Mmm',
                         y = ['Estamps_challan_cnt','Doc_Rev_cnt'],
                         markers = True,
                        #  color_discrete_map = {'Doc_Rev_cnt':'#fe8ec1','Estamps_challan_cnt':'#fe0175'},
                         color_discrete_map={'Doc_Rev_cnt': theme_colors[theme_color][0],
                                             'Estamps_challan_cnt': theme_colors[theme_color][2]}
                        )

    
    hovertemplate = '<b>%{y:,.0f}'

    multi_line.update_traces(hovertemplate = hovertemplate,
#                              mode = 'lines+markers+text',
                             textposition = 'top center',
#                              text = filtered_df[['estamps_challans_cnt','documents_registered_cnt']]
                            )
    
    multi_line.update_layout( showlegend = True,
                              xaxis = dict(showgrid = True),
                              hovermode = 'x unified',
                              margin = dict(l = 0, r = 0,t = 0,b = 0),
                              font_size = 10,
                              height = 240,
#                               width = 580,
                              hoverlabel = dict(font_size = 12),
                              legend = dict(title = 'Measure', orientation = 'h', font_size = 12),
                              plot_bgcolor = 'rgba(0,0,0,0)',
                              paper_bgcolor = 'rgba(0,0,0,0)'
                              )
    multi_line.update_xaxes(title = '')
    multi_line.update_yaxes(title = '',range = [20000,175000])
#     multi_line.update_yaxes(visible = False)
    return (multi_line)

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '580px',  # Set a maximum width for the chart
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

# ------------------------------- (E-challan-rev)-(doc-registered-rev) ABS-Diff bar -------------------------------

combained_df = fact_stamps_df.merge(dim_date_df,left_on = 'month',right_on = 'month') ## Joining stamps and dimdate tables

final_df_ans_2 = combained_df.merge(dim_districts_df,left_on = 'dist_code',right_on = 'dist_code') ## Joining combined and districts


@callback(   
     Output('abs-diff-bar', 'figure'),
     Input('year-selector-growth-diff', 'value'),
     Input('radio','value'),
    Input('theme-selector-main', 'value')
)


def update_abs_diff_bar(year_val,graph_type, theme_color):
    combained_df = fact_stamps_df.merge(dim_date_df,left_on = 'month',right_on = 'month') ## Joining stamps and dimdate tables

    final_df_ans_2 = combained_df.merge(dim_districts_df,left_on = 'dist_code',right_on = 'dist_code') ## Joining combined and districts

    final_filtered_df = final_df_ans_2[final_df_ans_2['fiscal_year'] == year_val].copy()

    final_filtered_df['abs_diff_Bn'] = (final_filtered_df['estamps_challans_rev'] - \
                                        final_filtered_df['documents_registered_rev'] )/10**9

    ans_2_df = final_filtered_df.groupby(['dist_code'],as_index = True )\
                                .sum(['documents_registered_rev'])\
                                .merge(dim_districts_df, left_on = 'dist_code', right_on = 'dist_code')\
                                .sort_values(['abs_diff_Bn'], ascending = False) [['district','abs_diff_Bn']]

    ans_2_df['abs_diff_Bn'] = round(ans_2_df['abs_diff_Bn'],2)
    
    filtered_19_22_df = dim_date_df [dim_date_df['fiscal_year'].isin([year_val,(year_val+1)])]#&(dim_date_df['fiscal_year']!=2022)]

    intm_df= fact_stamps_df.\
             merge(filtered_19_22_df, left_on = 'month', right_on = 'month').\
             merge(dim_districts_df, left_on = 'dist_code', right_on = 'dist_code')

    filtered_dim_dates_start = intm_df[intm_df['fiscal_year'] == year_val]
    filtered_dim_dates_end = intm_df[intm_df['fiscal_year'] == (year_val+1)]

    doc_rev_generated_start = filtered_dim_dates_start\
                           .groupby(['fiscal_year','district'],
                           as_index = False)['fiscal_year','district','documents_registered_rev'].sum()

    doc_rev_generated_end = filtered_dim_dates_end\
                           .groupby(['fiscal_year','district'],
                            as_index = False)['fiscal_year','district','documents_registered_rev'].sum()

    final_ans_1_b = doc_rev_generated_start.merge(doc_rev_generated_end,
                                               left_on = 'district',
                                               right_on = 'district',
                                               suffixes = ['_start','_end'])\
                                               [['district','documents_registered_rev_start','documents_registered_rev_end']]

    final_ans_1_b['diff'] = final_ans_1_b['documents_registered_rev_end'] - final_ans_1_b['documents_registered_rev_start']

    final_ans_1_b['Growth_Diff_pct'] = round((final_ans_1_b['diff']  / final_ans_1_b['documents_registered_rev_start'])*100,2) 

    ans_1b_df = final_ans_1_b.sort_values(['Growth_Diff_pct'],ascending = False)

    
    if graph_type == 'Abs-Diff':
        bar = px.bar(  data_frame = ans_2_df.iloc[:5],
                       y = 'district',
                       x = 'abs_diff_Bn',
                       text = [f'{i}' for i in ans_2_df['abs_diff_Bn'].iloc[:5].transform(lambda x:'{:.2} Bn'.format(x))],
                       orientation = 'h',
                       color_discrete_sequence = theme_colors[theme_color],
#                        width = 470,
                       height = 240,
                       template = 'simple_white'
                    )

        yaxis_side = 'right' if ans_2_df['abs_diff_Bn'].mean()< 0 else 'left'

        bar.update_yaxes(title = '')
        bar.update_xaxes(visible = False)
        bar.update_layout(barmode = 'stack',
                          yaxis = dict(autorange ='reversed', side = yaxis_side , tickfont = dict(size = 10)),
                          margin = dict(l = 30, r = 0,t = 10,b = 10),
                          plot_bgcolor = 'rgba(0,0,0,0)',## Making background transparent:
                          paper_bgcolor = 'rgba(0,0,0,0)')
        bar.update_traces(textposition = 'auto')
    else:
        bar = px.bar(data_frame = ans_1b_df.iloc[:5], ## Fix FY2022 not showing
             x = 'Growth_Diff_pct',
             y = 'district',
             text = [f'{i}' for i in ans_1b_df['Growth_Diff_pct'].iloc[:5].transform(lambda x:'{:,.2%}'.format(x/100))],
             color_discrete_sequence = theme_colors[theme_color], ## Green color
             template = 'simple_white',
#              width = 470,
             height = 240,
             orientation = 'h')
        
        yaxis_side_growth = 'right' if ans_1b_df['Growth_Diff_pct'].mean()< 0 else 'left'  ## Direction logic for diverging bars
        
        bar.update_layout(barmode = 'stack',
                          yaxis = dict(autorange ='reversed',side = yaxis_side_growth, tickfont = dict(size = 10)),
                          margin = dict(l = 30, r = 0,t = 10,b = 10),
                          plot_bgcolor = 'rgba(0,0,0,0)',## Making background transparent:
                          paper_bgcolor = 'rgba(0,0,0,0)') 
        
        bar.update_xaxes(visible = False)
        bar.update_yaxes(title = '')
    return(bar)

# def update_chart_size(graph_id):
#     chart_width = {
#         'width': '100%',  # Set the chart width to 100% of the container
#         'maxWidth': '470px',  # Set a maximum width for the chart| same as manually typed before making it dynamic(commented out)
#         'margin': 'auto'  # Center the chart horizontally
#     }
#     return chart_width

# -------------------------------  Segmentation bar chart -------------------------------

@callback(   
     Output('segment-bar', 'figure'),
     Input('year-selector-segment', 'value'),
    Input('theme-selector-main', 'value')
)

def update_seg_bar_data(year_val, theme_color):

    filtered_df = final_df_ans_2[final_df_ans_2['fiscal_year'].isin([year_val,(year_val+1)])] 

    agg_df = filtered_df.groupby(['dist_code'], as_index = False)\
    .sum(['estamps_challans_rev'])\
    .sort_values(['estamps_challans_rev'], ascending = False)\
    [['dist_code','estamps_challans_rev']]

    max_investment_value = agg_df.estamps_challans_rev.max()
    min_investment_value = agg_df.estamps_challans_rev.min()

    first_threshold = int((max_investment_value - min_investment_value ) * 0.33) + 1
    second_threshold = int((max_investment_value - min_investment_value ) * 0.66) + 1

    agg_df.loc[(agg_df['estamps_challans_rev'] >= 0) & (agg_df['estamps_challans_rev'] <= first_threshold ), 'Segment'] = 'Low'
    agg_df.loc[(agg_df['estamps_challans_rev'] >= first_threshold + 1 ) & (agg_df['estamps_challans_rev'] <= second_threshold ), 'Segment'] = 'Medium'
    agg_df.loc[ agg_df['estamps_challans_rev'] >= second_threshold + 1 , 'Segment' ] = 'High'

    dist_agg = agg_df.merge(dim_districts_df,how = 'inner',left_on ='dist_code',right_on = 'dist_code')\
                     .set_index('district')['Segment']\
                     .reset_index()

    High_districts = dist_agg[dist_agg['Segment'] == 'High']
    Medium_districts = dist_agg[dist_agg['Segment'] == 'Medium']
    Low_districts = dist_agg[dist_agg['Segment'] == 'Low']

    segmented_df = agg_df.groupby(['Segment'], as_index = False)\
                  .count()\
                  .sort_values(['estamps_challans_rev'], ascending = False)\
                  [['Segment','dist_code']]

    segmented_df.rename(columns = {'dist_code': '#_Districts'}, inplace = True)
    
    bar = px.bar(data_frame = segmented_df,
                x = 'Segment',
                y = '#_Districts',
                text = segmented_df['#_Districts'],
                color_discrete_sequence = theme_colors[theme_color],
#                 title = 'Segmentation by Estamps-Challan',
                height = 240,
#                 width = 330,
                template = 'simple_white'
                )

    bar.update_xaxes(title = '')
    bar.update_yaxes(title = '', visible = False)
    bar.update_layout(margin = dict(l = 10, r = 0,t = 0,b = 0),
                      title = dict(font_size = 14,x = 1.0, y = 0.9),
                      plot_bgcolor = 'rgba(0,0,0,0)',paper_bgcolor = 'rgba(0,0,0,0)')
    bar.update_traces(textposition = 'auto',width = 0.6)
    
    # title = f'Segmentation for {year_val} - {year_val + 1}'
    bar.update_layout(title_text = '')

    return bar

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '330px',  # Set a maximum width for the chart| same as manually typed before making it dynamic(commented out)
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

@callback(
    Output('card-header-1','style'),
    Output('card-header-2','style'),
    Output('card-header-3','style'),
    Output('card-header-4','style'),
    Input('theme-selector-main','value'),
)

def update_color(color):
    card_header_style = {'background-color':color,'font-size':12,'font-weight':'bold',
                         'font-family':'Arial','display':'flex','border-radius':'5px 5px 0px 0px','height':'45px'}
    return card_header_style,card_header_style,card_header_style,card_header_style