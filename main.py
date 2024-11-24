from collections import Counter
from utils import read_input_file, save_output_file, build_hufman_table, input_file, output_file, table_file, generate_huffman_codes, build_huffman_tree, save_file


def compress_huffman(input):

    frequency = Counter(input)

    # Build the Huffman tree
    root = build_huffman_tree(frequency)

    # generating codes
    huffman_codes = generate_huffman_codes(root)

    compressed_data = ""
    for char in input :
        compressed_data += huffman_codes[char]

    save_output_file(table_file, huffman_codes)
    save_file(output_file, compressed_data) 

    return compressed_data


def decompress_huffman(compressed_data: str):
    compressed_data += '$' # dumy char
    huffman_table = read_input_file(table_file)
    hufman_dict = {}
    for line in huffman_table.split("\n") :
        line_splited = line.split(',')
        hufman_dict[line_splited[1]] = line_splited[0]

    decompressed_data=""
    current_binary = ""
    for binary_code in compressed_data:
        if(current_binary in hufman_dict):
            decompressed_data += hufman_dict[current_binary]
            current_binary = ""

        current_binary += binary_code  
    
    return decompressed_data

def main():
    input_string = read_input_file(input_file)
    compressed_data = compress_huffman(input_string)
    decompress_data = decompress_huffman(compressed_data)

    if(input_string != decompress_data):
        print("fail")
    else:
        print("success")


main()
