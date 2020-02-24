#!/usr/bin/env python3
import pandas as pd
from bokeh.plotting import figure, output_file, show, ColumnDataSource, save
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.embed import components

df = pd.read_csv('cars.csv')

source = ColumnDataSource(df)


output_file('index.html')
car_list = source.data['Car'].tolist()

p = figure(
    y_range=car_list,
    plot_width=800,
    plot_height=600,
    title='Cars with Top HP',
    x_axis_label='Horsepower',
    tools="pan,box_select,save,reset"
)
p.hbar(y='Car', right='Horsepower', left=0, height=0.4, legend_group='Car',
       fill_alpha=0.75, source=source, fill_color=factor_cmap('Car', palette=Blues8, factors=car_list))
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

hover = HoverTool()
hover.tooltips = """
                <div>
                <h3>@Car</h3>
                <div><strong>Price:</strong>@Price</div>
                <div><strong>HP:</strong>@Horsepower</div>
                <div><img src="@Image" alt="" width=200/></div>
                </div>
                """
p.add_tools(hover)
save(p)
script, div = components(p)
print(div)
print(script)
