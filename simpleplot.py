from typing import Any
from pyecharts.options.charts_options import GraphLink, GraphNode
from pyecharts.options.series_options import LabelOpts, LineStyleOpts
from pyecharts.options import InitOpts
from pyecharts.charts import Graph
from pyecharts.globals import ThemeType
import pandas as pd

import argparse
import webbrowser

from DataLoader.dataloader import load_file
import helper
import settings


class BaseEdge(GraphLink):
    def __init__(self, **kwargs) -> None:
        directed = kwargs.pop("directed", True)
        color = kwargs.pop("color", None)

        if directed:
            kwargs["symbol"] = ["none", "arrow"]
        else:
            kwargs["symbol"] = "none"

        # emmm, if there is a self-loop...
        # it dosen't work.
        curve = 1 if kwargs['source'] == kwargs["target"] else 0

        super().__init__(linestyle_opts=LineStyleOpts(color=color, curve=curve), **kwargs)


class BaseNode(GraphNode):
    def __init__(self, **kwargs) -> None:
        kwargs['symbol_size'] = kwargs.pop("size", 20)
        color = kwargs.pop("color", None)
        super().__init__(**kwargs,

                         #  label_opts=LabelOpts(color=color)
                         )


def plot(nodes: list, edges: list, **kw) -> None:
    width = kw.get("width", '98vw')
    height = kw.get("height", '95vh')
    repulsion = kw.get("repulsion", 1500)
    layout = kw.get("layout", "force")
    is_draggable = kw.get("is_draggable", True)
    output = kw.get("output", "SimplePlot.html")

    c = (
        Graph(init_opts=InitOpts(
            width=width,
            height=height,
            page_title="SimplePlot",
            theme=ThemeType.MACARONS,
        ))
        .add("", nodes, edges, repulsion=repulsion, layout=layout,
             edge_length=100,
             is_draggable=is_draggable)
        .set_global_opts()
        .render(output)
    )

    webbrowser.open(output)


def main():
    parser = argparse.ArgumentParser(description=helper.descrepition)

    parser.add_argument("-n", "--nodes", help=helper.nodes_help,
                        # default="./nodes.csv",
                        default=None,
                        )
    parser.add_argument(
        "-e", "--edges", help=helper.edges_help, default="./edges.csv")
    parser.add_argument(
        "-o", "--output", help=helper.output_help, default="SimplePlot.html")
    parser.add_argument("-u", "--undirect",
                        help=helper.undirect_help, action="store_true")
    parser.add_argument("-s", "--self-loop",
                        help=helper.selfloop_help, action="store_true")

    args = parser.parse_args()

    allow_selfloop = args.self_loop
    # allow_selfloop = True
    is_global_directed = not args.undirect
    edges_file = args.edges

    edges_df = load_edges(edges_file)
    nodes_id = set()
    nodes_attr_id = set()
    edges = []
    nodes = []

    if args.nodes:
        node_file = args.nodes
        nodes_df = load_nodes(node_file)
        nodes_attr_id.update(nodes_df['name'].values.tolist())
        for i, n in nodes_df.iterrows():
            nodes.append(GraphNode(name=n["name"], symbol_size=n["size"]))

    nodes_id.update(edges_df['source'].values.tolist())
    nodes_id.update(edges_df['target'].values.tolist())

    for i, e in edges_df.iterrows():
        s = e['source']
        t = e['target']
        if s == t:
            print("allow self-loop {}, {}".format(allow_selfloop, s))
        else:
            edges.append(BaseEdge(source=s,
                                  target=t,
                                  color=e['color'],
                                  directed=is_global_directed
                                  ))

    for node in (nodes_id-nodes_attr_id):
        nodes.append(GraphNode(name=node, symbol_size=20))

    plot(nodes=nodes, edges=edges, output=args.output)
    pass


def load_nodes(nodes_file) -> pd.DataFrame:
    node_df = load_file(nodes_file, settings.node_attributes)
    return node_df


def load_edges(edges_file) -> pd.DataFrame:
    edges_df = load_file(edges_file, settings.edge_attributes)
    return edges_df


if __name__ == "__main__":
    main()
