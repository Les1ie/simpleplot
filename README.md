# Simpleplot

A simple plot library used to plot graph throuh edges file and vertices file.

It's designed for my gf `WJie` 😘~~

## Usage

### Installation

```cmd
git clone https://github.com/Les1ie/simpleplot.git simpleplot
cd simpleplot
pip install -r requirements.txt
```

### Vectice' Attribute
- [ ] color: string, don't support in current version. 
- [x] size: int, the symbol size of node, default is `20`.

### Edge's Attribute
- [x] color: string, user color's name or `"rgb(r,g,b)"` (**notice it need the double quotes**) to set it.
- [x] direction: default is directed, use the command line parameter `-u` or `--undirected` to set graph undirected.
- [x] linked vertices(source and target): string, there are necessary.
- [ ] self-loop: use command line parameter `-s` or `--self-loop` to set whether self-loop is allowed, but the self-loop edge is difficult to see even it's `Ture` (but you can see the arrow if you shrinking the graph). 

## Example

Plot graph just use edge file:
```cmd
python simpleplot --edges edges.csv --output simpleplot.html
```

Plot undirected graph through both edge file and node file :
```cmd
python simpleplot -e edges.csv -n nodes.csv -o simpleplot.html -u
```

Use `python SimplePlot --help` for detail.

## Note for developer

To expert the requriements of this project, use `pipreq` as follow:
```cmd
pipreqs ./
```

Do not use `pip freeze` because it only saves the packages that are installed with pip install in your environment.
 
Documents of the dependicies libraries:
- [Echarts api: Options](https://pyecharts.org/#/zh-cn/series_options?id=linestyleopts%ef%bc%9a%e7%ba%bf%e6%a0%b7%e5%bc%8f%e9%85%8d%e7%bd%ae%e9%a1%b9)
- [Echarts api: Graph](https://pyecharts.org/#/zh-cn/basic_charts?id=graph%ef%bc%9a%e5%85%b3%e7%b3%bb%e5%9b%be)
- [Echarts gallery](https://gallery.pyecharts.org/#/Graph/graph_les_miserables)
- [Pipreqs github](https://github.com/bndr/pipreqs)
- [Pandas](https://www.pypandas.cn/)