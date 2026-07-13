# Linkly - Your fully featured self hosted URL Shortener.

## Description

An URL Shortener that you can self host. A project that started as a learning tool, but evolved to be a production ready URL Shortener with analytics. Soon to have more features. 
It can be used for teaching purposes, or self hosting for you URL Shortening needs. 
It was designed with scalibity and development experience in mind.

## Motivation

While studying Systems Design in the past, I missed hands on projects content to solidify knowledge. So I decided to build a few projects that may serve educational content purposes, as well as be useful as self hosted and open source versions of existing known systems. 
This is the first one of many others.

## Quick Start

Docker is nicely setup with both the backend service as well as the postgres database server.
To spin up the server run:

```
docker compose up -d 
```

## Usage

If you want to spin up your own database, you can setup the `.env` file and run the fastapi server with 

```
uvicorn app.main:app --reload
```

To test out you can use an HTTP client like Bruno or Postman and send requests to the following endpoints:

### POST /shorten
{
"long_url": "http://www.google.com"
}

This will return your shortened URL as response.

### GET /{short_url}

This endpoint will use your shortened URL to redirect you to the corresponding long URL.

## Roadmap

- [x] Core API (in-memory)	Base62, redirect logic, REST design
- [x] PostgreSQL persistence	SQLAlchemy, schema design
- [ ] Redis caching	Cache-aside, write-through, TTL
- [ ] Async click tracking	Queue, decoupling, eventual consistency
- [x] Load testing	Bottleneck identification, p99 latency

## Contributing
