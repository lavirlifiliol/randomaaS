import os
from pathlib import Path

from ariadne import gql, QueryType, make_executable_schema
from ariadne.wsgi import GraphQL

types = gql((Path(__file__).parent / 'randomaas.gql').read_text())
query = QueryType()


@query.field('hello')
def resolve_hello(*_):
    return f"Hello, World"


schema = make_executable_schema(types, query)
app = GraphQL(schema, debug=os.environ.get('DEBUG', False))
