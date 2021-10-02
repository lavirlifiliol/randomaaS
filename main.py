import os
from pathlib import Path
from random import Random

from ariadne import gql, QueryType, make_executable_schema, ObjectType
debug=os.environ.get('DEBUG', False)
if debug:
    from ariadne.asgi import GraphQL
else:
    from ariadne.wsgi import GraphQL

types = gql((Path(__file__).parent / 'randomaas.gql').read_text())
query = QueryType()
random_data = ObjectType('RandomData')


@query.field('random')
def resolve_random(parent, info, seed):
    return Random(seed)


@random_data.field('int')
def resolve_int(parent, info, min, max):
    return parent.randint(min, max)


@random_data.field('float')
def resolve_float(parent, info):
    return parent.random()


@random_data.field('floats')
def resolve_floats(parent, _, n):
    return [parent.random() for _ in range(n)]


@random_data.field('ints')
def resolve_floats(parent, _, n, min, max):
    return [parent.randint(min, max) for _ in range(n)]


@random_data.field('bits')
def resolve_bits(parent: Random, _, n):
    return bin(parent.getrandbits(n))[2:]


schema = make_executable_schema(types, query, random_data)
app = GraphQL(schema, debug=debug)
