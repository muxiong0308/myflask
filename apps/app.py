# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.pages import (
    overview,
    pricePerformance,
    portfolioManagement,
    feesMins,
    distributions,
    newsReviews,
)


def init_app(server):
    appDash = dash.Dash(__name__,
                        meta_tags=[{
                            "name": "viewport",
                            "content": "width=device-width"
                        }],
                        server=server,
                        url_base_pathname="/dashboard/")    

    # Describe the layout/ UI of the app
    appDash.layout = html.Div(
        [dcc.Location(id="url", refresh=False),
         html.Div(id="page-content")])

    # Update page
    @appDash.callback(Output("page-content", "children"),
                      [Input("url", "pathname")])
    def display_page(pathname):
        if pathname == "/dashboard/price-performance":
            return pricePerformance.create_layout(appDash)
        elif pathname == "/dashboard/portfolio-management":
            return portfolioManagement.create_layout(appDash)
        elif pathname == "/dashboard/fees":
            return feesMins.create_layout(appDash)
        elif pathname == "/dashboard/distributions":
            return distributions.create_layout(appDash)
        elif pathname == "/dashboard/news-and-reviews":
            return newsReviews.create_layout(appDash)
        elif pathname == "/dashboard/full-view":
            return (
                overview.create_layout(appDash),
                pricePerformance.create_layout(appDash),
                portfolioManagement.create_layout(appDash),
                feesMins.create_layout(appDash),
                distributions.create_layout(appDash),
                newsReviews.create_layout(appDash),
            )
        else:
            return overview.create_layout(appDash)

    return appDash.server
