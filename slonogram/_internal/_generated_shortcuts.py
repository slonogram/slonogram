# This file was automatically @generated via code_generation package
# Do not edit it directly
#
# Version: Bot API 6.9
# Changelog: https://core.telegram.org/bots/api#september-22-2023
# Release date: September 22, 2023
from slonogram.schemas import (
    InlineKeyboardMarkup,
    Message,
    ForceReply,
    InputMediaVideo,
    InputMediaDocument,
    ReplyKeyboardRemove,
    CallbackQuery,
    MessageEntity,
    InlineQueryResultsButton,
    ReplyKeyboardMarkup,
    InputMediaAudio,
    InputMediaPhoto,
    InlineQueryResult,
    InlineQuery,
)
from typing import Awaitable, TypeVar
from slonogram.abstract.context import AbstractContext
from types import EllipsisType
from io import IOBase

M = TypeVar("M")


class GeneratedShortcuts(AbstractContext[M]):
    def send_media_group(
        self: AbstractContext[Message],
        media: list[InputMediaAudio]
        | list[InputMediaDocument]
        | list[InputMediaPhoto]
        | list[InputMediaVideo],
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
    ) -> Awaitable[list[Message]]:
        """Alias to the `Bot.send_media_group` with usable defaults, for more, see `Bot.send_media_group` docs"""
        return self.rpc.send_media_group(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            media=media,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
        )

    def send_photo(
        self: AbstractContext[Message],
        photo: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_photo` with usable defaults, for more, see `Bot.send_photo` docs"""
        return self.rpc.send_photo(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            photo=photo,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_audio(
        self: AbstractContext[Message],
        audio: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        duration: int | None = None,
        performer: str | None = None,
        title: str | None = None,
        thumbnail: IOBase | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_audio` with usable defaults, for more, see `Bot.send_audio` docs"""
        return self.rpc.send_audio(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            audio=audio,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            performer=performer,
            title=title,
            thumbnail=thumbnail,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_document(
        self: AbstractContext[Message],
        document: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        thumbnail: IOBase | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        disable_content_type_detection: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_document` with usable defaults, for more, see `Bot.send_document` docs"""
        return self.rpc.send_document(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            document=document,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            disable_content_type_detection=disable_content_type_detection,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_video(
        self: AbstractContext[Message],
        video: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: IOBase | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        supports_streaming: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_video` with usable defaults, for more, see `Bot.send_video` docs"""
        return self.rpc.send_video(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            video=video,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            supports_streaming=supports_streaming,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_animation(
        self: AbstractContext[Message],
        animation: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        duration: int | None = None,
        width: int | None = None,
        height: int | None = None,
        thumbnail: IOBase | str | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        has_spoiler: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_animation` with usable defaults, for more, see `Bot.send_animation` docs"""
        return self.rpc.send_animation(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            animation=animation,
            duration=duration,
            width=width,
            height=height,
            thumbnail=thumbnail,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            has_spoiler=has_spoiler,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_voice(
        self: AbstractContext[Message],
        voice: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        caption: str | None = None,
        parse_mode: str | None = None,
        caption_entities: list[MessageEntity] | None = None,
        duration: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_voice` with usable defaults, for more, see `Bot.send_voice` docs"""
        return self.rpc.send_voice(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            voice=voice,
            caption=caption,
            parse_mode=parse_mode,
            caption_entities=caption_entities,
            duration=duration,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_video_note(
        self: AbstractContext[Message],
        video_note: IOBase | str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        duration: int | None = None,
        length: int | None = None,
        thumbnail: IOBase | str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_video_note` with usable defaults, for more, see `Bot.send_video_note` docs"""
        return self.rpc.send_video_note(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            video_note=video_note,
            duration=duration,
            length=length,
            thumbnail=thumbnail,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_location(
        self: AbstractContext[Message],
        latitude: float,
        longitude: float,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        horizontal_accuracy: float | None = None,
        live_period: int | None = None,
        heading: int | None = None,
        proximity_alert_radius: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_location` with usable defaults, for more, see `Bot.send_location` docs"""
        return self.rpc.send_location(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            latitude=latitude,
            longitude=longitude,
            horizontal_accuracy=horizontal_accuracy,
            live_period=live_period,
            heading=heading,
            proximity_alert_radius=proximity_alert_radius,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_venue(
        self: AbstractContext[Message],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        foursquare_id: str | None = None,
        foursquare_type: str | None = None,
        google_place_id: str | None = None,
        google_place_type: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_venue` with usable defaults, for more, see `Bot.send_venue` docs"""
        return self.rpc.send_venue(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            latitude=latitude,
            longitude=longitude,
            title=title,
            address=address,
            foursquare_id=foursquare_id,
            foursquare_type=foursquare_type,
            google_place_id=google_place_id,
            google_place_type=google_place_type,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_contact(
        self: AbstractContext[Message],
        phone_number: str,
        first_name: str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        last_name: str | None = None,
        vcard: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_contact` with usable defaults, for more, see `Bot.send_contact` docs"""
        return self.rpc.send_contact(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            vcard=vcard,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_poll(
        self: AbstractContext[Message],
        question: str,
        options: list[str],
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        is_anonymous: bool | None = None,
        type: str | None = None,
        allows_multiple_answers: bool | None = None,
        correct_option_id: int | None = None,
        explanation: str | None = None,
        explanation_parse_mode: str | None = None,
        explanation_entities: list[MessageEntity] | None = None,
        open_period: int | None = None,
        close_date: int | None = None,
        is_closed: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_poll` with usable defaults, for more, see `Bot.send_poll` docs"""
        return self.rpc.send_poll(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            question=question,
            options=options,
            is_anonymous=is_anonymous,
            type=type,
            allows_multiple_answers=allows_multiple_answers,
            correct_option_id=correct_option_id,
            explanation=explanation,
            explanation_parse_mode=explanation_parse_mode,
            explanation_entities=explanation_entities,
            open_period=open_period,
            close_date=close_date,
            is_closed=is_closed,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_dice(
        self: AbstractContext[Message],
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        emoji: str | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None = None,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_dice` with usable defaults, for more, see `Bot.send_dice` docs"""
        return self.rpc.send_dice(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            emoji=emoji,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def send_action(
        self: AbstractContext[Message],
        action: str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
    ) -> Awaitable[bool]:
        """Alias to the `Bot.send_chat_action` with usable defaults, for more, see `Bot.send_chat_action` docs"""
        return self.rpc.send_chat_action(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            action=action,
        )

    def reply(
        self: AbstractContext[Message],
        text: str,
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        parse_mode: str | None = None,
        entities: list[MessageEntity] | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None | EllipsisType = ...,
        allow_sending_without_reply: bool | None = None,
        reply_markup: InlineKeyboardMarkup
        | ReplyKeyboardMarkup
        | ReplyKeyboardRemove
        | ForceReply
        | None = None,
    ) -> Awaitable[Message]:
        """Alias to the `Bot.send_message` with usable defaults, for more, see `Bot.send_message` docs"""
        return self.rpc.send_message(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            text=text,
            parse_mode=parse_mode,
            entities=entities,
            disable_web_page_preview=disable_web_page_preview,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=self.model.message_id
            if reply_to_message_id is ...
            else reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
            reply_markup=reply_markup,
        )

    def reply_media_group(
        self: AbstractContext[Message],
        media: list[InputMediaAudio]
        | list[InputMediaDocument]
        | list[InputMediaPhoto]
        | list[InputMediaVideo],
        chat_id: int | str | EllipsisType = ...,
        message_thread_id: int | None = None,
        disable_notification: bool | None = None,
        protect_content: bool | None = None,
        reply_to_message_id: int | None | EllipsisType = ...,
        allow_sending_without_reply: bool | None = None,
    ) -> Awaitable[list[Message]]:
        """Alias to the `Bot.send_media_group` with usable defaults, for more, see `Bot.send_media_group` docs"""
        return self.rpc.send_media_group(
            chat_id=self.model.chat.id if chat_id is ... else chat_id,
            message_thread_id=message_thread_id,
            media=media,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=self.model.message_id
            if reply_to_message_id is ...
            else reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply,
        )

    def answer_callback(
        self: AbstractContext[CallbackQuery],
        callback_query_id: str | EllipsisType = ...,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None,
    ) -> Awaitable[bool]:
        """Alias to the `Bot.answer_callback_query` with usable defaults, for more, see `Bot.answer_callback_query` docs"""
        return self.rpc.answer_callback_query(
            callback_query_id=self.model.id
            if callback_query_id is ...
            else callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )

    def notify(
        self: AbstractContext[CallbackQuery],
        callback_query_id: str | EllipsisType = ...,
        text: str | None = None,
        show_alert: bool | None = None,
        url: str | None = None,
        cache_time: int | None = None,
    ) -> Awaitable[bool]:
        """Alias to the `Bot.answer_callback_query` with usable defaults, for more, see `Bot.answer_callback_query` docs"""
        return self.rpc.answer_callback_query(
            callback_query_id=self.model.id
            if callback_query_id is ...
            else callback_query_id,
            text=text,
            show_alert=show_alert,
            url=url,
            cache_time=cache_time,
        )

    def alert(
        self: AbstractContext[CallbackQuery],
        callback_query_id: str | EllipsisType = ...,
        text: str | None = None,
        show_alert: bool | None | EllipsisType = ...,
        url: str | None = None,
        cache_time: int | None = None,
    ) -> Awaitable[bool]:
        """Alias to the `Bot.answer_callback_query` with usable defaults, for more, see `Bot.answer_callback_query` docs"""
        return self.rpc.answer_callback_query(
            callback_query_id=self.model.id
            if callback_query_id is ...
            else callback_query_id,
            text=text,
            show_alert=True if show_alert is ... else show_alert,
            url=url,
            cache_time=cache_time,
        )

    def answer_inline(
        self: AbstractContext[InlineQuery],
        results: list[InlineQueryResult],
        inline_query_id: str | EllipsisType = ...,
        cache_time: int | None = None,
        is_personal: bool | None = None,
        next_offset: str | None = None,
        button: InlineQueryResultsButton | None = None,
    ) -> Awaitable[bool]:
        """Alias to the `Bot.answer_inline_query` with usable defaults, for more, see `Bot.answer_inline_query` docs"""
        return self.rpc.answer_inline_query(
            inline_query_id=self.model.id
            if inline_query_id is ...
            else inline_query_id,
            results=results,
            cache_time=cache_time,
            is_personal=is_personal,
            next_offset=next_offset,
            button=button,
        )
