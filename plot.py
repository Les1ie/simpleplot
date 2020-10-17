from pyecharts.options.charts_options import GraphLink, GraphNode
from pyecharts.options.series_options import ItemStyleOpts, LabelOpts, LineStyleOpts
from pyecharts.options import InitOpts
from pyecharts.charts import Graph


class BaseLink(GraphLink):
    def __init__(self, **kwargs) -> None:
        directed = kwargs.get("directed", True)
        color = kwargs.pop("color", None)

        if directed:
            kwargs["symbol"] = ["arrow", "none"]
        else:
            kwargs["symbol"] = "none"

        super().__init__(linestyle_opts=LineStyleOpts(color=color), **kwargs)


# class BaseNode(GraphNode):
#     def __init__(self, **kwargs) -> None:
#         kwargs['size'] = 20
#         color = kwargs.pop("color", None)

#         super().__init__(**kwargs,
#                          label_opts=LabelOpts(color="green")
#                          )

def BaseNode(**kw) -> dict:
    name = kw.get("name", "")
    color = kw.get("name", "red")
    return {
        "id": name,
        "name": name,
        "symbolSize": 20,
        "itemStyle": {"normal": {"color": color}},
    },


nodes = [
    GraphNode(name="结点1", symbol_size=10,),
    GraphNode(name="结点2", symbol_size=20),
    GraphNode(name="结点3", symbol_size=30),
    GraphNode(name="结点4", symbol_size=40),
    GraphNode(name="结点5", symbol_size=50),
]
links = [
    {},
    BaseLink(source="结点1", target="结点2",
             color='blue'
             ),
    BaseLink(source="结点2", target="结点3",
             # color='green',
             ),
    GraphLink(source="结点3", target="结点4",
              linestyle_opts=LineStyleOpts(color='black')
              ),
    GraphLink(source="结点4", target="结点5",
              linestyle_opts=LineStyleOpts(color='red')
              ),
    GraphLink(source="结点5", target="结点1",
              linestyle_opts=LineStyleOpts(color='rgb(160,82,45)')
              ),
    GraphLink(source="结点4", target="结点1",
              linestyle_opts=LineStyleOpts(color='rgb(175,238,238)')
              ),
]


c = (
    Graph(init_opts=InitOpts(
        width='98vw',
        height='95vh',
    ))
    .add("", nodes, links, repulsion=1000,layout="force",is_draggable=True)
    # .set_global_opts(title_opts=TitleOpts(title="Graph-基本示例"))
    .set_global_opts()
    .render("graph_base.html")
)
