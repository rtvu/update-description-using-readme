import argparse
import os


def get_description(readme_path):
    description = ""
    with open(readme_path, "r") as readme:
        for line in readme:
            line = line.strip()
            if len(line) > 0 and line[0] != "#":
                description = line
                break

    output_path = os.getenv("GITHUB_OUTPUT")
    with open(output_path, "a") as output:
        output.write(f"description={description}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("readme_path", nargs="?", type=str, help="Path to README", default="README.md")
    args = parser.parse_args()

    get_description(readme_path=args.readme_path)


if __name__ == "__main__":
    main()
