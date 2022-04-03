<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Generating PDF <hr/>
`ReportLab` : Pyton tools to generate PDF

We will be using Page Layout and Typography using Scripts (PLATYPUS)

```python
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

from reportlab.platypus import SimpleDocTemplate
report = SimpleDocTemplate("/tmp/report.pdf")
```

Next create text, use `Flowables` : Cunks of a document that reportlab can arrange to complete report

```python
# Individual elements in the final document
from reportlab.platypus import Paragraph, Spacer, Table, Image

# Tell what style each part of document have
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
```

Next, we'll create the text
```python
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

report.build([report_title]) # Generate the PDF
```

<br>

## Creating Table <hr/>
To create table, you need your data to be 2 dimensional list
```python
table_data = [['elderberries', 1], ['figs', 1], ['apples', 2], ['durians', 3], ['bananas', 5], ['cherries', 8], ['grapes', 13]]

# report_table = Table(data=table_data)
# Creating table with Color
from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

report.build([report_title, report_table])
```

<br>

## Adding Graphic to PDFs <hr/>
We are going to do a Pie Chart using `Drawing` Flowable

```python
from reportlab.graphics.charts.piecharts import Pie

report_pie = Pie(width=3*inch, height=3*inch)
```
```python
report_pie.data = [2, 5, 8, 3, 1, 1, 13]
report_pie.labels = ['apples', 'bananas', 'cherries', 'durians', 'elderberries', 'figs', 'grapes']
```


Pie object isn't Flowable, so it is placed inside `Drawing` Flowable.
```python
from reportlab.graphics.shapes import Drawing

report_chart = Drawing()
report_chart.add(report_pie)
```

Rwebuild the PDFs
```python
report.build([report_title, report_table, report_chart])
```
