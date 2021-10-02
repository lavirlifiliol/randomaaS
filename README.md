# A graphQL API for generating random values
A toy project for learning about graphQL APIs

When in debug mode, we use asgi so that we can use the uvicorn development server,
but in prod we use wsgi, as it has wider support. Feel free to adjust the code if you need asgi.