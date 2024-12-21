from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import Select
import numpy as np
import time

# driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))

# driver.get("http://127.0.0.1:8000/")


def test_signup_valid():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "email").send_keys("validemail@example.com")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )
        print("Test Passed: Valid signup")
    except:
        print("Test Failed: Valid signup")
    finally:
        driver.quit()


def test_signup_invalid_email():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/")

    driver.find_element(By.ID, "username").send_keys("invaliduser")
    driver.find_element(By.ID, "email").send_keys("invalidemail")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        time.sleep(2)
        alert = driver.switch_to.alert
        print("Alert detected with text:", alert.text)

        alert.accept()
        print("Test Passed: Invalid Email message displayed")
    except NoAlertPresentException:
        print("Test Failed: Invalid Email message displayed")
    finally:
        driver.quit()


def test_signup_existing_username():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "email").send_keys("validuser@example.com")
    driver.find_element(By.ID, "password").send_keys("Password123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/p"))
        )
        print("Test Passed: User Exists")
    except:
        print("Test Failed: User Exists")
    finally:
        driver.quit()


def test_signup_existing_email():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/")

    driver.find_element(By.ID, "username").send_keys("validemail")
    driver.find_element(By.ID, "email").send_keys("validemail@example.com")
    driver.find_element(By.ID, "password").send_keys("Password123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/p"))
        )
        print("Test Passed: Email Exists")
    except:
        print("Test Failed: Email Exists")
    finally:
        driver.quit()

def test_signup_missing_fields():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        # WebDriverWait(driver, 10).until(EC.alert_is_present())
        time.sleep(2)
        alert = driver.switch_to.alert
        print("Alert detected with text:", alert.text)

        alert.accept()
        print("Test Passed: Missing fields validation message displayed")
    except NoAlertPresentException:
        print("Test Failed: Missing fields validation message not displayed")
    finally:
        driver.quit()



#///////////////////////////////////////////// El Test Beta3 el Login Page //////////////////////////////////////////////

def test_login_valid():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )
        print("Test Passed: Login Successful")
    except:
        print("Test Failed: Login Successful")

    finally:
        driver.quit()

def test_login_username():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("invaliduser")
    driver.find_element(By.ID, "password").send_keys("Password123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/p"))
        )
        print("Test Passed: Wrong UserName")
    except:
        print("Test Failed: Wrong UserName")
    finally:
        driver.quit()

def test_login_password():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("Password1!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/p"))
        )
        print("Test Passed: Wrong Password")
    except:
        print("Test Failed: Wrong Password")
    finally:
        driver.quit()


#///////////////////////////////////////////// El Test Beta3 el Movies Page //////////////////////////////////////////////
def test_Home_Page_Logged_In_valid():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )
        print("Test Passed: Home Page Logged In Working")
    except:
        print("Test Failed: Home Page Logged In Working")
    finally:
        driver.quit()


def test_Home_Page_Logged_Out_valid():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/shenron/movies/")

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )
        print("Test Passed: Home Page Logged Out Working")
    except:
        print("Test Failed: Home Page Logged Out  Working")
    finally:
        driver.quit()


def test_movie_Page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[7]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]"))
        )
        print("Test Passed: Movie Page Logged In Working")
    except:
        print("Test Failed: Movie Page Logged In Working")
    finally:
        driver.quit()

def test_movie_Page_logged_out():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get(f"http://127.0.0.1:8000/shenron/movies/{np.random.randint(0, 500)}/")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]"))
        )
        print("Test Passed: Movie Page Logged Out Working")
    except:
        print("Test Failed: Movie Page Logged Out Working")
    finally:
        driver.quit()

#///////////////////////////////////////////// El Test Beta3 el Search //////////////////////////////////////////////
def test_Search_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/div/a[1]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/form/input[2]"))
        )

        driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys("avengers")

        driver.find_element(By.XPATH, "/html/body/form/button").click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/ul/li[1]"))
        )

        print("Test Passed: Search Logged In Working")
    except:
        print("Test Failed: Search Logged In Working")
    finally:
        driver.quit()
#///////////////////////////////////////////// El Test Beta3 el Favourites Page //////////////////////////////////////////////
def test_favorites_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[3]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/p"))
        )
        print("Test Passed: Empty Favorites Logged In")
    except:
        print("Test Failed: Empty favorites Logged In")
    finally:
        driver.quit()


def test_Add_favorites_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[7]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div[2]/a"))
        )

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/a").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[3]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div"))
        )

        print("Test Passed: Add to favorites Logged In")
    except:
        print("Test Failed: Add to favorites Logged In")
    finally:
        driver.quit()



def test_remove_favorites_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[3]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div/div"))
        )

        card = driver.find_element(By.XPATH, "/html/body/main/div/div/a")

        actions = ActionChains(driver)
        actions.move_to_element(card).perform()

        driver.find_element(By.XPATH, "/html/body/main/div/div/form/button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/p"))
        )

        print("Test Passed: Remove Favorites Logged In")
    except:
        print("Test Failed: Remove favorites Logged In")
    finally:
        driver.quit()


def test_favorites_page_logged_out():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get(f"http://127.0.0.1:8000/shenron/movies/{np.random.randint(0, 500)}/")

    driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/a").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )


        print("Test Passed: Add to favorites Logged Out")
    except:
        print("Test Failed: Add to favorites Logged Out")
    finally:
        driver.quit()


#///////////////////////////////////////////// El Test Beta3 el Forums Page //////////////////////////////////////////////
def test_forums_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/h2"))
        )
        print("Test Passed: Forums Logged In")
    except:
        print("Test Failed: Forums Logged In")
    finally:
        driver.quit()


def test_delete_forums_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()

        forums_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))
        for i in range(1, forums_list_count + 1):
            forums_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "Created by validuser" in forums_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/form/button").click()
                break

        WebDriverWait(driver, 10).until(
            lambda driver: len(driver.find_elements(By.XPATH, "/html/body/ul/li")) < forums_list_count
        )
        print("Test Passed: Delete Forums Logged In")
    except:
        print("Test Failed: Delete Forums Logged In")
    finally:
        driver.quit()

def test_create_forums_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()

        forums_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))

        driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys(f"Post Test")
        driver.find_element(By.XPATH, "/html/body/form/button").click()


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/ul/li[{forums_list_count + 1}]/a"))
        )
        print("Test Passed: Create Forums Logged In")
    except:
        print("Test Failed: Create Forums Logged In")
    finally:
        driver.quit()


def test_create_post_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()

        forums_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))

        for i in range(1, forums_list_count + 1):
            forums_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "Created by validuser" in forums_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/a").click()
                break



        posts_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))

        WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element(By.XPATH, "/html/body/h2[1]").text == "Posts"
        )
        driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys("Test Title")
        driver.find_element(By.XPATH, "/html/body/form/textarea").send_keys("Test Content")

        driver.find_element(By.XPATH, "/html/body/form/button").click()


        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/ul/li[{posts_list_count + 1}]/a"))
        )

        print("Test Passed: Create Post Logged In")
    except:
        print("Test Failed: Create Post Logged In")
    finally:
        driver.quit()


def test_create_comment_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()

        forums_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))

        for i in range(1, forums_list_count + 1):
            forums_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "by validuser" in forums_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/a").click()
                break

        posts_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))


        WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element(By.XPATH, "/html/body/h2[1]").text == "Posts"
        )

        for i in range(1, posts_list_count + 1):
            posts_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "by validuser" in posts_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/a").click()
                break

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.XPATH, "/html/body/h2[1]").text == "Comments"
        )
        comments_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))

        driver.find_element(By.XPATH, "/html/body/form[2]/textarea").send_keys("Test Comment")
        driver.find_element(By.XPATH, f"/html/body/form[2]/button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"/html/body/ul/li[{comments_list_count + 1}]"))
        )

        print("Test Passed: Create Comment Logged In")
    except:
        print("Test Failed: Create Comment Logged In")
    finally:
        driver.quit()


def test_delete_post_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()

        forums_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))

        for i in range(1, forums_list_count + 1):
            forums_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "by validuser" in forums_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/a").click()
                break

        posts_list_count = len(driver.find_elements(By.XPATH, "/html/body/ul/li"))


        WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element(By.XPATH, "/html/body/h2[1]").text == "Posts"
        )

        for i in range(1, posts_list_count + 1):
            posts_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "by validuser" in posts_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/a").click()
                break

        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.XPATH, "/html/body/h2[1]").text == "Comments"
        )

        driver.find_element(By.XPATH, f"/html/body/form[1]/button").click()

        for i in range(1, forums_list_count + 1):
            forums_list = driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]").text
            if "by validuser" in forums_list:
                driver.find_element(By.XPATH, f"/html/body/ul/li[{i}]/a").click()
                break

        WebDriverWait(driver, 10).until(
            lambda driver: len(driver.find_elements(By.XPATH, "/html/body/ul/li")) < posts_list_count
        )

        print("Test Passed: Delete Post Logged In")
    except:
        print("Test Failed: Delete Post Logged In")
    finally:
        driver.quit()

def test_forums_page_logged_out():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/forum/")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )


        print("Test Passed: Forums Logged Out")
    except:
        print("Test Failed: Forums Logged Out")
    finally:
        driver.quit()

#///////////////////////////////////////////// El Test Beta3 el Reviews Page //////////////////////////////////////////////

def test_reviews_Page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[5]").click()

        WebDriverWait(driver, 10).until(
            lambda driver: "validuser" in driver.find_element(By.XPATH, "/html/body/div[2]/h1").text
        )
        print("Test Passed: Reviews Page Logged In Working")
    except:
        print("Test Failed: Reviews Page Logged In Working")
    finally:
        driver.quit()

def test_add_new_reviews_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[7]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[3]/a").click()

        dropdown = Select(driver.find_element(By.ID, "acting"))
        dropdown.select_by_value("3")
        dropdown2 = Select(driver.find_element(By.ID, "plot"))
        dropdown2.select_by_value("4")
        dropdown3 = Select(driver.find_element(By.ID, "cinematography"))
        dropdown3.select_by_value("3")
        dropdown4 = Select(driver.find_element(By.ID, "music"))
        dropdown4.select_by_value("3")
        dropdown5 = Select(driver.find_element(By.ID, "pacing"))
        dropdown5.select_by_value("4")
        dropdown6 = Select(driver.find_element(By.ID, "character_development"))
        dropdown6.select_by_value("5")

        driver.find_element(By.ID, "overall").send_keys("test review")

        driver.find_element(By.XPATH, "/html/body/form/button").click()

        WebDriverWait(driver, 10).until(
            lambda driver: "Spirited Away" in driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h2").text
        )

        print("Test Passed: Review Add Logged In")
    except:
        print("Test Failed: Review Add Logged In")
    finally:
        driver.quit()

def test_add_existing_reviews_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[7]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[3]/a").click()

        WebDriverWait(driver, 10).until(
            lambda driver: "Spirited Away" in driver.find_element(By.XPATH, "/html/body/div[2]/div/div/h2").text
        )

        print("Test Passed: Review Exists Logged In")
    except:
        print("Test Failed: Review Exists Logged In")
    finally:
        driver.quit()

def test_movie_reviews_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div/div[7]").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[4]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/a").click()

        WebDriverWait(driver, 10).until(
            lambda driver: "Spirited Away's Reviews" in driver.find_element(By.XPATH, "/html/body/div[2]/h1").text
        )

        print("Test Passed: Movie Reviews Logged In")
    except:
        print("Test Failed: Movie Reviews Logged In")
    finally:
        driver.quit()

def test_remove_movie_reviews_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[5]").click()

        WebDriverWait(driver, 10).until(
            lambda driver: "validuser" in driver.find_element(By.XPATH, "/html/body/div[2]/h1").text
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div/form/button/a").click()

        WebDriverWait(driver, 10).until(
            lambda driver: len(driver.find_elements(By.XPATH, "/html/body/div[2]/div/div")) == 0
        )
        print("Test Passed: Remove Reviews Logged In")
    except:
        print("Test Failed: Remove Reviews Logged In")
    finally:
        driver.quit()






#///////////////////////////////////////////// El Test Beta3 el Profile Page //////////////////////////////////////////////
def test_profile_page_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.get("http://127.0.0.1:8000/profile/")

        # driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/a[4]").click()
        #
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/img"))
        )
        print("Test Passed: Profile Logged In")
    except:
        print("Test Failed: Profile Logged In")
    finally:
        driver.quit()

def test_reset_password_same_as_old_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.get("http://127.0.0.1:8000/profile/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/a").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "old_password"))
        )

        driver.find_element(By.ID, "old_password").send_keys("ValidPassword123!")
        driver.find_element(By.ID, "new_password").send_keys("ValidPassword123!")
        driver.find_element(By.ID, "confirm_password").send_keys("ValidPassword123!")

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/form/button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/p"))
        )

        print("Test Passed: New Password equal Old Password Logged In")
    except:
        print("Test Failed: New Password equal Old Password Logged In")
    finally:
        driver.quit()


def test_reset_password_old_wrong_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.get("http://127.0.0.1:8000/profile/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/a").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "old_password"))
        )

        driver.find_element(By.ID, "old_password").send_keys("ValidPassword12")
        driver.find_element(By.ID, "new_password").send_keys("ValidPassword12!")
        driver.find_element(By.ID, "confirm_password").send_keys("ValidPassword12!")

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/form/button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/p"))
        )

        print("Test Passed: Old Password Wrong Logged In")
    except:
        print("Test Failed: Old Password Wrong Logged In")
    finally:
        driver.quit()

def test_reset_password_new_confirm_wrong_logged_in():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/login/")

    driver.find_element(By.ID, "username").send_keys("validuser")
    driver.find_element(By.ID, "password").send_keys("ValidPassword123!")

    driver.find_element(By.XPATH, "/html/body/form/button").click()

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div/div/div[2]/button/a").click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]"))
        )

        driver.get("http://127.0.0.1:8000/profile/")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div/img"))
        )

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/a").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "old_password"))
        )

        driver.find_element(By.ID, "old_password").send_keys("ValidPassword123!")
        driver.find_element(By.ID, "new_password").send_keys("ValidPassword12!")
        driver.find_element(By.ID, "confirm_password").send_keys("ValidPassword1!")

        driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/form/button").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/p"))
        )

        print("Test Passed: New and Confirm Password Wrong Logged In")
    except:
        print("Test Failed: New and Confirm Password Wrong Logged In")
    finally:
        driver.quit()



def test_profile_page_logged_out():
    driver = webdriver.Chrome(service=service.Service(ChromeDriverManager().install()))
    driver.get("http://127.0.0.1:8000/profile/")

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )


        print("Test Passed: Forums Logged Out")
    except:
        print("Test Failed: Forums Logged Out")
    finally:
        driver.quit()
try:
    test_signup_valid()
    test_signup_invalid_email()
    test_signup_existing_username()
    test_signup_existing_email()
    test_signup_missing_fields()

    test_login_valid()
    test_login_username()
    test_login_password()

    test_Home_Page_Logged_In_valid()
    test_Home_Page_Logged_Out_valid()
    test_movie_Page_logged_in()
    test_movie_Page_logged_out()

    test_Search_logged_in()

    test_favorites_page_logged_in()
    test_Add_favorites_page_logged_in()
    test_remove_favorites_page_logged_in()
    test_favorites_page_logged_out()

    test_delete_forums_page_logged_in()
    test_create_forums_page_logged_in()
    test_create_post_page_logged_in()
    test_create_comment_logged_in()
    test_delete_post_logged_in()

    test_reviews_Page_logged_in()
    test_add_new_reviews_logged_in()
    test_add_existing_reviews_logged_in()
    test_movie_reviews_logged_in()
    test_remove_movie_reviews_logged_in()


    test_profile_page_logged_in()
    test_reset_password_same_as_old_logged_in()
    test_reset_password_old_wrong_logged_in()
    test_reset_password_new_confirm_wrong_logged_in()
    test_profile_page_logged_out()
finally:
    print("Registration Tests finished")