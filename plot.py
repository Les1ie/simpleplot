from pyecharts.options.charts_options import GraphLink, GraphNode
from pyecharts.options.series_options import ItemStyleOpts, LabelOpts, LineStyleOpts
from pyecharts.options import InitOpts
from pyecharts.charts import Graph
import argparse

from DataLoader.dataloader import csv_to_list
import webbrowser


class BaseEdge(GraphLink):
    def __init__(self, **kwargs) -> None:
        directed = kwargs.get("directed", True)
        color = kwargs.pop("color", None)

        if directed:
            kwargs["symbol"] = ["none", "arrow"]
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
    BaseEdge(source="结点1", target="结点2",
             color='blue'
             ),
    BaseEdge(source="结点2", target="结点3",
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


def plot(nodes: list, edges: list, **kw) -> None:
    width = kw.get("width", '98vw')
    height = kw.get("height", '95vh')
    repulsion = kw.get("repulsion", 1000)
    layout = kw.get("layout", "force")
    is_draggable = kw.get("is_draggable", True)
    output = kw.get("output", "SimplePlot.html")

    c = (
        Graph(init_opts=InitOpts(
            width=width,
            height=height,
        ))
        .add("", nodes, edges, repulsion=repulsion, layout=layout, is_draggable=is_draggable)
        # .set_global_opts(title_opts=TitleOpts(title="Graph-基本示例"))
        .set_global_opts()
        .render(output)
    )

    webbrowser.open(output)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--nodes-input", help="the file contains vertices in graph, it shoud be a csv file.")
    parser.add_argument(
        "--edges-input", help="the file contains edges in graph, it shoud be a csv file.")
    parser.add_argument(
        "--output", help="output file, it should be a html file.")
    args = vars(parser.parse_args())
    node_file = args.get('nodes-input', "./nodes.csv")
    edge_file = args.get('edges-input', "./edges.csv")

    edges_list = csv_to_list(edge_file)
    edges = []
    nodes_id = set()
    for e in edges_list:
        nodes_id.add(e[0])
        nodes_id.add(e[1])
        edges.append(BaseEdge(source=e[0], target=e[1], color=e[2]))

    nodes = [GraphNode(name=node, symbol_size=20) for node in nodes_id]
    plot(nodes=nodes, edges=edges)
    pass


if __name__ == "__main__":
    main()
    pass
