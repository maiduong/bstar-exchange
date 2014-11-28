# RabbitMQ BSTAR Exchange Type

This exchange type is for Master/Slave behavior among consumers. It's basically 
a direct exchange, with the exception that, instead of each consumer bound 
to that exchange with the same routing key getting a copy of the message, 
the exchange type selects the first queue to route to.

### Installation

    git clone git://github.com/quantedge/bstar-exchange.git
    cd bstar-exchange
    make package
    cp dist/*.ez $RABBITMQ_HOME/plugins

### Usage

To use it, declare an exchange of type "x-bstar".

    Apache 2.0 Licensed:
    http://www.apache.org/licenses/LICENSE-2.0.html
