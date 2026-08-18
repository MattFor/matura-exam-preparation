from typing import List
from main import get_file


# Main must return data or [output_file_name, data]
def main() -> str | List[str]:
	file = get_file("!DATA_FILE_NAME_HERE!")

	return ["!OUTPUT_FILE_NAME_HERE!", f"!OUTPUT_DATA_HERE!"]


if __name__ == "__main__":
	main()  # All submodules are executed as main during import
