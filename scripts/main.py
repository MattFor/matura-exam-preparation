import os
from typing import List, Any, Callable
from io import TextIOWrapper

answers = {}  # A dictionary to store answer file objects for later use


def get_import_data(filename) -> str | List[str]:
    return __import__(
        f"src.{filename}",
        fromlist=["main"]
    ).main()


def get_answer(question: str, ans: str) -> TextIOWrapper:
    """
    Function to get or create an answer file for a question and write an answer to it.

    Args:
        question (str): The question for which the answer is being stored.
        ans (str): The answer to the question.

    Returns:
        file: The file object where the answer is stored.
    """

    if question not in answers.keys():
        answers[question] = open(f"odp/{question}", "w")  # Open or create an answer file
    answers[question].write(f"{ans}{"" if ans[-1] == "\n" else "\n"}")  # Write the answer to the file
    return answers[question]  # Return the file object


def get_file(path: str, func: Callable[[str], Any] = lambda x: x.rstrip()) -> Any:
    """
    Function to read lines from a file and apply a function to each line.

    Args:
        path (str): The path to the file to be read.
        func (function, optional): A function to be applied to each line read from the file. Defaults to .rstrip().

    Returns:
        list: A list containing the lines of the file after applying the function.
    """

    file = []

    with open(f"dane/{path}.txt") as f:
        for line in f.readlines():
            file.append(func(line))  # Apply the provided function to each line and append to the list

    return file  # Return the list containing lines of the file


class Answer:
    def __init__(self, task_answer_txt: str, task_data: str):
        """
        Class to handle answers to questions.

        Args:
            task_answer_txt (str): The question for which the answer is being handled.
            task_data (str): The module path containing the function to compute the answer.
        """

        get_answer(
            f"{task_answer_txt}.txt",
            task_data  # Get the answer using the main function from the specified module
        )


def main() -> None:
    """
    Main function to gather answers and save them to appropriate files

    This function traverses the ./src folder, picks out the .py file names, and generates the answer classes.
    """

    files = [f for f in os.listdir("./src") if f.endswith(".py")]

    if len(files) == 0:
        print("No .py files found.")
        return None

    for f_name in files:
        task = f_name.split(".")[0]
        task_data = get_import_data(task)
        Answer(
            f"{  # ZadanieX_X if task returns "" and not ["", ""]
                f"zadanie{task}" if type(task_data) is str
                else task_data[0]
            }",
            task_data if type(task_data) is str  # X_X
            else task_data[1]
        )


if __name__ == '__main__':
    main()  # Main script to run to gather answers
