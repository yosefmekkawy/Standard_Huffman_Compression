import heapq

input_file = "input.txt"
output_file = "output.txt"
table_file = "table.txt"

class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency
    

def read_input_file(input_file):
    """Reads the input string from a file."""
    with open(input_file, 'r') as file:
        return file.read().strip()



def save_output_file(output_file, huffman_codes):
    """Saves the Huffman codes to an output file."""
    with open(output_file, 'w') as file:
        for char, code in huffman_codes.items():
            # Escape special characters like newline for clarity in the output
            escaped_char = repr(char).strip("'")
            file.write(f"{escaped_char},{code}\n")
        
def save_file(file_name: str, target: str):
    with open(file_name, 'w') as file:
        file.write(target)
     


def build_huffman_tree(frequency):
    """Build the Huffman tree from character frequencies."""
    # Create a priority queue of nodes
    priority_queue = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(priority_queue)

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = Node(frequency=left_child.frequency + right_child.frequency)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]

def generate_huffman_codes(node, code="", huffman_codes={}):
    #Generate Huffman codes recursively.
    if node is not None:
        if node.symbol is not None:  # Leaf node
            huffman_codes[node.symbol] = code
        generate_huffman_codes(node.left, code + "0", huffman_codes)
        generate_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes


def build_hufman_table(output_file):
    pass