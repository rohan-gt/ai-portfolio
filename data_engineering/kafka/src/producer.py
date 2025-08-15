from typing import Optional

from confluent_kafka import Producer, KafkaError, Message

from config import config


def callback(err: Optional[KafkaError], msg: Message) -> None:
    """
    Delivery report callback.

    Args:
        err (Optional[KafkaError]): The error that occurred, or None on success.
        msg (Message): The message that was produced or failed.
    """
    if err is not None:
        print(f"Produce to topic {msg.topic()} failed for event: {msg.key()}")
    else:
        val = msg.value().decode("utf-8")
        print(f"{val} sent to partition {msg.partition()}.")


def say_hello(producer: Producer, key: str) -> None:
    """
    Produce a message to the 'hello_topic' with a key.

    Args:
        producer (Producer): The Kafka producer instance.
        key (str): The key for the message.
    """
    value = f"Hello {key}!"
    producer.produce("hello_topic", value=value, key=key, on_delivery=callback)


if __name__ == "__main__":

    # Initialize the Kafka producer with the loaded configuration
    producer = Producer(config)

    # List of keys to send messages for
    keys = ["Amy", "Brenda", "Cindy", "Derrick", "Elaine", "Fred"]

    # Produce messages for each key
    [say_hello(producer, key) for key in keys]

    # Wait for any outstanding messages to be delivered and delivery reports to be received
    producer.flush()
