import dash
from flask import Flask
from dash import dcc, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd

# Initialize Flask Server
server = Flask(__name__)

# Define Dash apps with Flask as the server
app1 = dash.Dash(__name__, server=server, routes_pathname_prefix='/app1/', external_stylesheets=[dbc.themes.LUX])
app2 = dash.Dash(__name__, server=server, routes_pathname_prefix='/app2/')

# Data Assets
df_resume = pd.read_csv(r'/Users/jbslaunwhite01/projects/portfolio/resume.csv')

# Define the Navigation bar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Portfolio", href="/app1/")),
        dbc.NavItem(dbc.NavLink("Project 1", href="/app2/")),
    ],
    brand="Main Dashboard",
    brand_href="/",
    color="primary",
    dark=True,
)

# Define the layout of app1
app1.layout = html.Div([navbar,
    html.H1(children='Jonas Slaunwhite', style={'textAlign':'center'}),
    html.P(children='Professional Portfolio', style={'textAlign':'center'}),
    # Add a container to hold the content of the entire single-page report
    dbc.Container([
        html.Section(id='bio', children=[
            html.H1("Biography"),
            html.P(children="""My name is Jonas Slaunwhite, from Halifax, Nova Scotia. I'm a warm-hearted professional who takes pride in my extensive experience within the financial services, alternative investment, and consulting sectors. As a dedicated leader, I enjoy collaborating with diverse teams to create meaningful change and drive success. 
                   \n My expertise lies in data analytics, business analysis, and business transformation, along with project management, financial asset valuation, derivative investment valuation, and risk management. I hold an undergraduate degree with a focus on Accounting from St. Mary's University, which has laid the foundation for my continued growth.
                   \n I am a self-taught python developer, starting in 2016 with three years of professional development experience and I continue to work on expanding my knowledge in data analytics, application development and web applications.
                   """),
            # Content for Biography
        ]),
        html.Hr(),  # Add horizontal line for separation
        html.Section(id='skills', children=[
            html.H1("Skills"),
            html.P(children="Python Data Analytics & Software Engineering"),
            html.P(children="Big Data Analytics with Apache Spark"),
            html.P(children="Business Analysis with SQL"),
            html.P(children="Advanced Applied Finance & Accounting"),
            html.P(children="Project Management & Engagement Leadership"),
            # Content for Skills
        ]),
        html.Hr(),
        html.Section(id='resume', children=[
            html.H1("Resume"),
            dash_table.DataTable(data=df_resume.to_dict('records'), page_size=10),
            
        ]),
        html.Hr(),
        html.Section(id='education', children=[
            html.H1("Education"),
            html.P(children="Saint Mary's University - Bachelor of Commerce, Accounting (2012)"),
            
        ]),
        html.Hr(),
        html.Section(id='projects', children=[
            html.H1("Projects"),
            # Content for Projects
        ]),
        html.Hr(),
        html.Section(id='contact', children=[
            html.H1("Contact"),
            html.P(children="LinkedIn: https://www.linkedin.com/in/jbslaunwhite/"),
            html.P(children="GitHub: https://github.com/jb-s01"),
            # Content for Contact
        ]),
    ], fluid=True)
])

# Define the layout of app2
app2.layout = html.Div([navbar,
    html.H1('App 2'),
    html.P('This is the second Dash app.')
])

# Define the default route for the main dashboard or landing page
@server.route('/')
def render_dashboard():
    # You can return a simple string or an HTML page with links to your Dash apps
    return '''
    <h1>Main Dashboard</h1>
    <p>Welcome to the main dashboard. Use the navigation bar to visit the apps:</p>
    <ul>
        <li><a href="/app1/">Portfolio</a></li>
        <li><a href="/app2/">Project 1</a></li>
    </ul>
    '''

if __name__ == '__main__':
    server.run(debug=True)
