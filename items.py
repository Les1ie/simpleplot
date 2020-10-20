from pyecharts.options.charts_options import GraphLink, GraphNode
from pyecharts.options.series_options import LabelOpts, LineStyleOpts
from pyecharts.options import InitOpts
from pyecharts.charts import Graph


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