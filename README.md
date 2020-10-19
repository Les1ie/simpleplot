# Simpleplot

A simple plot library used to plot graph with arrtibuted vertices and edges.

## Usage

### Installation

```cmd
git clone https://github.com/Les1ie/simpleplot.git simpleplot
cd simpleplot
pip install -r requirements.txt
```

### Vectice' Attribute
- [ ] color 

### Edge's Attribute
- [x] color
- [x] direction (default is directed)
- [x] linked vertices (source and target)

## Example


```cmd
python simpleplot --edges edges.csv --output simpleplot.html
```

## Note

To expert the requriements of this project, use `pipreq` as follow:
```cmd
pipreqs ./
```

Do not use `pip freeze` because it only saves the packages that are installed with pip install in your environment.
 
Documents of the dependicies libraries:
- [Echarts api](https://pyecharts.org/#/zh-cn/series_options?id=linestyleopts%ef%bc%9a%e7%ba%bf%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9)
- [Echarts gallery](https://gallery.pyecharts.org/#/Graph/graph_les_miserables)
- [pipreqs github](https://github.com/bndr/pipreqs)