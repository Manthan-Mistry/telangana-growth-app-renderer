import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash import html
from dash import Input, Output, callback, State

from data_processing import *

theme_colors = {
    '#feccd7': px.colors.sequential.RdPu[:5][::-1],
    '#C7E9C0': px.colors.sequential.Greens[:5][::-1],
    '#FDD0A2': px.colors.sequential.Oranges[:5][::-1],
    '#FCBBA1': px.colors.sequential.Reds[:5][::-1],
    '#C6DBEF': px.colors.sequential.Blues[:5][::-1],
}

author_content = """
## Author: Manthan Mistry 
| Data Analyst 

### Contact Information:
- **Email:** mistrymanthan26@gmail.com
- **LinkedIn:** [Manthan Mistry](https://www.linkedin.com/in/manthan-mistry-6370421bb)

### Project Description:
This analytical dashboard, based on real-time datasets from Open Data Telangana, aims to provide strategic insights into various aspects of Telangana's districts. Through interactive visualizations and data-driven analysis, the dashboard uncovers key patterns, trends, and opportunities for stakeholders to make informed decisions.

### Key Features:
- Interactive visualizations mapped on the Telangana district map (.json)
- Data analysis on monetary, infrastructure, and economic indicators
- Recommendations tailored for top-level management
- Integration of additional datasets for comprehensive insights

### Contributors:
- Data Analysis & Viz Design: Manthan Mistry

### Version:
Dashboard Version 1.0 (Last Updated: March 11, 2024)

### Acknowledgments:
- *__Telangana Government__* for providing real-time datasets
- *__Open Data Telangana__* for valuable public access resources
- *__Codebasics__* for presenting opportunity via their resume project challanges

### Privacy and Security:
Rest assured, all data handling adheres to strict privacy and security measures. The dashboard ensures the confidentiality and integrity of sensitive information.

### Feedback and Support:
Your feedback is valuable! For inquiries, feedback, or technical support, please reach out to Manthan Mistry at mistrymanthan26@gmail.com.
"""

navbar = dbc.Container([
    dbc.NavbarSimple(
        id="navbar",
        class_name = 'navbar',
        children=[
    dbc.DropdownMenu(
                [
                    dbc.DropdownMenuItem("Stamp Registration", href="/"),
                    dbc.DropdownMenuItem("Transportation", href="/transportation"),
                    dbc.DropdownMenuItem("Ts-iPASS", href="/tsipass"),
                    dbc.DropdownMenuItem("Employment", href="/employement"),
                ],
                label="Pagination",
                color="transparent",
                size = 'sm',
                class_name = 'pagination',
                style={'background-color': 'transparent', 'border': 'none',
                        'color': 'black', 'fontSize': '14px'},
            ),        
            dbc.Button(
        id="menu-dropdown",
        children=[
            dbc.DropdownMenuItem("Filter Pane ⏷", id="filter-pane-dropdown", style={'fontSize': '14px'}),
        ],
        style={"color": "black", 'background-color': 'transparent', 'border': 'none'},
    ),
    dcc.Store(id='filter-pane-state', data=False),  # Store to keep track of the filter pane state
    html.Div(id='filter-pane-content', style={'display': 'none'}),  # Hidden content
    
            dbc.Button("About Project", id="open-about-btn", color="primary",
                       style = {'background-color':'transparent','border':'none','color':'black','fontSize':'14px'}),
                    dbc.Modal([
                        dbc.ModalHeader("About Project"),
                        dbc.ModalBody(
                            [
                                html.P(
                                    "Telangana is one of the fastest-growing states in India and one of the states with an open data policy. "
                                    "The government has published all their data online, making it accessible for analysis and insights."
                                ),
                                html.P(
                                    "Peter Pandey is an aspiring data analyst looking for a project with real-time data to add to his portfolio. "
                                    "He aims to analyze Telangana’s growth among different sectors quantitatively and provide actionable insights to the Telangana government."
                                ),
                                html.P(
                                    "Peter Pandey began this project by drafting some of the key objectives for this analysis. The tasks include:"
                                ),
                                html.Ul([
                                    html.Li("Analyzing the provided research questions and recommendations."),
                                    html.Li("Using tools such as Python, SQL, PowerBI, Tableau, Excel, or PowerPoint for analysis."),
                                    html.Li("Ensuring all insights are visualized and mapped on the Telangana district map provided."),
                                    html.Li("Creating a convincing presentation aimed at top-level management."),
                                    html.Li("Using additional data to support recommendations."),
                                ]),
                                html.P(
                                    "Peter Pandey's work will help the Telangana government make data-informed decisions to further support the growth of the state."
                                ),
                                html.P(
                                    "This project includes resources such as the dataset required for analysis, Telangana district map (.json), metadata, and instructions for using the dataset and district map."
                                ),
                                html.P(
                                    "Credits: The dataset is taken from Open Data Telangana. Thanks to the Telangana Government for providing real-time datasets for public access, a valuable learning asset for analysts and researchers."
                                )
                            ]
                        ),
                        dbc.ModalFooter(
                            dbc.Button("Close", id="close-about-btn", color="danger", className="sm")
                        ),
                    ], id="about-modal", size="lg"),
            
    dbc.Button("About Author", id="open-author-modal", style = {'background-color':'transparent','border':'none',
                                                          'color':'black','fontSize': '14px'}),
    dbc.Modal(
        [
            dbc.ModalHeader("Get to know the Author"),
            dbc.ModalBody(html.Div(dcc.Markdown(author_content))),
            dbc.ModalFooter(
                dbc.Button("Close", id="close-author-modal", className="ml-auto",color = 'danger')
            ),
        ],
        id="author-modal",
        size="xl"
    ),

        ],
        brand="Telangana Growth Dashboard",
        brand_href="#",
        style = {'border-radius':'5px', 'border':'2px solid black',
                 'position':'sticky','top':'0','z-index':'999','display':'flex'}
    ),
    
    dbc.Collapse([
        dbc.Row([
            dbc.Col([
                 html.Label('Select Year-Range',style = {'font-size':12,'margin-left':'20px'}),
                    dcc.RangeSlider(
                                 id= 'year-selector-main',
                                 className = 'rangeslider',
                                 min = 2019,
                                 max = 2022,
                                 step = 1 ,
                                 marks = { int(x): str(x) for x in tsipass_merged['fiscal_year']},
                                 value = [2019,2022])
            ],width = 4, style = {'border-right':'1px dashed grey','margin-bottom':'10px','height':'85%'}),


            dbc.Col([
                html.Label('Theme color',style = {'font-size':12}),
                    dcc.Dropdown(id='theme-selector-main',
                                options=[
                                            {'label': 'Pink', 'value': '#feccd7'},
                                            {'label': 'Green', 'value': '#C7E9C0'},
                                            {'label': 'Orange', 'value': '#FDD0A2'},
                                            {'label': 'Red', 'value': '#FCBBA1'},
                                            {'label': 'Blue', 'value': '#C6DBEF'},
                                        ],
                                value= '#feccd7',
                                multi = False,
                                clearable = False,
                                style = {'font-size': 12}
                                 )
                    ], width = 2,style = {'border-right':'1px dashed grey','margin-bottom':'10px','height':'85%'}), 
            dbc.Col(
            dcc.Markdown('**Note**: Year and Month refers to Fiscal-Year and Fiscal-Month.'),
                style = {'font-size':'12px'}
            )
        ],style = {'display':'flex','position':'sticky','top':0,'z-index':'1000',
                   'background-color':'#F3F3F3','border':'1px solid grey','border-radius':' 0 0 5px 5px','padding-top':'10px',
                   'margin-left':'2px','margin-right':'2px','height':'80px','width':'auto'
                   }), #===================================>> End of filter pane.
    ],
        id="filter-pane",
        is_open=False,
    )
], fluid = True, style = {'margin-bottom':'20px'})

# ------------------------------- Navbar-callbck -------------------------------

@callback(
    Output("filter-pane", "is_open"),
    [Input("filter-pane-dropdown", "n_clicks"), Input("navbar", "id")],
    [State("filter-pane", "is_open")],
)
def toggle_filter_pane(n, nav_id, is_open):
    if nav_id == "navbar" and n:
        return not is_open
    return is_open
# ------------------------------- Theme-color-callbck -------------------------------
@callback(
    Output("navbar", "color"),
    [Input("theme-selector-main", "value")]
)
def update_navbar_color(selected_color):
    return selected_color


# ------------------------------- filter-button-callbck -------------------------------
@callback(
    Output('filter-pane-dropdown', 'children'),
    Output('filter-pane-content', 'style'),
    Input('filter-pane-state', 'data')
)
def update_dropdown_arrow(is_open):
    if is_open:
        return "Filter Pane ⏶", {'display': 'block'}
    else:
        return "Filter Pane ⏷", {'display': 'none'}


@callback(
    Output('filter-pane-state', 'data'),
    Input('menu-dropdown', 'n_clicks'),
    State('filter-pane-state', 'data')
)
def toggle_filter_pane(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# ------------------------------- author-button-callbck -------------------------------

@callback(
    Output("author-modal", "is_open"),
    [Input("open-author-modal", "n_clicks"), Input("close-author-modal", "n_clicks")],
    [dash.dependencies.State("author-modal", "is_open")],
)
def toggle_author_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


# ------------------------------- Modal-callbck -------------------------------

# Callback to open/close the modal
@callback(
    Output("about-modal", "is_open"),
    [Input("open-about-btn", "n_clicks"), Input("close-about-btn", "n_clicks")],
    [State("about-modal", "is_open")],
)
def toggle_about_modal(open_btn_clicks, close_btn_clicks, is_open):
    if open_btn_clicks or close_btn_clicks:
        return not is_open
    return is_open