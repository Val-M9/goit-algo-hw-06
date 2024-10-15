import networkx as nx
import matplotlib.pyplot as plt

district = nx.Graph()
district.add_nodes_from([
    'Home', 'School', 'Park', 'Library', 'Store', 'Gym', 'Restaurant',
    'Work', 'Bank', 'Pharmacy', 'Cinema', 'Hospital'
])

district.add_edges_from([
    ('Home', 'School', {'weight': 2}),
    ('Home', 'Bank', {'weight': 4}),
    ('Home', 'Work', {'weight': 5}),
    ('Home', 'Gym', {'weight': 3}),
    ('Home', 'Store', {'weight': 1}),
    ('Home', 'Hospital', {'weight': 8}),
    ('Home', 'Cinema', {'weight': 10}),
    ('Home', 'Restaurant', {'weight': 6}),
    ('Home', 'Library', {'weight': 5}),
    ('School', 'Library', {'weight': 2}),
    ('School', 'Park', {'weight': 3}),
    ('School', 'Store', {'weight': 4}),
    ('Park', 'Cinema', {'weight': 8}),
    ('Cinema', 'Library', {'weight': 6}),
    ('Store', 'Bank', {'weight': 3}),
    ('Store', 'Pharmacy', {'weight': 2}),
    ('Pharmacy', 'Bank', {'weight': 4}),
    ('Pharmacy', 'Hospital', {'weight': 2}),
    ('Bank', 'Gym', {'weight': 6}),
    ('Library', 'Work', {'weight': 3}),
])

if __name__ == '__main__':

    num_vertices = district.number_of_nodes()
    num_edges = district.number_of_edges()
    degrees = dict(district.degree())
    density = nx.density(district)

    print(f"Number of vertices: {num_vertices}")
    print(f"Number of edges: {num_edges}")
    print(f"Degrees of vertices: {degrees}")
    print(f"Density: {density:.2f}")

    pos = nx.spring_layout(district)
    nx.draw(district, pos, with_labels=True, node_color='skyblue', font_size=8,
            font_color='black', edge_color='gray', node_size=700)
    plt.gca().set_aspect('equal', adjustable='datalim')
    plt.gca().set_xlim(-1.5, 1.5)
    plt.gca().set_ylim(-1.5, 1.5)
    edge_labels = nx.get_edge_attributes(district, 'weight')
    nx.draw_networkx_edge_labels(district, pos, edge_labels=edge_labels)
    plt.show()
