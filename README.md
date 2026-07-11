# Linkly - Your fully featured self hosted URL Shortener.

## Description

An URL that you can self host.

## Motivation

While studying System Design, I felt the need to implement a scalable version of a full system myself, along with scaling strategies with each new update.

## Roadmap

- [x] Core API (in-memory)	Base62, redirect logic, REST design
- [x] PostgreSQL persistence	SQLAlchemy, schema design
- [ ] Redis caching	Cache-aside, write-through, TTL
- [ ] Async click tracking	Queue, decoupling, eventual consistency
- [x] Load testing	Bottleneck identification, p99 latency
