from pathlib import Path
import os

from ariadne import gql, QueryType, make_executable_schema

types = gql((Path(__file__) / '../randomaas.schema').read_text())
query = QueryType()


@query.field('hello')
def resolve_hello(_, info):
    return f"Hello, {info.context['request'].headers.get('user-agent', 'NaN')}!"


schema = make_executable_schema(types, query)
if os.environ.get('DEBUG', False):
    from ariadne.asgi import GraphQL
    app = GraphQL(schema, debug=True)
else:
    from ariadne.wsgi import GraphQL
    app = GraphQL(schema, debug=False)