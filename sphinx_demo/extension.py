import uuid

import sphinx.application
from docutils import nodes
import docutils.parsers.rst.directives
from docutils.parsers.rst import Directive


class my_element(nodes.Element):
    pass


def visit_my_element(self, node):

    self.visit_container(node)


def depart_my_element(self, node):
    self.depart_container(node)


class MyElement(Directive):
    option_spec = {"name": docutils.parsers.rst.directives.unchanged}

    has_content = True

    def run(self):
        element_node = my_element()

        name = self.options.get("name")
        if name is None:
            # TODO Somehow get the name off the surrounding label?
            name = str(uuid.uuid4())
        element_node["names"] = [name]

        element_node += nodes.caption(text="".join(self.content))

        self.state.document.note_implicit_target(element_node)

        return [element_node]


def setup(app: sphinx.application.Sphinx):
    # my-container
    app.add_enumerable_node(
        my_element,
        "container",
        lambda node: node["names"][0],
        html=(visit_my_element, depart_my_element),
    )
    app.add_directive("numbered-object", MyElement)
