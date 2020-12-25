#!/usr/bin/env python3

import time
import os
import config

FILE_PATH = 'path_to_text_file.txt'
SECONDS = 5


def get_words_list(file_path: str) -> list:
    """Returns a list of the text file word-by-word."""
    word_list = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                word_list.append(word)
    return word_list


def send_message(message: str, chatId: str) -> None:
    """Console command to run AppleScript."""
    os.system('osascript send.scpt {msg} "{id}"'.format(
        msg=message, id=chatId))


if __name__ == '__main__':
    word_list = get_words_list(FILE_PATH)
    for word in word_list:
        send_message(word, config.chat_guid)
        time.sleep(SECONDS)
