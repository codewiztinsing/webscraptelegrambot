import logging
import time
import  helium as hl
from bs4 import  BeautifulSoup
import requests
from bs4 import BeautifulSoup
from telegram import __version__ as TG_VER
import subprocess
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import pyautogui
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.


def key():
    pyautogui.keyDown("ctrl")
    pyautogui.keyDown("alt")
    pyautogui.press("z")
    pyautogui.keyUp("alt")
    pyautogui.keyUp("ctrl")


    time.sleep(5)
    pyautogui.moveTo(x=696, y=442, duration=0.05)
    print("Type: x=696, y=442")
    pyautogui.click()
    print("click3")
    pyautogui.moveTo(x=723, y=442, duration=0.05)
    print("Type: x=696, y=442")
    pyautogui.click()
    print("click3")
    pyautogui.moveTo(x=723, y=442, duration=0.05)
    print("Type: x=696, y=442")
    pyautogui.click()
    print("click3")
    pyautogui.moveTo(x=696, y=442, duration=0.05)
    print("Type: x=696, y=442")
    pyautogui.click()
    print("click3")


    time.sleep(1)
    pyautogui.moveTo(x=781, y=557, duration=0.1)
    print("Type:x=781, y=557")
    pyautogui.click()
    print("Click: ok")

    time.sleep(1.5)
    screen = pyautogui.screenshot(region=(1240,749, 120, 70))
    opencvImage = cv2.cvtColor(numpy.array(screen), cv2.COLOR_BGR2RGB)
    thresh = 70
    maxValue = 255

    # Binary Threshold1221
    th, binary = cv2.threshold(opencvImage, thresh, maxValue, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.expanduser("~") + "/Downloads/img.png",binary)
    return binary



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def parse_data_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    otp_generator_path = "/usr/bin/otp_generator"
    subprocess.Popen(otp_generator_path)
    # Enter a value
    value = "1221"
    # Send the value to the OTP generator
    subprocess.Popen(["otp_generator", "-set_value", value])

    otp = subprocess.check_output(["otp_generator", "-get_otp"]).decode("utf-8")
    browser = hl.start_firefox("https://cbeib.com.et/ARCIB-4/servlet/BrowserServlet")
    driver = hl.get_driver()
    hl.click("Close")

    hl.write("ABAALEXIB158", into="User Id")
    hl.write("654321", into="Password")
    hl.write(otp,into="One Time Password")
    hl.click("Login")
    hl.wait_until(hl.Text("Logout").exists())
    html = driver.page_source

    # scarape website
    dashboard_page = BeautifulSoup(html, 'html.parser')
    message = dashboard_page.h1.string
    hl.kill_browser()
    await update.message.reply_text(message)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("5568203115:AAG91GD83_4wexA5sAu7E5LDmK78yHFMVzU").build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("parse", parse_data_command))
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()

