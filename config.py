
import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Config(object):

    API_ID = os.environ.get("API_ID", "22384370")
    API_HASH = os.environ.get("API_HASH", "05e2be75292ecbec3f7a29bf13b1e29e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8111134914:AAEjc9qhiuPGDnob9OS2zL31eOnd6j8PRPk")

    # start_pic
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/5d01f129358105db8f748.jpg")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "80"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = os.environ.get("FORCE_SUB", "") 
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "Cluster0")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://botzashu:LjkXI1JoztDQiQlr@cluster0.38ague0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

    # sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAELFqBllhB70i13m-woXeIWDXU6BD2j7wAC9gcAAkb7rAR7xdjVOS5ziTQE")

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7062828064').split()]
    
    

    SET_CPT = """Exam: <code>/set_caption {file_name} & {file_caption}</code>
    
||https://t.me/PW_BOT_HELP/2||"""

    DEF_CAP  = """<b>{file_caption}</b>

<blockquote>⚡️𝐉𝐎𝐈𝐍 𝐁𝐀𝐂𝐊𝐔𝐏 - @Techshyam007
⚡️𝐉𝐎𝐈𝐍 𝐓𝐞𝐜𝐡𝐬𝐡𝐲𝐚𝐦 - @techshyaam</blockquote>"""

