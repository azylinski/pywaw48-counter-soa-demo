# PyWaw#48 - Counter demo (SOA)
### http://pywaw.org/48/

Simple redis counter to demonstrate docker containers composition #SOA

### Install dependencies

Demo requires the following dependencies:

- docker (1.5+)
- docker-compose (1.2+)

### Getting started

- checkout repo: ```git clone https://github.com/azylinski/pywaw48-counter-soa-demo.git pywaw-48```
- enter folder: ```cd pywaw-48```
- [start docker daemon](https://docs.docker.com/reference/commandline/cli/#daemon) - ```docker -d```
- build & run an app: ```docker-compose up```
- view: http://127.0.0.1:8888/

### What's happening

There are 3 routes prepared on ```front``` service:
- http://127.0.0.1:8888/
- http://127.0.0.1:8888/sync
- http://127.0.0.1:8888/async

The first one will get current counter value. The other two, will increase redis key.

![demo-schema](https://cloud.githubusercontent.com/assets/493243/8180693/0cabfad2-1420-11e5-96eb-afab21f10ec0.png)

### Contact details

@ArturZylinski
artur@growbots.com
www.growbots.com
