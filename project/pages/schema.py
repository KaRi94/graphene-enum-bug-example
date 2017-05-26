from graphene import AbstractType, relay
from graphene_django import DjangoObjectType

from project.pages.models import Page, SubPage


class PageNode(DjangoObjectType):
    class Meta:
        model = Page
        interfaces = (relay.Node, )


class SubPageNode(DjangoObjectType):
    class Meta:
        model = SubPage
        interfaces = (relay.Node, )


class Query(AbstractType):
    page = relay.Node.Field(PageNode)
    sub_page = relay.Node.Field(SubPageNode)
