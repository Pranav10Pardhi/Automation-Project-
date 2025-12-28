import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WEBSITE_URL = "https://demoqa.com/automation-practice-form"

# ---------- TEXT INPUT SELECTORS ----------
TEXT_SELECTORS = {
    "first_name": "#firstName",
    "last_name": "#lastName",
    "email": "#userEmail",
    "mobile": "#userNumber",
    "address": "#currentAddress"
}

# ---------- READ DATA FROM TXT FILE ----------
def parse_text_file(file_path: str):
    data = {}
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                data[key.strip().lower()] = value.strip()
    return data

# ---------- FILL FORM ----------
def fill_form(driver, data):
    wait = WebDriverWait(driver, 10)

    driver.get(WEBSITE_URL)

    wait = WebDriverWait(driver, 15)

    wait.until(EC.presence_of_element_located((By.ID, "firstName")))

    # ---------- TEXT FIELDS ----------
    for field, selector in TEXT_SELECTORS.items():
        if field in data:
            driver.find_element(By.CSS_SELECTOR, selector).send_keys(data[field])

    # ---------- GENDER ----------
    gender = data.get("gender", "").lower()
    if gender in ["male", "female", "other"]:
        driver.find_element(
            By.XPATH, f"//label[text()='{gender.capitalize()}']"
        ).click()

    # ---------- DATE OF BIRTH ----------
    if "dob" in data:
        dob_input = driver.find_element(By.ID, "dateOfBirthInput")
        dob_input.click()
        dob_input.send_keys(Keys.CONTROL + "a")
        dob_input.send_keys(data["dob"])
        dob_input.send_keys(Keys.ENTER)

    # ---------- SUBJECTS ----------
    if "subjects" in data:
        subject_input = driver.find_element(By.ID, "subjectsInput")
        for subject in data["subjects"].split(","):
            subject_input.send_keys(subject.strip())
            subject_input.send_keys(Keys.ENTER)

    # ---------- HOBBIES ----------
    if "hobbies" in data:
        for hobby in data["hobbies"].split(","):
            driver.find_element(
                By.XPATH, f"//label[text()='{hobby.strip()}']"
            ).click()

    # ---------- WAIT FOR MANUAL CHECK ----------
    print("🛑 Please verify form manually. Press ENTER to submit...")
    input()
    wait.until(
        EC.presence_of_element_located((By.ID, "example-modal-sizes-title-lg"))
    )
    print("✅ FORM SUBMITTED SUCCESSFULLY")


# ---------- MAIN ----------
def main():
    # data_file = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    data = parse_text_file("data.txt")

    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(WEBSITE_URL)
        fill_form(driver, data)
        time.sleep(3)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
