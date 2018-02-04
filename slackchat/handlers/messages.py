from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from markslack import MarkSlack
from slackchat.exceptions import (KeyValueError, KeywordArgumentNotFoundError,
                                  MessageNotFoundError, UserNotFoundError)
from slackchat.models import Channel, KeywordArgument, Message, User

marker = MarkSlack()

ignored_subtypes = [
    'group_join',
    'file_share',
    'group_archive',
]


def strptimestamp(timestamp):
    return datetime.fromtimestamp(float(timestamp))


def handle_removed(id, event):
    try:
        channel = Channel.objects.get(
            api_id=event.get('channel')
        )
    except ObjectDoesNotExist:
        return
    msg = {
        'user': event.get('previous_message').get('user'),
        'ts': event.get('previous_message').get('ts'),
        'text': event.get('message', {}).get('text', None)
    }
    user, created = User.objects.get_or_create(
        api_id=msg.get('user')
    )

    if event.get('previous_message', {}).get('thread_ts'):
        thread = event.get('previous_message')
        key, value = thread.get('text').split(': ', 1)

        try:
            original_message = Message.objects.get(
                timestamp=strptimestamp(thread.get('thread_ts'))
            )
        except ObjectDoesNotExist:
            raise MessageNotFoundError(
                '{}'.format(strptimestamp(thread.get('thread_ts')))
            )
        try:
            user = User.objects.get(api_id=thread.get('user'))
        except ObjectDoesNotExist:
            raise UserNotFoundError(thread.get('user'))
        try:
            kwarg = KeywordArgument.objects.get(
                timestamp=strptimestamp(thread.get('ts')),
                message=original_message,
                user=user
            )
        except ObjectDoesNotExist:
            raise KeywordArgumentNotFoundError(
                'KeywordArgument not found.'
            )
        kwarg.delete()
    else:
        Message.objects.get(
            channel=channel,
            timestamp=strptimestamp(msg.get('ts')),
            user=user,
        ).delete()


def handle(id, event):
    try:
        channel = Channel.objects.get(
            api_id=event.get('channel')
        )
    except ObjectDoesNotExist:
        return

    subtype = event.get('subtype', None)
    if subtype in ignored_subtypes:
        return

    if subtype:
        msg = {
            'user': event.get('previous_message').get('user'),
            'ts': event.get('previous_message').get('ts'),
            'text': event.get('message', {}).get('text', None)
        }
    else:
        msg = {
            'user': event.get('user'),
            'ts': event.get('ts'),
            'text': event.get('text')
        }

    user, created = User.objects.get_or_create(
        api_id=msg.get('user')
    )

    thread_ts = event.get('thread_ts', None) or \
        event.get('message', {}).get('thread_ts', None)
    if thread_ts and (
        event.get('parent_user_id', None) or
        event.get('message', {}).get('parent_user_id', None)
    ):
        try:
            text = msg.get('text')
            key, value = text.split(': ', 1)
        except Exception as e:
            raise KeyValueError('Could not split reply.')

        try:
            original_message = Message.objects.get(
                timestamp=strptimestamp(thread_ts)
            )
        except ObjectDoesNotExist:
            raise MessageNotFoundError(
                '{}'.format(strptimestamp(thread_ts))
            )
        KeywordArgument.objects.update_or_create(
            timestamp=strptimestamp(msg.get('ts')),
            message=original_message,
            user=user,
            defaults={
                "key": key,
                "value": value
            }
        )
    else:
        message, created = Message.objects.update_or_create(
            channel=channel,
            timestamp=strptimestamp(msg.get('ts')),
            user=user,
            defaults={
                'text': marker.mark(msg.get('text'))
            }
        )
