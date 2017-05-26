import graphene

from project.pages.schema import Query as PageQuery


class Query(graphene.ObjectType, PageQuery):

    class Meta:
        name = 'Viewer'
        interfaces = (graphene.relay.Node, )


schema = graphene.Schema(query=Query)
