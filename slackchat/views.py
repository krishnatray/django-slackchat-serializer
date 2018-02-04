from rest_framework import status
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from slackchat.conf import settings

from .handlers import (handle_message, handle_message_removed,
                       handle_reaction_added, handle_reaction_removed)


class Events(APIView):
    def post(self, request, *args, **kwargs):
        slack_message = request.data

        if slack_message.get('token') != settings.SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if slack_message.get('type') == 'url_verification':
            return Response(
                data=slack_message.get('challenge'),
                status=status.HTTP_200_OK
            )

        if 'event' in slack_message:
            id = slack_message.get('event_id')
            event = slack_message.get('event')

            if event.get('type') == 'message':
                if event.get('subtype', None) == 'message_deleted':
                    handle_message_removed(id, event)
                else:
                    handle_message(id, event)

            if event.get('type') == 'reaction_added':
                handle_reaction_added(id, event)

            if event.get('type') == 'reaction_removed':
                handle_reaction_removed(id, event)

        return Response(status=status.HTTP_200_OK)


class SwaggerSchemaView(APIView):
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)
