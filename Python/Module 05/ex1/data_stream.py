from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.processed_count: int = 0
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return (data_batch)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_count": self.processed_count,
            "stream_type": self.stream_type
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid Data")
            self.processed_count = len(data_batch)
            temps = [item.get("temp", 0.0) for item in data_batch if item.get
                     ("temp") is not None]
            avg_temp = sum(temps) / len(temps) if temps else 0.0
            result: str = (
                f"Sensor analysis: {self.processed_count} readings processed, "
                f"avg temp: {avg_temp:.1f}°C"
            )
            return result
        except Exception as e:
            return f"Error processing data: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria in ("high priority", "critical"):
            return [item for item in data_batch if item.get("temp", 0) > 25.0]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid Data")
            self.processed_count = len(data_batch)
            buy = [item.get("buy", 0) for item in data_batch]
            sell = [item.get("sell", 0) for item in data_batch]
            net = sum(buy) - sum(sell)
            result: str = (
                f"Transaction analysis: {self.processed_count} operations, "
                f"net flow: {net:+d} units"
            )
            return (result)
        except Exception as e:
            return f"Error processing data: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "large":
            return [
                item for item in data_batch if item.get("buy", 0) > 100 or
                item.get("sell", 0) > 100
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            if not isinstance(data_batch, list):
                raise ValueError("Invalid Data")
            self.processed_count = len(data_batch)
            errors = 0
            for item in data_batch:
                if item == "error":
                    errors += 1
            result: str = (f"Event analysis: {self.processed_count} events, "
                           f"{errors} error detected")
            return result
        except Exception as e:
            return f"Error processing data: {e}"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "error":
            return [item for item in data_batch if item == "error"]
        return super().filter_data(data_batch, criteria)


class StreamProcessor:
    def process_stream(
            self, stream: DataStream, data_batch: List[Any],
            criteria: Optional[str] = None) -> str:
        try:
            filtered = stream.filter_data(data_batch, criteria)
            return stream.process_batch(filtered)
        except Exception:
            return "Stream processing failed"


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    stats = sensor.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")
    sensor_data = [{"temp": 22.5}, {"humidity": 65}, {"pressure": 1013}]
    batch_str = ""
    for item in sensor_data:
        for key, val in item.items():
            batch_str += f"{key}:{val}, "
    batch_str = batch_str[:-2]
    print(f"Processing sensor batch: [{batch_str}]")
    print(sensor.process_batch(sensor_data))

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    stats = transaction.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")
    transaction_data = [{"buy": 100}, {"sell": 150}, {"buy": 75}]
    batch_str = ""
    for item in transaction_data:
        for key, val in item.items():
            batch_str += f"{key}:{val}, "
    batch_str = batch_str[:-2]
    print(f"Processing transaction batch: [{batch_str}]")
    print(transaction.process_batch(transaction_data))

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    stats = event.get_stats()
    print(f"Stream ID: {stats['stream_id']}, Type: {stats['stream_type']}")
    event_data = ["login", "error", "logout"]
    batch_str = ""
    for item in event_data:
        batch_str += f"{item}, "
    batch_str = batch_str[:-2]
    print(f"Processing event batch: [{batch_str}]")
    print(event.process_batch(event_data))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()

    print("Batch 1 Results:")

    processor.process_stream(sensor, [{"temp": 30.0}, {"temp": 20.0}])
    processor.process_stream(transaction, [{"buy": 200}, {"sell": 50},
                                           {"buy": 20}, {"sell": 10}])
    processor.process_stream(event, ["login", "error", "logout"])

    print(f"- Sensor data: {sensor.get_stats()['processed_count']} "
          "readings processed")
    print(f"- Transaction data: {transaction.get_stats()['processed_count']} "
          "operations processed")
    print(f"- Event data: {event.get_stats()['processed_count']} "
          "events processed")

    critical_data = [{"temp": 30.5}, {"temp": 18.0}, {"temp": 27.0},
                     {"temp": 15.0}]
    large_trans = [{"buy": 200}, {"sell": 50}, {"buy": 30}]

    critical_filtered = sensor.filter_data(critical_data, criteria="critical")
    large_filtered = transaction.filter_data(large_trans, criteria="large")

    print("\nStream filtering active: High-priority data only")
    print(f"Filtered results: {len(critical_filtered)} critical sensor "
          f"alerts, {len(large_filtered)} large transactions")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
