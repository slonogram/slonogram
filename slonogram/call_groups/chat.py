# flake8: noqa
from typing import Awaitable, Optional, List, IO
from slonogram import schemas
from slonogram.types.api_session import ApiSession
from slonogram.utils.json import dumps


class ChatCallGroup:
    __slots__ = ("_session",)

    def __init__(self, session: ApiSession) -> None:
        self._session = session

    def send_action(
        self,
        chat_id: int | str,
        action: str,
        message_thread_id: Optional[int] = None,
    ) -> Awaitable[bool]:
        """
        Use this method when you need to tell the user that something is
        happening on the bot's side. The status is set for 5 seconds or
        less (when a message arrives from your bot, Telegram clients
        clear its typing status). Returns True on success. We only
        recommend using this method when a response from the bot will
        take a noticeable amount of time to arrive. for more:
        https://core.telegram.org/bots/api#sendchataction
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread; supergroups only
        :param action: Type of action to broadcast. Choose one,
                       depending on what the user is about to
                       receive: typing for text messages,
                       upload_photo for photos, record_video or
                       upload_video for videos, record_voice or
                       upload_voice for voice notes, upload_document
                       for general files, choose_sticker for
                       stickers, find_location for location data,
                       record_video_note or upload_video_note for
                       video notes.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "action": action}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        return self._session.call_method(bool, "sendChatAction", params)

    def send_message(
        self,
        chat_id: int | str,
        text: str,
        message_thread_id: Optional[int] = None,
        parse_mode: Optional[schemas.ParseMode] = None,
        entities: Optional[List[schemas.MessageEntity]] = None,
        disable_web_page_preview: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send text messages. On success, the sent
        Message is returned. for more:
        https://core.telegram.org/bots/api#sendmessage
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param text: Text of the message to be sent, 1-4096
                     characters after entities parsing
        :param parse_mode: Mode for parsing entities in the message
                           text. See formatting options for more
                           details.
        :param entities: A JSON-serialized list of special entities
                         that appear in message text, which can be
                         specified instead of parse_mode
        :param disable_web_page_preview: Disables link previews for
                                         links in this message
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "text": text}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if entities is not None:
            params["entities"] = dumps(self._session.retort.dump(entities))

        if disable_web_page_preview is not None:
            params["disable_web_page_preview"] = disable_web_page_preview

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = dumps(
                self._session.retort.dump(reply_markup)
            )

        return self._session.call_method(
            schemas.Message, "sendMessage", params
        )

    def forward_message(
        self,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to forward messages of any kind. Service messages
        can't be forwarded. On success, the sent Message is returned. for
        more: https://core.telegram.org/bots/api#forwardmessage
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param from_chat_id: Unique identifier for the chat where
                             the original message was sent (or
                             channel username in the format
                             @channelusername)
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the
                                forwarded message from forwarding
                                and saving
        :param message_id: Message identifier in the chat specified
                           in from_chat_id
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
        }
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        return self._session.call_method(
            schemas.Message, "forwardMessage", params
        )

    def copy_message(
        self,
        chat_id: int | str,
        from_chat_id: int | str,
        message_id: int,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.MessageId]:
        """
        Use this method to copy messages of any kind. Service messages
        and invoice messages can't be copied. A quiz poll can be copied
        only if the value of the field correct_option_id is known to the
        bot. The method is analogous to the method forwardMessage, but
        the copied message doesn't have a link to the original message.
        Returns the MessageId of the sent message on success. for more:
        https://core.telegram.org/bots/api#copymessage
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param from_chat_id: Unique identifier for the chat where
                             the original message was sent (or
                             channel username in the format
                             @channelusername)
        :param message_id: Message identifier in the chat specified
                           in from_chat_id
        :param caption: New caption for media, 0-1024 characters
                        after entities parsing. If not specified,
                        the original caption is kept
        :param parse_mode: Mode for parsing entities in the new
                           caption. See formatting options for more
                           details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the new
                                 caption, which can be specified
                                 instead of parse_mode
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "from_chat_id": from_chat_id,
            "message_id": message_id,
        }
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.MessageId, "copyMessage", params
        )

    def send_photo(
        self,
        chat_id: int | str,
        photo: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send photos. On success, the sent Message is
        returned. for more: https://core.telegram.org/bots/api#sendphoto
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param photo: Photo to send. Pass a file_id as String to
                      send a photo that exists on the Telegram
                      servers (recommended), pass an HTTP URL as a
                      String for Telegram to get a photo from the
                      Internet, or upload a new photo using
                      multipart/form-data. The photo must be at most
                      10 MB in size. The photo's width and height
                      must not exceed 10000 in total. Width and
                      height ratio must be at most 20. More
                      information on Sending Files:
                      https://core.telegram.org/bots/api#sending-
                      files
        :param caption: Photo caption (may also be used when
                        resending photos by file_id), 0-1024
                        characters after entities parsing
        :param parse_mode: Mode for parsing entities in the photo
                           caption. See formatting options for more
                           details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the
                                 caption, which can be specified
                                 instead of parse_mode
        :param has_spoiler: Pass True if the photo needs to be
                            covered with a spoiler animation
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "photo": photo}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if has_spoiler is not None:
            params["has_spoiler"] = has_spoiler

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendPhoto", params
        )

    def send_audio(
        self,
        chat_id: int | str,
        audio: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumbnail: Optional[IO[bytes] | str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send audio files, if you want Telegram clients
        to display them in the music player. Your audio must be in the
        .MP3 or .M4A format. On success, the sent Message is returned.
        Bots can currently send audio files of up to 50 MB in size, this
        limit may be changed in the future. For sending voice messages,
        use the sendVoice method instead. for more:
        https://core.telegram.org/bots/api#sendaudio
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param audio: Audio file to send. Pass a file_id as String
                      to send an audio file that exists on the
                      Telegram servers (recommended), pass an HTTP
                      URL as a String for Telegram to get an audio
                      file from the Internet, or upload a new one
                      using multipart/form-data. More information on
                      Sending Files:
                      https://core.telegram.org/bots/api#sending-
                      files
        :param caption: Audio caption, 0-1024 characters after
                        entities parsing
        :param parse_mode: Mode for parsing entities in the audio
                           caption. See formatting options for more
                           details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the
                                 caption, which can be specified
                                 instead of parse_mode
        :param duration: Duration of the audio in seconds
        :param performer: Performer
        :param title: Track name
        :param thumbnail: Thumbnail of the file sent; can be ignored
                          if thumbnail generation for the file is
                          supported server-side. The thumbnail
                          should be in JPEG format and less than 200
                          kB in size. A thumbnail's width and height
                          should not exceed 320. Ignored if the file
                          is not uploaded using multipart/form-data.
                          Thumbnails can't be reused and can be only
                          uploaded as a new file, so you can pass
                          "attach://<file_attach_name>" if the
                          thumbnail was uploaded using
                          multipart/form-data under
                          <file_attach_name>. More information on
                          Sending Files: https://core.telegram.org/b
                          ots/api#sending-files
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "audio": audio}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if duration is not None:
            params["duration"] = duration

        if performer is not None:
            params["performer"] = performer

        if title is not None:
            params["title"] = title

        if thumbnail is not None:
            params["thumbnail"] = thumbnail

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendAudio", params
        )

    def send_document(
        self,
        chat_id: int | str,
        document: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        thumbnail: Optional[IO[bytes] | str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send general files. On success, the sent
        Message is returned. Bots can currently send files of any type of
        up to 50 MB in size, this limit may be changed in the future. for
        more: https://core.telegram.org/bots/api#senddocument
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param document: File to send. Pass a file_id as String to
                         send a file that exists on the Telegram
                         servers (recommended), pass an HTTP URL as
                         a String for Telegram to get a file from
                         the Internet, or upload a new one using
                         multipart/form-data. More information on
                         Sending Files:
                         https://core.telegram.org/bots/api#sending-
                         files
        :param thumbnail: Thumbnail of the file sent; can be ignored
                          if thumbnail generation for the file is
                          supported server-side. The thumbnail
                          should be in JPEG format and less than 200
                          kB in size. A thumbnail's width and height
                          should not exceed 320. Ignored if the file
                          is not uploaded using multipart/form-data.
                          Thumbnails can't be reused and can be only
                          uploaded as a new file, so you can pass
                          "attach://<file_attach_name>" if the
                          thumbnail was uploaded using
                          multipart/form-data under
                          <file_attach_name>. More information on
                          Sending Files: https://core.telegram.org/b
                          ots/api#sending-files
        :param caption: Document caption (may also be used when
                        resending documents by file_id), 0-1024
                        characters after entities parsing
        :param parse_mode: Mode for parsing entities in the document
                           caption. See formatting options for more
                           details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the
                                 caption, which can be specified
                                 instead of parse_mode
        :param disable_content_type_detection: Disables automatic
                                               server-side content
                                               type detection for
                                               files uploaded using
                                               multipart/form-data
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "document": document}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if thumbnail is not None:
            params["thumbnail"] = thumbnail

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if disable_content_type_detection is not None:
            params[
                "disable_content_type_detection"
            ] = disable_content_type_detection

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendDocument", params
        )

    def send_video(
        self,
        chat_id: int | str,
        video: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[IO[bytes] | str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send video files, Telegram clients support
        MPEG4 videos (other formats may be sent as Document). On success,
        the sent Message is returned. Bots can currently send video files
        of up to 50 MB in size, this limit may be changed in the future.
        for more: https://core.telegram.org/bots/api#sendvideo
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param video: Video to send. Pass a file_id as String to
                      send a video that exists on the Telegram
                      servers (recommended), pass an HTTP URL as a
                      String for Telegram to get a video from the
                      Internet, or upload a new video using
                      multipart/form-data. More information on
                      Sending Files:
                      https://core.telegram.org/bots/api#sending-
                      files
        :param duration: Duration of sent video in seconds
        :param width: Video width
        :param height: Video height
        :param thumbnail: Thumbnail of the file sent; can be ignored
                          if thumbnail generation for the file is
                          supported server-side. The thumbnail
                          should be in JPEG format and less than 200
                          kB in size. A thumbnail's width and height
                          should not exceed 320. Ignored if the file
                          is not uploaded using multipart/form-data.
                          Thumbnails can't be reused and can be only
                          uploaded as a new file, so you can pass
                          "attach://<file_attach_name>" if the
                          thumbnail was uploaded using
                          multipart/form-data under
                          <file_attach_name>. More information on
                          Sending Files: https://core.telegram.org/b
                          ots/api#sending-files
        :param caption: Video caption (may also be used when
                        resending videos by file_id), 0-1024
                        characters after entities parsing
        :param parse_mode: Mode for parsing entities in the video
                           caption. See formatting options for more
                           details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the
                                 caption, which can be specified
                                 instead of parse_mode
        :param has_spoiler: Pass True if the video needs to be
                            covered with a spoiler animation
        :param supports_streaming: Pass True if the uploaded video
                                   is suitable for streaming
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "video": video}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if duration is not None:
            params["duration"] = duration

        if width is not None:
            params["width"] = width

        if height is not None:
            params["height"] = height

        if thumbnail is not None:
            params["thumbnail"] = thumbnail

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if has_spoiler is not None:
            params["has_spoiler"] = has_spoiler

        if supports_streaming is not None:
            params["supports_streaming"] = supports_streaming

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendVideo", params
        )

    def send_animation(
        self,
        chat_id: int | str,
        animation: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[IO[bytes] | str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send animation files (GIF or H.264/MPEG-4 AVC
        video without sound). On success, the sent Message is returned.
        Bots can currently send animation files of up to 50 MB in size,
        this limit may be changed in the future. for more:
        https://core.telegram.org/bots/api#sendanimation
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param animation: Animation to send. Pass a file_id as
                          String to send an animation that exists on
                          the Telegram servers (recommended), pass
                          an HTTP URL as a String for Telegram to
                          get an animation from the Internet, or
                          upload a new animation using
                          multipart/form-data. More information on
                          Sending Files: https://core.telegram.org/b
                          ots/api#sending-files
        :param duration: Duration of sent animation in seconds
        :param width: Animation width
        :param height: Animation height
        :param thumbnail: Thumbnail of the file sent; can be ignored
                          if thumbnail generation for the file is
                          supported server-side. The thumbnail
                          should be in JPEG format and less than 200
                          kB in size. A thumbnail's width and height
                          should not exceed 320. Ignored if the file
                          is not uploaded using multipart/form-data.
                          Thumbnails can't be reused and can be only
                          uploaded as a new file, so you can pass
                          "attach://<file_attach_name>" if the
                          thumbnail was uploaded using
                          multipart/form-data under
                          <file_attach_name>. More information on
                          Sending Files: https://core.telegram.org/b
                          ots/api#sending-files
        :param caption: Animation caption (may also be used when
                        resending animation by file_id), 0-1024
                        characters after entities parsing
        :param parse_mode: Mode for parsing entities in the
                           animation caption. See formatting options
                           for more details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the
                                 caption, which can be specified
                                 instead of parse_mode
        :param has_spoiler: Pass True if the animation needs to be
                            covered with a spoiler animation
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "animation": animation}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if duration is not None:
            params["duration"] = duration

        if width is not None:
            params["width"] = width

        if height is not None:
            params["height"] = height

        if thumbnail is not None:
            params["thumbnail"] = thumbnail

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if has_spoiler is not None:
            params["has_spoiler"] = has_spoiler

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendAnimation", params
        )

    def send_voice(
        self,
        chat_id: int | str,
        voice: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[schemas.MessageEntity]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send audio files, if you want Telegram clients
        to display the file as a playable voice message. For this to
        work, your audio must be in an .OGG file encoded with OPUS (other
        formats may be sent as Audio or Document). On success, the sent
        Message is returned. Bots can currently send voice messages of up
        to 50 MB in size, this limit may be changed in the future. for
        more: https://core.telegram.org/bots/api#sendvoice
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param voice: Audio file to send. Pass a file_id as String
                      to send a file that exists on the Telegram
                      servers (recommended), pass an HTTP URL as a
                      String for Telegram to get a file from the
                      Internet, or upload a new one using
                      multipart/form-data. More information on
                      Sending Files:
                      https://core.telegram.org/bots/api#sending-
                      files
        :param caption: Voice message caption, 0-1024 characters
                        after entities parsing
        :param parse_mode: Mode for parsing entities in the voice
                           message caption. See formatting options
                           for more details.
        :param caption_entities: A JSON-serialized list of special
                                 entities that appear in the
                                 caption, which can be specified
                                 instead of parse_mode
        :param duration: Duration of the voice message in seconds
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "voice": voice}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if caption is not None:
            params["caption"] = caption

        if parse_mode is not None:
            params["parse_mode"] = parse_mode

        if caption_entities is not None:
            params["caption_entities"] = caption_entities

        if duration is not None:
            params["duration"] = duration

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendVoice", params
        )

    def send_video_note(
        self,
        chat_id: int | str,
        video_note: IO[bytes] | str,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumbnail: Optional[IO[bytes] | str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        As of v.4.0, Telegram clients support rounded square MPEG4 videos
        of up to 1 minute long. Use this method to send video messages.
        On success, the sent Message is returned. for more:
        https://core.telegram.org/bots/api#sendvideonote
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param video_note: Video note to send. Pass a file_id as
                           String to send a video note that exists
                           on the Telegram servers (recommended) or
                           upload a new video using multipart/form-
                           data. More information on Sending Files:
                           https://core.telegram.org/bots/api#sendin
                           g-files. Sending video notes by a URL is
                           currently unsupported
        :param duration: Duration of sent video in seconds
        :param length: Video width and height, i.e. diameter of the
                       video message
        :param thumbnail: Thumbnail of the file sent; can be ignored
                          if thumbnail generation for the file is
                          supported server-side. The thumbnail
                          should be in JPEG format and less than 200
                          kB in size. A thumbnail's width and height
                          should not exceed 320. Ignored if the file
                          is not uploaded using multipart/form-data.
                          Thumbnails can't be reused and can be only
                          uploaded as a new file, so you can pass
                          "attach://<file_attach_name>" if the
                          thumbnail was uploaded using
                          multipart/form-data under
                          <file_attach_name>. More information on
                          Sending Files: https://core.telegram.org/b
                          ots/api#sending-files
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "video_note": video_note}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if duration is not None:
            params["duration"] = duration

        if length is not None:
            params["length"] = length

        if thumbnail is not None:
            params["thumbnail"] = thumbnail

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendVideoNote", params
        )

    def send_media_group(
        self,
        chat_id: int | str,
        media: List[schemas.InputMediaAudio]
        | List[schemas.InputMediaDocument]
        | List[schemas.InputMediaPhoto]
        | List[schemas.InputMediaVideo],
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
    ) -> Awaitable[List[schemas.Message]]:
        """
        Use this method to send a group of photos, videos, documents or
        audios as an album. Documents and audio files can be only grouped
        in an album with messages of the same type. On success, an array
        of Messages that were sent is returned. for more:
        https://core.telegram.org/bots/api#sendmediagroup
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param media: A JSON-serialized array describing messages to
                      be sent, must include 2-10 items
        :param disable_notification: Sends messages silently. Users
                                     will receive a notification
                                     with no sound.
        :param protect_content: Protects the contents of the sent
                                messages from forwarding and saving
        :param reply_to_message_id: If the messages are a reply, ID
                                    of the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "media": media}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        return self._session.call_method(
            List[schemas.Message], "sendMediaGroup", params
        )

    def send_location(
        self,
        chat_id: int | str,
        latitude: float,
        longitude: float,
        message_thread_id: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send point on the map. On success, the sent
        Message is returned. for more:
        https://core.telegram.org/bots/api#sendlocation
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param latitude: Latitude of the location
        :param longitude: Longitude of the location
        :param horizontal_accuracy: The radius of uncertainty for
                                    the location, measured in
                                    meters; 0-1500
        :param live_period: Period in seconds for which the location
                            will be updated (see Live Locations,
                            should be between 60 and 86400.
        :param heading: For live locations, a direction in which the
                        user is moving, in degrees. Must be between
                        1 and 360 if specified.
        :param proximity_alert_radius: For live locations, a maximum
                                       distance for proximity alerts
                                       about approaching another
                                       chat member, in meters. Must
                                       be between 1 and 100000 if
                                       specified.
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
        }
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if horizontal_accuracy is not None:
            params["horizontal_accuracy"] = horizontal_accuracy

        if live_period is not None:
            params["live_period"] = live_period

        if heading is not None:
            params["heading"] = heading

        if proximity_alert_radius is not None:
            params["proximity_alert_radius"] = proximity_alert_radius

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendLocation", params
        )

    def send_venue(
        self,
        chat_id: int | str,
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        message_thread_id: Optional[int] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send information about a venue. On success,
        the sent Message is returned. for more:
        https://core.telegram.org/bots/api#sendvenue
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param latitude: Latitude of the venue
        :param longitude: Longitude of the venue
        :param title: Name of the venue
        :param address: Address of the venue
        :param foursquare_id: Foursquare identifier of the venue
        :param foursquare_type: Foursquare type of the venue, if
                                known. (For example,
                                "arts_entertainment/default",
                                "arts_entertainment/aquarium" or
                                "food/icecream".)
        :param google_place_id: Google Places identifier of the
                                venue
        :param google_place_type: Google Places type of the venue.
                                  (See supported types.)
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "latitude": latitude,
            "longitude": longitude,
            "title": title,
            "address": address,
        }
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if foursquare_id is not None:
            params["foursquare_id"] = foursquare_id

        if foursquare_type is not None:
            params["foursquare_type"] = foursquare_type

        if google_place_id is not None:
            params["google_place_id"] = google_place_id

        if google_place_type is not None:
            params["google_place_type"] = google_place_type

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendVenue", params
        )

    def send_contact(
        self,
        chat_id: int | str,
        phone_number: str,
        first_name: str,
        message_thread_id: Optional[int] = None,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send phone contacts. On success, the sent
        Message is returned. for more:
        https://core.telegram.org/bots/api#sendcontact
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param phone_number: Contact's phone number
        :param first_name: Contact's first name
        :param last_name: Contact's last name
        :param vcard: Additional data about the contact in the form
                      of a vCard, 0-2048 bytes
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "phone_number": phone_number,
            "first_name": first_name,
        }
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if last_name is not None:
            params["last_name"] = last_name

        if vcard is not None:
            params["vcard"] = vcard

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendContact", params
        )

    def send_poll(
        self,
        chat_id: int | str,
        question: str,
        options: List[str],
        message_thread_id: Optional[int] = None,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[List[schemas.MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send a native poll. On success, the sent
        Message is returned. for more:
        https://core.telegram.org/bots/api#sendpoll
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param question: Poll question, 1-300 characters
        :param options: A JSON-serialized list of answer options,
                        2-10 strings 1-100 characters each
        :param is_anonymous: True, if the poll needs to be
                             anonymous, defaults to True
        :param type: Poll type, "quiz" or "regular", defaults to
                     "regular"
        :param allows_multiple_answers: True, if the poll allows
                                        multiple answers, ignored
                                        for polls in quiz mode,
                                        defaults to False
        :param correct_option_id: 0-based identifier of the correct
                                  answer option, required for polls
                                  in quiz mode
        :param explanation: Text that is shown when a user chooses
                            an incorrect answer or taps on the lamp
                            icon in a quiz-style poll, 0-200
                            characters with at most 2 line feeds
                            after entities parsing
        :param explanation_parse_mode: Mode for parsing entities in
                                       the explanation. See
                                       formatting options for more
                                       details.
        :param explanation_entities: A JSON-serialized list of
                                     special entities that appear in
                                     the poll explanation, which can
                                     be specified instead of
                                     parse_mode
        :param open_period: Amount of time in seconds the poll will
                            be active after creation, 5-600. Can't
                            be used together with close_date.
        :param close_date: Point in time (Unix timestamp) when the
                           poll will be automatically closed. Must
                           be at least 5 and no more than 600
                           seconds in the future. Can't be used
                           together with open_period.
        :param is_closed: Pass True if the poll needs to be
                          immediately closed. This can be useful for
                          poll preview.
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "question": question,
            "options": options,
        }
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if is_anonymous is not None:
            params["is_anonymous"] = is_anonymous

        if type is not None:
            params["type"] = type

        if allows_multiple_answers is not None:
            params["allows_multiple_answers"] = allows_multiple_answers

        if correct_option_id is not None:
            params["correct_option_id"] = correct_option_id

        if explanation is not None:
            params["explanation"] = explanation

        if explanation_parse_mode is not None:
            params["explanation_parse_mode"] = explanation_parse_mode

        if explanation_entities is not None:
            params["explanation_entities"] = explanation_entities

        if open_period is not None:
            params["open_period"] = open_period

        if close_date is not None:
            params["close_date"] = close_date

        if is_closed is not None:
            params["is_closed"] = is_closed

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendPoll", params
        )

    def send_dice(
        self,
        chat_id: int | str,
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        reply_to_message_id: Optional[int] = None,
        allow_sending_without_reply: Optional[bool] = None,
        reply_markup: Optional[
            schemas.InlineKeyboardMarkup
            | schemas.ReplyKeyboardMarkup
            | schemas.ReplyKeyboardRemove
            | schemas.ForceReply
        ] = None,
    ) -> Awaitable[schemas.Message]:
        """
        Use this method to send an animated emoji that will display a
        random value. On success, the sent Message is returned. for more:
        https://core.telegram.org/bots/api#senddice
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_thread_id: Unique identifier for the target
                                  message thread (topic) of the
                                  forum; for forum supergroups only
        :param emoji: Emoji on which the dice throw animation is
                      based. Currently, must be one of "🎲", "🎯",
                      "🏀", "⚽", "🎳", or "🎰". Dice can have values
                      1-6 for "🎲", "🎯" and "🎳", values 1-5 for "🏀"
                      and "⚽", and values 1-64 for "🎰". Defaults to
                      "🎲"
        :param disable_notification: Sends the message silently.
                                     Users will receive a
                                     notification with no sound.
        :param protect_content: Protects the contents of the sent
                                message from forwarding
        :param reply_to_message_id: If the message is a reply, ID of
                                    the original message
        :param allow_sending_without_reply: Pass True if the message
                                            should be sent even if
                                            the specified replied-to
                                            message is not found
        :param reply_markup: Additional interface options. A JSON-
                             serialized object for an inline
                             keyboard, custom reply keyboard,
                             instructions to remove reply keyboard
                             or to force a reply from the user.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}
        if message_thread_id is not None:
            params["message_thread_id"] = message_thread_id

        if emoji is not None:
            params["emoji"] = emoji

        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        if protect_content is not None:
            params["protect_content"] = protect_content

        if reply_to_message_id is not None:
            params["reply_to_message_id"] = reply_to_message_id

        if allow_sending_without_reply is not None:
            params[
                "allow_sending_without_reply"
            ] = allow_sending_without_reply

        if reply_markup is not None:
            params["reply_markup"] = reply_markup

        return self._session.call_method(
            schemas.Message, "sendDice", params
        )

    def ban(
        self,
        chat_id: int | str,
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to ban a user in a group, a supergroup or a
        channel. In the case of supergroups and channels, the user will
        not be able to return to the chat on their own using invite
        links, etc., unless unbanned first. The bot must be an
        administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns True on success. for
        more: https://core.telegram.org/bots/api#banchatmember
        :param chat_id: Unique identifier for the target group or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :param until_date: Date when the user will be unbanned, unix
                           time. If user is banned for more than 366
                           days or less than 30 seconds from the
                           current time they are considered to be
                           banned forever. Applied for supergroups
                           and channels only.
        :param revoke_messages: Pass True to delete all messages
                                from the chat for the user that is
                                being removed. If False, the user
                                will be able to see messages in the
                                group that were sent before the user
                                was removed. Always True for
                                supergroups and channels.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "user_id": user_id}
        if until_date is not None:
            params["until_date"] = until_date

        if revoke_messages is not None:
            params["revoke_messages"] = revoke_messages

        return self._session.call_method(bool, "banChatMember", params)

    def unban(
        self,
        chat_id: int | str,
        user_id: int,
        only_if_banned: Optional[bool] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to unban a previously banned user in a supergroup
        or channel. The user will not return to the group or channel
        automatically, but will be able to join via link, etc. The bot
        must be an administrator for this to work. By default, this
        method guarantees that after the call the user is not a member of
        the chat, but will be able to join it. So if the user is a member
        of the chat they will also be removed from the chat. If you don't
        want this, use the parameter only_if_banned. Returns True on
        success. for more:
        https://core.telegram.org/bots/api#unbanchatmember
        :param chat_id: Unique identifier for the target group or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :param only_if_banned: Do nothing if the user is not banned
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "user_id": user_id}
        if only_if_banned is not None:
            params["only_if_banned"] = only_if_banned

        return self._session.call_method(bool, "unbanChatMember", params)

    def restrict_user(
        self,
        chat_id: int | str,
        user_id: int,
        permissions: schemas.ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
        until_date: Optional[int] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to restrict a user in a supergroup. The bot must
        be an administrator in the supergroup for this to work and must
        have the appropriate administrator rights. Pass True for all
        permissions to lift restrictions from a user. Returns True on
        success. for more:
        https://core.telegram.org/bots/api#restrictchatmember
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup (in the
                        format @supergroupusername)
        :param user_id: Unique identifier of the target user
        :param permissions: A JSON-serialized object for new user
                            permissions
        :param use_independent_chat_permissions: Pass True if chat
                                                 permissions are set
                                                 independently.
                                                 Otherwise, the can_
                                                 send_other_messages
                                                 and can_add_web_pag
                                                 e_previews
                                                 permissions will
                                                 imply the
                                                 can_send_messages,
                                                 can_send_audios,
                                                 can_send_documents,
                                                 can_send_photos,
                                                 can_send_videos, ca
                                                 n_send_video_notes,
                                                 and can_send_voice_
                                                 notes permissions;
                                                 the can_send_polls
                                                 permission will
                                                 imply the
                                                 can_send_messages
                                                 permission.
        :param until_date: Date when restrictions will be lifted for
                           the user, unix time. If user is
                           restricted for more than 366 days or less
                           than 30 seconds from the current time,
                           they are considered to be restricted
                           forever
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "user_id": user_id,
            "permissions": permissions,
        }
        if use_independent_chat_permissions is not None:
            params[
                "use_independent_chat_permissions"
            ] = use_independent_chat_permissions

        if until_date is not None:
            params["until_date"] = until_date

        return self._session.call_method(
            bool, "restrictChatMember", params
        )

    def promote(
        self,
        chat_id: int | str,
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to promote or demote a user in a supergroup or a
        channel. The bot must be an administrator in the chat for this to
        work and must have the appropriate administrator rights. Pass
        False for all boolean parameters to demote a user. Returns True
        on success. for more:
        https://core.telegram.org/bots/api#promotechatmember
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param user_id: Unique identifier of the target user
        :param is_anonymous: Pass True if the administrator's
                             presence in the chat is hidden
        :param can_manage_chat: Pass True if the administrator can
                                access the chat event log, chat
                                statistics, message statistics in
                                channels, see channel members, see
                                anonymous administrators in
                                supergroups and ignore slow mode.
                                Implied by any other administrator
                                privilege
        :param can_post_messages: Pass True if the administrator can
                                  create channel posts, channels
                                  only
        :param can_edit_messages: Pass True if the administrator can
                                  edit messages of other users and
                                  can pin messages, channels only
        :param can_delete_messages: Pass True if the administrator
                                    can delete messages of other
                                    users
        :param can_manage_video_chats: Pass True if the
                                       administrator can manage
                                       video chats
        :param can_restrict_members: Pass True if the administrator
                                     can restrict, ban or unban chat
                                     members
        :param can_promote_members: Pass True if the administrator
                                    can add new administrators with
                                    a subset of their own privileges
                                    or demote administrators that
                                    they have promoted, directly or
                                    indirectly (promoted by
                                    administrators that were
                                    appointed by him)
        :param can_change_info: Pass True if the administrator can
                                change chat title, photo and other
                                settings
        :param can_invite_users: Pass True if the administrator can
                                 invite new users to the chat
        :param can_pin_messages: Pass True if the administrator can
                                 pin messages, supergroups only
        :param can_manage_topics: Pass True if the user is allowed
                                  to create, rename, close, and
                                  reopen forum topics, supergroups
                                  only
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "user_id": user_id}
        if is_anonymous is not None:
            params["is_anonymous"] = is_anonymous

        if can_manage_chat is not None:
            params["can_manage_chat"] = can_manage_chat

        if can_post_messages is not None:
            params["can_post_messages"] = can_post_messages

        if can_edit_messages is not None:
            params["can_edit_messages"] = can_edit_messages

        if can_delete_messages is not None:
            params["can_delete_messages"] = can_delete_messages

        if can_manage_video_chats is not None:
            params["can_manage_video_chats"] = can_manage_video_chats

        if can_restrict_members is not None:
            params["can_restrict_members"] = can_restrict_members

        if can_promote_members is not None:
            params["can_promote_members"] = can_promote_members

        if can_change_info is not None:
            params["can_change_info"] = can_change_info

        if can_invite_users is not None:
            params["can_invite_users"] = can_invite_users

        if can_pin_messages is not None:
            params["can_pin_messages"] = can_pin_messages

        if can_manage_topics is not None:
            params["can_manage_topics"] = can_manage_topics

        return self._session.call_method(bool, "promoteChatMember", params)

    def set_custom_title(
        self, chat_id: int | str, user_id: int, custom_title: str
    ) -> Awaitable[bool]:
        """
        Use this method to set a custom title for an administrator in a
        supergroup promoted by the bot. Returns True on success. for
        more: https://core.telegram.org/bots/api#setchatadministratorcust
        omtitle
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup (in the
                        format @supergroupusername)
        :param user_id: Unique identifier of the target user
        :param custom_title: New custom title for the administrator;
                             0-16 characters, emoji are not allowed
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "user_id": user_id,
            "custom_title": custom_title,
        }

        return self._session.call_method(
            bool, "setChatAdministratorCustomTitle", params
        )

    def ban_channel(
        self, chat_id: int | str, sender_chat_id: int
    ) -> Awaitable[bool]:
        """
        Use this method to ban a channel chat in a supergroup or a
        channel. Until the chat is unbanned, the owner of the banned chat
        won't be able to send messages on behalf of any of their
        channels. The bot must be an administrator in the supergroup or
        channel for this to work and must have the appropriate
        administrator rights. Returns True on success. for more:
        https://core.telegram.org/bots/api#banchatsenderchat
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param sender_chat_id: Unique identifier of the target
                               sender chat
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id,
        }

        return self._session.call_method(bool, "banChatSenderChat", params)

    def unban_channel(
        self, chat_id: int | str, sender_chat_id: int
    ) -> Awaitable[bool]:
        """
        Use this method to unban a previously banned channel chat in a
        supergroup or channel. The bot must be an administrator for this
        to work and must have the appropriate administrator rights.
        Returns True on success. for more:
        https://core.telegram.org/bots/api#unbanchatsenderchat
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param sender_chat_id: Unique identifier of the target
                               sender chat
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "sender_chat_id": sender_chat_id,
        }

        return self._session.call_method(
            bool, "unbanChatSenderChat", params
        )

    def set_permissions(
        self,
        chat_id: int | str,
        permissions: schemas.ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to set default chat permissions for all members.
        The bot must be an administrator in the group or a supergroup for
        this to work and must have the can_restrict_members administrator
        rights. Returns True on success. for more:
        https://core.telegram.org/bots/api#setchatpermissions
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup (in the
                        format @supergroupusername)
        :param permissions: A JSON-serialized object for new default
                            chat permissions
        :param use_independent_chat_permissions: Pass True if chat
                                                 permissions are set
                                                 independently.
                                                 Otherwise, the can_
                                                 send_other_messages
                                                 and can_add_web_pag
                                                 e_previews
                                                 permissions will
                                                 imply the
                                                 can_send_messages,
                                                 can_send_audios,
                                                 can_send_documents,
                                                 can_send_photos,
                                                 can_send_videos, ca
                                                 n_send_video_notes,
                                                 and can_send_voice_
                                                 notes permissions;
                                                 the can_send_polls
                                                 permission will
                                                 imply the
                                                 can_send_messages
                                                 permission.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "permissions": permissions}
        if use_independent_chat_permissions is not None:
            params[
                "use_independent_chat_permissions"
            ] = use_independent_chat_permissions

        return self._session.call_method(
            bool, "setChatPermissions", params
        )

    def export_invite_link(self, chat_id: int | str) -> Awaitable[str]:
        """
        Use this method to generate a new primary invite link for a chat;
        any previously generated primary link is revoked. The bot must be
        an administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns the new invite link as
        String on success. for more:
        https://core.telegram.org/bots/api#exportchatinvitelink
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(
            str, "exportChatInviteLink", params
        )

    def create_invite_link(
        self,
        chat_id: int | str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
    ) -> Awaitable[schemas.ChatInviteLink]:
        """
        Use this method to create an additional invite link for a chat.
        The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. The link can be
        revoked using the method revokeChatInviteLink. Returns the new
        invite link as ChatInviteLink object. for more:
        https://core.telegram.org/bots/api#createchatinvitelink
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param name: Invite link name; 0-32 characters
        :param expire_date: Point in time (Unix timestamp) when the
                            link will expire
        :param member_limit: The maximum number of users that can be
                             members of the chat simultaneously
                             after joining the chat via this invite
                             link; 1-99999
        :param creates_join_request: True, if users joining the chat
                                     via the link need to be
                                     approved by chat
                                     administrators. If True,
                                     member_limit can't be specified
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}
        if name is not None:
            params["name"] = name

        if expire_date is not None:
            params["expire_date"] = expire_date

        if member_limit is not None:
            params["member_limit"] = member_limit

        if creates_join_request is not None:
            params["creates_join_request"] = creates_join_request

        return self._session.call_method(
            schemas.ChatInviteLink, "createChatInviteLink", params
        )

    def edit_invite_link(
        self,
        chat_id: int | str,
        invite_link: str,
        name: Optional[str] = None,
        expire_date: Optional[int] = None,
        member_limit: Optional[int] = None,
        creates_join_request: Optional[bool] = None,
    ) -> Awaitable[schemas.ChatInviteLink]:
        """
        Use this method to edit a non-primary invite link created by the
        bot. The bot must be an administrator in the chat for this to
        work and must have the appropriate administrator rights. Returns
        the edited invite link as a ChatInviteLink object. for more:
        https://core.telegram.org/bots/api#editchatinvitelink
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param invite_link: The invite link to edit
        :param name: Invite link name; 0-32 characters
        :param expire_date: Point in time (Unix timestamp) when the
                            link will expire
        :param member_limit: The maximum number of users that can be
                             members of the chat simultaneously
                             after joining the chat via this invite
                             link; 1-99999
        :param creates_join_request: True, if users joining the chat
                                     via the link need to be
                                     approved by chat
                                     administrators. If True,
                                     member_limit can't be specified
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "invite_link": invite_link}
        if name is not None:
            params["name"] = name

        if expire_date is not None:
            params["expire_date"] = expire_date

        if member_limit is not None:
            params["member_limit"] = member_limit

        if creates_join_request is not None:
            params["creates_join_request"] = creates_join_request

        return self._session.call_method(
            schemas.ChatInviteLink, "editChatInviteLink", params
        )

    def revoke_invite_link(
        self, chat_id: int | str, invite_link: str
    ) -> Awaitable[schemas.ChatInviteLink]:
        """
        Use this method to revoke an invite link created by the bot. If
        the primary link is revoked, a new link is automatically
        generated. The bot must be an administrator in the chat for this
        to work and must have the appropriate administrator rights.
        Returns the revoked invite link as ChatInviteLink object. for
        more: https://core.telegram.org/bots/api#revokechatinvitelink
        :param chat_id: Unique identifier of the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param invite_link: The invite link to revoke
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "invite_link": invite_link}

        return self._session.call_method(
            schemas.ChatInviteLink, "revokeChatInviteLink", params
        )

    def approve_join_request(
        self, chat_id: int | str, user_id: int
    ) -> Awaitable[bool]:
        """
        Use this method to approve a chat join request. The bot must be
        an administrator in the chat for this to work and must have the
        can_invite_users administrator right. Returns True on success.
        for more:
        https://core.telegram.org/bots/api#approvechatjoinrequest
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param user_id: Unique identifier of the target user
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "user_id": user_id}

        return self._session.call_method(
            bool, "approveChatJoinRequest", params
        )

    def decline_join_request(
        self, chat_id: int | str, user_id: int
    ) -> Awaitable[bool]:
        """
        Use this method to decline a chat join request. The bot must be
        an administrator in the chat for this to work and must have the
        can_invite_users administrator right. Returns True on success.
        for more:
        https://core.telegram.org/bots/api#declinechatjoinrequest
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param user_id: Unique identifier of the target user
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "user_id": user_id}

        return self._session.call_method(
            bool, "declineChatJoinRequest", params
        )

    def set_photo(
        self, chat_id: int | str, photo: IO[bytes]
    ) -> Awaitable[bool]:
        """
        Use this method to set a new profile photo for the chat. Photos
        can't be changed for private chats. The bot must be an
        administrator in the chat for this to work and must have the
        appropriate administrator rights. Returns True on success. for
        more: https://core.telegram.org/bots/api#setchatphoto
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param photo: New chat photo, uploaded using multipart/form-
                      data
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "photo": photo}

        return self._session.call_method(bool, "setChatPhoto", params)

    def delete_photo(self, chat_id: int | str) -> Awaitable[bool]:
        """
        Use this method to delete a chat photo. Photos can't be changed
        for private chats. The bot must be an administrator in the chat
        for this to work and must have the appropriate administrator
        rights. Returns True on success. for more:
        https://core.telegram.org/bots/api#deletechatphoto
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(bool, "deleteChatPhoto", params)

    def set_title(self, chat_id: int | str, title: str) -> Awaitable[bool]:
        """
        Use this method to change the title of a chat. Titles can't be
        changed for private chats. The bot must be an administrator in
        the chat for this to work and must have the appropriate
        administrator rights. Returns True on success. for more:
        https://core.telegram.org/bots/api#setchattitle
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param title: New chat title, 1-128 characters
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "title": title}

        return self._session.call_method(bool, "setChatTitle", params)

    def set_description(
        self, chat_id: int | str, description: Optional[str] = None
    ) -> Awaitable[bool]:
        """
        Use this method to change the description of a group, a
        supergroup or a channel. The bot must be an administrator in the
        chat for this to work and must have the appropriate administrator
        rights. Returns True on success. for more:
        https://core.telegram.org/bots/api#setchatdescription
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param description: New chat description, 0-255 characters
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}
        if description is not None:
            params["description"] = description

        return self._session.call_method(
            bool, "setChatDescription", params
        )

    def pin_message(
        self,
        chat_id: int | str,
        message_id: int,
        disable_notification: Optional[bool] = None,
    ) -> Awaitable[bool]:
        """
        Use this method to add a message to the list of pinned messages
        in a chat. If the chat is not a private chat, the bot must be an
        administrator in the chat for this to work and must have the
        'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns
        True on success. for more:
        https://core.telegram.org/bots/api#pinchatmessage
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_id: Identifier of a message to pin
        :param disable_notification: Pass True if it is not
                                     necessary to send a
                                     notification to all chat
                                     members about the new pinned
                                     message. Notifications are
                                     always disabled in channels and
                                     private chats.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "message_id": message_id}
        if disable_notification is not None:
            params["disable_notification"] = disable_notification

        return self._session.call_method(bool, "pinChatMessage", params)

    def unpin_message(
        self, chat_id: int | str, message_id: Optional[int] = None
    ) -> Awaitable[bool]:
        """
        Use this method to remove a message from the list of pinned
        messages in a chat. If the chat is not a private chat, the bot
        must be an administrator in the chat for this to work and must
        have the 'can_pin_messages' administrator right in a supergroup
        or 'can_edit_messages' administrator right in a channel. Returns
        True on success. for more:
        https://core.telegram.org/bots/api#unpinchatmessage
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :param message_id: Identifier of a message to unpin. If not
                           specified, the most recent pinned message
                           (by sending date) will be unpinned.
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}
        if message_id is not None:
            params["message_id"] = message_id

        return self._session.call_method(bool, "unpinChatMessage", params)

    def unpin_all_messages(self, chat_id: int | str) -> Awaitable[bool]:
        """
        Use this method to clear the list of pinned messages in a chat.
        If the chat is not a private chat, the bot must be an
        administrator in the chat for this to work and must have the
        'can_pin_messages' administrator right in a supergroup or
        'can_edit_messages' administrator right in a channel. Returns
        True on success. for more:
        https://core.telegram.org/bots/api#unpinallchatmessages
        :param chat_id: Unique identifier for the target chat or
                        username of the target channel (in the
                        format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(
            bool, "unpinAllChatMessages", params
        )

    def leave(self, chat_id: int | str) -> Awaitable[bool]:
        """
        Use this method for your bot to leave a group, supergroup or
        channel. Returns True on success. for more:
        https://core.telegram.org/bots/api#leavechat
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(bool, "leaveChat", params)

    def get(self, chat_id: int | str) -> Awaitable[schemas.Chat]:
        """
        Use this method to get up to date information about the chat
        (current name of the user for one-on-one conversations, current
        username of a user, group or channel, etc.). Returns a Chat
        object on success. for more:
        https://core.telegram.org/bots/api#getchat
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(schemas.Chat, "getChat", params)

    def get_adminstrators(
        self, chat_id: int | str
    ) -> Awaitable[List[schemas.ChatMember]]:
        """
        Use this method to get a list of administrators in a chat, which
        aren't bots. Returns an Array of ChatMember objects. for more:
        https://core.telegram.org/bots/api#getchatadministrators
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(
            List[schemas.ChatMember], "getChatAdministrators", params
        )

    def get_chat_member_count(self, chat_id: int | str) -> Awaitable[int]:
        """
        Use this method to get the number of members in a chat. Returns
        Int on success. for more:
        https://core.telegram.org/bots/api#getchatmembercount
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(int, "getChatMemberCount", params)

    def get_member(
        self, chat_id: int | str, user_id: int
    ) -> Awaitable[schemas.ChatMember]:
        """
        Use this method to get information about a member of a chat. The
        method is only guaranteed to work for other users if the bot is
        an administrator in the chat. Returns a ChatMember object on
        success. for more:
        https://core.telegram.org/bots/api#getchatmember
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup or channel
                        (in the format @channelusername)
        :param user_id: Unique identifier of the target user
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id, "user_id": user_id}

        return self._session.call_method(
            schemas.ChatMember, "getChatMember", params
        )

    def set_sticker_set(
        self, chat_id: int | str, sticker_set_name: str
    ) -> Awaitable[bool]:
        """
        Use this method to set a new group sticker set for a supergroup.
        The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Use the field
        can_set_sticker_set optionally returned in getChat requests to
        check if the bot can use this method. Returns True on success.
        for more: https://core.telegram.org/bots/api#setchatstickerset
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup (in the
                        format @supergroupusername)
        :param sticker_set_name: Name of the sticker set to be set
                                 as the group sticker set
        :return: See link mentioned above for more information
        """
        params: dict = {
            "chat_id": chat_id,
            "sticker_set_name": sticker_set_name,
        }

        return self._session.call_method(bool, "setChatStickerSet", params)

    def delete_sticker_set(self, chat_id: int | str) -> Awaitable[bool]:
        """
        Use this method to delete a group sticker set from a supergroup.
        The bot must be an administrator in the chat for this to work and
        must have the appropriate administrator rights. Use the field
        can_set_sticker_set optionally returned in getChat requests to
        check if the bot can use this method. Returns True on success.
        for more: https://core.telegram.org/bots/api#deletechatstickerset
        :param chat_id: Unique identifier for the target chat or
                        username of the target supergroup (in the
                        format @supergroupusername)
        :return: See link mentioned above for more information
        """
        params: dict = {"chat_id": chat_id}

        return self._session.call_method(
            bool, "deleteChatStickerSet", params
        )
