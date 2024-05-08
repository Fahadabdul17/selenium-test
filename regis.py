from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Membuka URL website
driver = webdriver.Chrome()
driver.get("https://accounts.lambdatest.com/register")

# Mengisi form register
email = driver.find_element(By.ID, "email")
email.send_keys("saya17@gmail.com")

password = driver.find_element(By.ID, "password")
password.send_keys("inisaya17")

confirm_password = driver.find_element(By.ID, "userpassword")
confirm_password.send_keys("inisaya17")

# Menyetujui terms of service
terms_of_service_checkbox = driver.find_element(By.ID, "terms_of_service_checkbox")
terms_of_service_checkbox.click()

# Mengklik tombol register
register_button = driver.find_element(By.ID, "register_button")
register_button.click()

# Menunggu email verifikasi
sleep(60)

# Membuka tab email baru
driver.execute_script("window.open(https://accounts.lambdatest.com/email/verify');")

# Beralih ke tab email baru
driver.switch_to.window(driver.window_handles[1])

# Menemukan email verifikasi
verification_email = driver.find_element(By.CSS_SELECTOR, "a[href*='verify']")

# Mengklik tautan verifikasi email
verification_email.click()

# Beralih kembali ke tab awal
driver.switch_to.window(driver.window_handles[0])

# Memverifikasi bahwa akun telah terverifikasi
verification_message = driver.find_element(By.CSS_SELECTOR, ".verification-message")
assert verification_message.text == "Your account has been verified."

# Menutup browser
driver.quit()
