
# Importing the necessary Libraries
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import random

# Library for loading the username and password
import os
from dotenv import load_dotenv
load_dotenv()



def get_jobs(keyword,num_jobs ):
    # Defining the chrome options to open in a private mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    # Fetching the Username and Password from the .env file
    username = os.getenv("STEPSTONE_USERNAME")
    password = os.getenv("STEPSTONE_PASSWORD")

    # Website address for Web Scrapping
    login_url = "https://www.stepstone.de/work/"+ keyword +"/in-germany?radius=100&searchOrigin=membersarea&whereType=autosuggest"

    driver.get(login_url)

    # Accepting the Cookies File
    try:
        driver.find_element(By.ID, "ccmgt_explicit_accept").click()
    except NoSuchElementException:
        pass
    # Signing in for getting the Salary Info. Can skip this step if salary info is not required.
    driver.find_element(By.XPATH, "//div[normalize-space()='Sign in']").click()

    driver.find_element(By.XPATH, "//span[@class='hf-provider-gxei9d'][normalize-space()='Sign in']").click()





    username_field = driver.find_element(By.CLASS_NAME, "login-registration-provider-1wuqtqx")
    password_field = driver.find_element(By.CLASS_NAME, "login-registration-provider-1g1vgpu")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.CLASS_NAME, "login-registration-provider-1k4ab3x")

    assert not  login_button.get_attribute("disabled")
    login_button.click()

    time.sleep(random.uniform(2, 5))

    # Defining the empty list to collect the details.

    jobs = []


    while len(jobs) < num_jobs:
        # Wait until job articles are loaded
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//article[starts-with(@id, "job-item-")]'))
        )

        job_articles = driver.find_elements(By.XPATH, '//article[starts-with(@id, "job-item-")]')

        for job in job_articles:
            # Printing the Progress of scraping
            print(f"Progress: {len(jobs)}/{num_jobs}")
            if len(jobs) >= num_jobs:
                break

            try:
                # Selecting each Job Box and Opening in new tab
                driver.execute_script("arguments[0].scrollIntoView();", job)
                clickable_div = job.find_element(By.XPATH, './/div[contains(@class, "res-")]')
                clickable_div.click()
                time.sleep(random.uniform(2, 5))
                job_tab = driver.window_handles[1]
                driver.switch_to.window(job_tab)
                time.sleep(random.uniform(2, 5))
                # Checking for Akamai Edge Error and Skipping it.
                if "Reference #" in driver.page_source and "edgesuite.net" in driver.current_url:
                    print("Akamai Edge error detected. Retrying once after delay...")
                    time.sleep(2)
                    driver.refresh()
                    WebDriverWait(driver, 10).until(
                        lambda d: "Reference #" not in d.page_source or "edgesuite.net" not in d.current_url)
                    time.sleep(random.uniform(2, 5))

                    if "Reference #" in driver.page_source:
                        print("Persistent Akamai error. Skipping this session.")
                        if len(driver.window_handles) > 1:
                            driver.close()
                            driver.switch_to.window(driver.window_handles[0])
                        else:
                            print("No secondary tab to close. Continuing.")

                collected_successfully = False
                while not collected_successfully:
                    try:
                        # Collecting the mandatory details.
                        company_name = driver.find_element(By.XPATH, '//li[contains(@class, "company-name")]//span[@data-genesis-element="TEXT"]/span').text
                        location = driver.find_element(By.XPATH,'//li[contains(@class, "location")]//span[@data-genesis-element="TEXT"]/span').text
                        job_title = driver.find_element(By.XPATH, '//span[@data-at="header-job-title"]').text
                        collected_successfully = True

                    except NoSuchElementException:
                        time.sleep(5)
                        driver.refresh()
                # Collecting the remaining details.
                try:
                    contract_type = driver.find_element(By.XPATH, '//li[contains(@class, "contract-type")]//span[@data-genesis-element="TEXT"]/span').text
                except NoSuchElementException:
                    contract_type = -1

                try:
                    job_type = driver.find_element(By.XPATH,'//li[contains(@class, "work-type")]//span[@data-genesis-element="TEXT"]/span').text
                except NoSuchElementException:
                    job_type = -1

                try:
                    published_days = driver.find_element(By.XPATH, '//li[contains(@class, "date")]//span[@data-genesis-element="TEXT"]/span').text
                except NoSuchElementException:
                    published_days = -1

                try:
                    salary_range = driver.find_element(By.XPATH,'//span[@data-at="salary-range"]').text
                except NoSuchElementException:
                    salary_range = -1

                try:
                    verified_status = driver.find_element(By.XPATH, '//li[contains(@class, "verified")]//span[@data-genesis-element="TEXT"]/span').text
                except NoSuchElementException:
                    verified_status = -1
                # Saving all details in the List
                jobs.append({"Job Title" : job_title,
                             "Company Name": company_name,
                             "Location": location,
                             "Contract Type": contract_type,
                             "Job Type": job_type,
                             "Published Days": published_days,
                             "Salary Range": salary_range,
                             "Verified Status": verified_status})

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print(f"Error processing job: {e}")
                continue

        # Try to click the Next button
        try:
            next_button = driver.find_element(By.XPATH, "//a[@aria-label='Next']")
            if "disabled" in next_button.get_attribute("class"):
                print("Reached the last page.")
                break  # Exit the loop if the next button is disabled
            else:
                driver.execute_script("arguments[0].scrollIntoView();", next_button)
                next_button.click()
                time.sleep(random.uniform(2, 5))  # Wait for next page to load
        except Exception as e:
            print("No more pages or next button not found.")
            break

    return pd.DataFrame(jobs)


# Calling the function and saving the details in csv file.

df = get_jobs('data scientist',500)

df.to_csv('stepstone_jobs.csv', encoding='utf-8', index=False)