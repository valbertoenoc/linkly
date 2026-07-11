# Linkly - Your fully featured self hosted URL Shortener.

## Description

An URL that you can self host.

## Motivation

While studying Systems Design in the past, I missed hands on projects content to solidify knowledge. So I decided to build a few projects that may serve educational content purposes, as well as be useful as self hosted and open source versions of existing known systems. 
This is the first one of many others.

## Roadmap

- [x] Core API (in-memory)	Base62, redirect logic, REST design
- [x] PostgreSQL persistence	SQLAlchemy, schema design
- [ ] Redis caching	Cache-aside, write-through, TTL
- [ ] Async click tracking	Queue, decoupling, eventual consistency
- [x] Load testing	Bottleneck identification, p99 latency
