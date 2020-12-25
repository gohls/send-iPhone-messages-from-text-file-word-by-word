on run {targetMessageToSend, targetChatId}
  tell application "Messages"
    set targetService to 1st service whose service type = iMessage
    set chatId to targetChatId
    set targetGroupChat to a reference to text chat id chatId
    set targetMessage to targetMessageToSend
    send targetMessage to targetGroupChat
  end tell
end run
