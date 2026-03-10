from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (isinstance(data, list) and all(isinstance(i, int) for i in data)):
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid numeric data")
            num: int = len(data)
            sum_num: int = sum(data)
            avg: float = sum_num / num if num > 0 else 0.0
            result: str = (f"Processed {num} numeric values, sum={sum_num}, "
                           f"avg={avg:.1f}")
            return super().format_output(result)
        except Exception as e:
            return ValueError(f"Error processing numeric data: {e}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if (isinstance(data, str)):
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid text data")

            char: int = len(data)
            words: int = len(data.split())
            result: str = (f"Processed text: {char} characters, {words} words")
            return super().format_output(result)
        except Exception as e:
            return ValueError(f"Error processing text data: {e}")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        return False

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("Invalid log data")
            if "ERROR" in data:
                types = "ERROR"
                warning = "[ALERT]"
            elif "INFO" in data:
                types = "INFO"
                warning = "[INFO]"
            else:
                types = "UNKNOWN"
                warning = "[LOG]"
            result: str = (f"{warning} {types} level detected: "
                           f"{data.split(': ')[1]}")
            return super().format_output(result)
        except Exception as e:
            return (f"Error processing Log data: {e}")


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    numeric = NumericProcessor()
    data1 = [1, 2, 3, 4, 5]
    print(f"Processing data: {data1}")
    print(
        "Validation: "
        f"{'Numeric data verified' if numeric.validate(data1) else 'invalid'}"
    )
    print(f"{numeric.process(data1)}")

    print("\nInitializing Text Processor...")
    text = TextProcessor()
    data2 = "Hello Nexus World"
    print(f"Processing data: {data2}")
    print(
        "Validation: "
        f"{'Text data verified' if text.validate(data2) else 'invalid'}"
    )
    print(f"{text.process(data2)}")

    print("\nInitializing Log Processor...")
    log = LogProcessor()
    data3 = "ERROR: Connection timeout"
    print(f"Processing data: {data3}")
    print(
        "Validation: "
        f"{'Log entry verified' if log.validate(data3) else 'invalid'}"
    )
    print(f"{log.process(data3)}")

    print("\n=== Polymorphic Processing Demo ===\n")
    print("Processing multiple data types through same interface")
    demo1 = [4, 5, 8]
    demo2 = "Bye Nexus"
    demo3 = "INFO: System ready"
    print(f"Result 1: {numeric.process(demo1)}")
    print(f"Result 2: {text.process(demo2)}")
    print(f"Result 3: {log.process(demo3)}")


if __name__ == "__main__":
    main()
