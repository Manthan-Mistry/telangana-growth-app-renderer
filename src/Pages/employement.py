import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from databars_from_zero_custom_color import data_bars

from data_processing import *

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

dash.register_page(__name__, path = '/employement', name = 'Employement')


layout = dbc.Container([
    dbc.Row([    #===========================================>> Page-4 Start
        dbc.Col([
            dbc.Card([
                dbc.CardHeader([
                    dbc.Label(['Employement Trend'], style = {'margin-top':'5px'}),
                    dbc.Label(['Select X axis:'],style = {'margin-top':'5px','margin-right':'5px','margin-left':'120px'}),
                        dbc.Col([
                            dcc.Dropdown(
                                id='timeframe-dropdown-emp',
                                options=[
                                        {'label': 'Fiscal Year', 'value': 'fiscal_year'},
                                        {'label': 'Month', 'value': 'Mmm'},
                                        {'label': 'Qtr', 'value': 'quarter'}
                                        ],
                                value='Mmm',
                                clearable = False,
                                style = {'width':'100px','font-size': 12,'fontWeight':'bold','margin-bottom':'5px'}
                                        )
                                ],width = 2, style = {'margin-top':'-4px'}),
                    dbc.Label(['Sector: '], style = {'margin-top':'5px','margin-right':'5px'}),
                    dbc.Col([
                            dcc.Dropdown(
                                        id='sector-dropdown-emp',
                                        options=[
                                                {'label': x , 'value': x } for x in tsipass_merged['sector'].sort_values().unique()
                                                ],
                                        value = 'Engineering',
                                        clearable = False,
                                        style = {'width':'200px','font-size': 12,'fontWeight':'bold','margin-bottom':'5px'}
                                        )
                            ],width = 5, style = {'margin-top':'-4px','display':'flex'}),
                        ],id = 'card-header-12',  class_name = 'header'),
                dbc.CardBody([
                    dcc.Graph(id='employee-line',config = {'displayModeBar':False}),
                            ], style = {'width':'100%','border-radius':'0 0 5px 5px','padding':'none'}),

                    ],style = {'weight':'100%','padding':'0px','border':'2px solid black'})  ##Page-4 End
        ],style = {'height':'100%'})
    ]) 
], fluid = True)


# # -------------------------------  Employement-line   -------------------------------

@callback(
    Output('employee-line', 'figure'),
    Input('timeframe-dropdown-emp', 'value'),
    Input('year-selector-main','value'),
    Input('sector-dropdown-emp', 'value'),
    Input('theme-selector-main', 'value')

)


def employement_over_time(timeframe, year_range, sector,theme_color):
    
    if timeframe == 'Mmm':
        filtered_df = tsipass_merged[(tsipass_merged['fiscal_year'] >= year_range[0])\
                                     & (tsipass_merged['fiscal_year'] <= year_range[1])\
                                     & (tsipass_merged['sector'] == sector)]
        df = filtered_df.groupby( timeframe, as_index = False).sum()[[timeframe,'number_of_employees','investment in cr']]

        df['month_num'] = pd.to_datetime(df['Mmm'], format = '%b').dt.month
        df['sort_order'] = np.where(df.month_num > 3,df.month_num - 3,df.month_num + 9)
        df.sort_values(['sort_order'], inplace = True)
        
    else:
        filtered_df = tsipass_merged[(tsipass_merged['fiscal_year'] >= year_range[0])\
                                     & (tsipass_merged['fiscal_year'] <= year_range[1])\
                                     & (tsipass_merged['sector'] == sector)]        
        df = filtered_df.groupby( timeframe, as_index = False).sum()[[timeframe,'number_of_employees','investment in cr']]

    emp_line = px.line(data_frame = df,
                       x = timeframe,
                       y = 'number_of_employees',
                       color_discrete_sequence = theme_colors[theme_color],
                       markers = True,
                       text = [f'{i}' for i in df['number_of_employees'].transform(lambda x:'{:,.2}k '.format(x/10**3))],
                       template = 'simple_white',
                       labels = {'number_of_employees':'#_Employees'},
                       height = 240,
                       custom_data = ['investment in cr'],
#                        width = 900
                      )
    
    hovertemplate = '<br>#Employees: <b>%{y:,.0f}</b><br>' + 'Investment: <b>%{customdata:,.2f} Cr</b>'
    
    emp_line.update_xaxes(type = 'category', title = '')
    emp_line.update_yaxes(visible = False)
    emp_line.update_layout(
                           hovermode = 'x unified',
                           xaxis = dict(showgrid = True),
                           hoverlabel = dict(bgcolor = 'white',bordercolor = 'black',font_size = 12),
                           font = dict(size = 10),
                           title = dict(font_size = 16, x = 0 , y = 0.9),
                           margin = dict(l = 10, r = 0,t = 0,b = 0),
                           plot_bgcolor = 'rgba(0,0,0,0)'
                           )
    emp_line.update_traces(textposition = 'bottom right', hovertemplate = hovertemplate)
    return emp_line

def update_chart_size(graph_id):
    chart_width = {
        'width': '100%',  # Set the chart width to 100% of the container
        'maxWidth': '900px',  # Set a maximum width for the chart
        'margin': 'auto'  # Center the chart horizontally
    }
    return chart_width

@callback(
    Output('card-header-12','style'),
    Input('theme-selector-main','value'),
)

def update_color(color):
    card_header_style = {'background-color':color,'font-size':12,'font-weight':'bold',
                         'font-family':'Arial','display':'flex','border-radius':'5px 5px 0px 0px','height':'45px'}
    return card_header_style

