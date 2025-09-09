from typing import Optional

from confluent_kafka import Consumer, KafkaException, Message, TopicPartition

from config import config


def set_consumer_configs(config) -> None:
    """Set additional configurations for the Kafka consumer."""

    config["group.id"] = "hello_group"
    config["auto.offset.reset"] = "earliest"
    config["enable.auto.commit"] = False
    return config


def assignment_callback(consumer: Consumer, partitions: list[TopicPartition]) -> None:
    """Callback function triggered upon partition assignment.

    Args:
        consumer: The Kafka consumer instance.
        partitions: List of assigned TopicPartition instances.
    """

    for partition in partitions:
        print(f"Assigned to {partition.topic}, partition {partition.partition}")


if __name__ == "__main__":
    # Configure the consumer settings
    config = set_consumer_configs(config)

    # Initialize the Kafka consumer with the provided configuration
    consumer = Consumer(config)

    # Subscribe to the 'hello_topic' with an assignment callback
    consumer.subscribe(["hello_topic"], on_assign=assignment_callback)

    try:
        # Continuously poll for new messages
        while True:
            event: Optional[Message] = consumer.poll(timeout=1.0)

            # If no message is returned, continue polling
            if event is None:
                continue

            # Handle any errors in the received message
            if event.error():
                raise KafkaException(event.error())

            # Process and display the message content
            val = event.value().decode("utf-8")
            partition = event.partition()
            print(f"Received: {val} from partition {partition}")

            # Uncomment the following line to enable manual offset commits
            consumer.commit(event)

    except KeyboardInterrupt:
        # Handle graceful shutdown on user interruption
        print("Canceled by user.")

    finally:
        # Close the consumer to release resources
        consumer.close()
