from docutils import nodes
import docutils.parsers.rst.directives
from docutils.parsers.rst import Directive


class my_container(nodes.container):
    pass


def visit_my_container(self, node):

    self.visit_container(node)


def depart_my_container(self, node):
    self.depart_container(node)


class Mycontainer(Directive):
    option_spec = {"name": docutils.parsers.rst.directives.unchanged}

    has_content = True

    def run(self):
        container_node = my_container()

        name = self.options.get("name")
        if name is None:
            # TODO Somehow get the name off the surrounding label?
            name = "SOMETHING_ELSE"
        container_node.names = [name]

        container_node += nodes.caption(text="".join(self.content))
        return [container_node]


def setup(app):
    # my-container
    app.add_enumerable_node(
        my_container,
        "container",
        lambda node: node.names[0],
        html=(visit_my_container, depart_my_container),
    )
    app.add_directive("numbered-container", Mycontainer)
