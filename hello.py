import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple script example.")
    parser.add_argument('name', type=str, help="Your name")
    args = parser.parse_args()
    
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()

