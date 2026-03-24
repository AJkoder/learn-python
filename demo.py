#Argparese
import argparse
parser=argparse.ArgumentParser()

parser.add_argument('--name')
parser.add_argument('--age')
args=parser.parse_args()

print(f"Name is {args.name} and age is {args.age}.")