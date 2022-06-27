# marketplace

Run a RabbitMQ server

```
docker run -it --rm --name marketplace_message_broker -p 5672:5672 -p 15672:15672 -d rabbitmq:3.10-management
```
