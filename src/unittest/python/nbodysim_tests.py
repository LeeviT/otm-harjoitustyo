from unittest import TestCase
from main.python.quadtree.node import Node
from main.python.quadtree.body import Body
from enum import Enum
from main.python.quadtree.node_storage import NodeStorage
from main.python.quadtree.node_direction import NodeDirection
from main.python.math.center_of_mass import calculate_coms
from main.python.io.input_file_reader import read_data_to_body_list, read_number_of_bodies
from main.python.math.forces import check_if_related_node_added


class TestMath(TestCase):

    def test_check_if_related_node_added(self):
        calculated_nodes = []
        calculated_nodes.extend([34, 21, 1233,  12, 44])
        is_added = check_if_related_node_added(123, calculated_nodes)
        self.assertTrue(is_added)


class TestInputFileReader(TestCase):

    # src/main/resources/randominput.dat
    def test_read_number_of_bodies(self):
        nob = read_number_of_bodies("src/main/resources/randominput.dat")
        self.assertEqual(nob, 100)

    def test_read_data_to_list(self):
        nob, body_list = read_data_to_body_list("src/main/resources/randominput.dat")
        self.assertEqual(body_list[0].get_x(), 0.49635357897449217)


class TestNodeDirection(TestCase, Enum):

    def test_init(self):
        NodeDirection(Enum)


class TestCenterOfMass(TestCase):

    def test_calculate_com(self):
        body_list = []
        body1 = Body(1, 1.0, 0.25, 0.5, 0.1, 0.1)
        body2 = Body(2, 1.0, 0.75, 0.5, 0.1, 0.1)
        body_list.append(body1)
        body_list.append(body2)
        node_storage = NodeStorage()
        root_node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
        node_storage.add_node_to_storage(root_node, None)
        root_node.add_body_to_quadtree(body_list[0], node_storage, body_list)
        root_node.add_body_to_quadtree(body_list[1], node_storage, body_list)
        calculate_coms(node_storage, body_list)
        self.assertEqual(node_storage.get_node_using_id(0).get_com(), (0.5, 0.5, 2.0))


class TestNode(TestCase):

    def test_level(self):
        node = Node(0.0, 0.25, 0.25, 0.5, 'NW')
        level = node.get_level()
        self.assertEqual(level, 2)

    def test_generate_node_id_root(self):
        node = Node(0.0, 1.0, 0.0, 1.0, 'ROOT')
        root_id = node.generate_node_id(0)
        self.assertEqual(0, root_id)

    def test_node_get_info(self):
        node = Node(0.5, 1.0, 0.0, 0.5, 'SE')
        node_info = node.get_info()
        self.assertEqual(node_info, (0, 0.5, 1.0, 0.0, 0.5))


class TestBody(TestCase):

    def test_get_id(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        body_id = body.get_id()
        self.assertEqual(body_id, 1)

    def test_get_mass(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        mass = body.get_mass()
        self.assertEqual(mass, 12.0)

    def test_get_x(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        x = body.get_x()
        self.assertEqual(x, 0.3)

    def test_get_y(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        y = body.get_y()
        self.assertEqual(y, 0.6)

    def test_get_vx(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        vx = body.get_vx()
        self.assertEqual(vx, 0.1)

    def test_get_vy(self):
        body = Body(1, 12.0, 0.3, 0.6, 0.1, 0.2)
        vy = body.get_vy()
        self.assertEqual(vy, 0.2)
