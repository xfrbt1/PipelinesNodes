import logging

from kafka import KafkaConsumer

logger = logging.getLogger(__name__)


def subscribe_consumer(
    kafka_host: str | list[str],
    kafka_topic: str,
    group_id: str = "test-group",
) -> KafkaConsumer:

    try:
        consumer = KafkaConsumer(
            kafka_topic,
            bootstrap_servers=kafka_host,
            auto_offset_reset="earliest",
            group_id=group_id,
        )
        consumer.subscribe([kafka_topic])
        return consumer

    except Exception as ex:
        logger.exception(ex)
