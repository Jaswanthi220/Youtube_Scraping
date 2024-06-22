from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Set up the browser
driver = webdriver.Edge()

# Navigate to YouTube trending page
driver.get("https://www.youtube.com/feed/trending")

# Wait for the page to load
time.sleep(5)

# Scroll down to load more videos (you may need to customize this part)
for i in range(3):  # You may need to adjust the number of iterations based on your requirements
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
# Extract video titles and links
video_elements = driver.find_elements(By.XPATH, "//a[@id='video-title']")
video_titles = [video.text for video in video_elements]
video_links = [video.get_attribute("href") for video in video_elements]
# Store data in a CSV file
csv_file_path = "youtube_trending_video.csv"

with open(csv_file_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])  # Write header

    for title, link in zip(video_titles, video_links):
        writer.writerow([title, link])

# Print the path to the CSV file
print(f"Data saved to: {csv_file_path}")

# Close the browser
driver.quit()