import pywhatkit
from datetime import time
import random

entire_bible = {"Genesis": 50, "Exodus": 40, "Leviticus": 27, "Numbers": 36, "Deuteronomy": 34, "Joshua": 24, "Judges": 21, "Ruth": 4, "1 Samuel": 31, "2 Samuel": 24, "1 Kings": 22, "2 Kings": 25, "1 Chronicles": 29,"2 Chronicles": 36, "Ezra": 10, "Nehemiah": 13, "Esther": 10, "Job": 42, "Psalms": 150, "Proverbs": 31, "Ecclesiastes": 12, "Song of Solomon": 8, "Isaiah": 66, "Jeremiah": 52, "Lamentations": 5, "Ezekiel": 48, "Daniel": 12, "Hosea": 14, "Joel": 3, "Amos": 9, "Obadiah": 1, "Jonah": 4, "Micah": 7, "Nahum": 3, "Habakkuk": 3, "Zephaniah": 3, "Haggai": 2, "Zechariah": 14, "Malachi": 4, "Matthew": 28, "Mark": 16, "Luke": 24, "John": 21, "Acts": 28, "Romans": 16, "1 Corinthians": 16, "2 Corinthians": 13, "Galatians": 6, "Ephesians": 6, "Philippians": 4, "Colossians": 4, "1 Thessalonians": 5, "2 Thessalonians": 3, "1 Timothy": 6, "2 Timothy": 4, "Titus": 3, "Philemon": 1, "Hebrews": 13, "James": 5, "1 Peter": 5, "2 Peter": 3, "1 John": 5, "2 John": 1, "3 John": 1, "Jude": 1, "Revelation": 22}

book = list(entire_bible)

bible_list = []

adjective_list = ["Children of God", "Royal Priesthood", "Servants of God", "Young Transformers", "Young Generals", "Salt of the Earth"]
#now = datetime.now().strftime("%H:%M:%S")

for book in entire_bible:
    for i in range(entire_bible[book]):
        bible_list.append(book + " " + str(i+1))

start_index = bible_list.index("Jonah 3")
groupchat = "I9utFhxb4E04St1mCqQHwN"
while start_index < 1190:
    print("date and time =", dt_string)
    adjective = random.randint(0, len(adjective_list) - 1)
    whatsapp_message = "Good morning, " + adjective_list[adjective] + ", today's challenge is " + str(bible_list[start_index]) +  " to " + str(bible_list[start_index+3])
    pywhatkit.sendwhatmsg_to_group_instantly(groupchat, whatsapp_message, 40, True, 30)
    print(whatsapp_message)
    start_index += 4
