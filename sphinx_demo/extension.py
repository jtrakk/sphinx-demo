from docutils import nodes
from docutils.parsers.rst import Directive


class my_container(nodes.container):
    pass


def visit_my_container(self, node):
    self.body.append(self.starttag(node, 'div'))
    self.add_fignumber(node)
    # self.body.append(node['title'])
    self.visit_container(node)


def depart_my_container(self, node):
    self.depart_container(node)
    self.body.append('</div>')

class Mycontainer(Directive):

    has_content = True

    def run(self):
        container_node = my_container()
        container_node += nodes.caption(text="".join(self.content))
        return [container_node]


def setup(app):
    # my-container
    app.add_enumerable_node(
        my_container, "numbered-container", html=(visit_my_container, depart_my_container)
    )
    app.add_directive("numbered-container", Mycontainer)
