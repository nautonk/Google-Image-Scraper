# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
# Import libraries
import os
import concurrent.futures
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key):
    image_scraper = GoogleImageScraper(
        webdriver_path, image_path, search_key, extra_search_params, number_of_images, headless, min_resolution,
        max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)

    # Release resources
    del image_scraper


if __name__ == "__main__":
    # Define file path
    webdriver_path = os.path.normpath(os.path.join(os.getcwd(), 'webdriver', webdriver_executable()))
    image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

    # Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
    search_keys = list(
        set(["Female Cartoon", "Children Cartoon", "Cartoon Doodles", "Cartoon Face", "Cartoon People", "Horse Cartoon", "Cartoon Sketches", "Cartoon Funnies", "Cartoon Movies", "Teacher Cartoon", "Awesome Cartoon", "Panda Cartoon", "Cartoon Wallpaper", "Pig Cartoon", "List of Cartoons", "Number 7 Cartoon", "Cartoon Eyes", "Robot Cartoon", "Book Cartoon", "Cartoon Animals", "Cute Cartoon", "Cartoon Lovers", "Cartoons to Draw", "Food Cartoon", "Carton Box", "Pikachu Cartoon", "Cartoon Background", "How to Draw Cartoons", "Friends Cartoon", "Weird Cartoons", "Rabbit Cartoon", "Cartoon Objects", "Car Cartoon", "Classic Cartoons", "Baby Cartoon", "Om Nom Cartoon", "Cartoon Ghost", "Simple Cartoon", "Cartoon Couple", "Easy Cartoon", "Dog Cartoon", "Monkey Cartoon", "Cartoon Bunny", "English Cartoon", "Cartoon Strip", "Cake Cartoon", "Cow Cartoon", "Name Cartoon", "Penguin Cartoon", "Human Cartoon", "Heart Cartoon", "Cartoon Figures", "Forgotten Cartoons", "90s Kids Cartoons", "Cartoon Graphics", "Cartoon Heroes", "Top 10 Cartoons", "Cartoon Puppy", "Weather Cartoon", "Minion Cartoon", "Cartoon Clip Art", "Bugs Bunny Cartoons", "Head Cartoon", "Fish Cartoon", "School Cartoon", "Tiger Cartoon", "Bee Cartoon", "Unicorn Cartoon"]))

    # Parameters
    number_of_images = 50  # Desired number of images
    headless = True  # True = No Chrome GUI
    min_resolution = (700, 700)  # Minimum desired image resolution
    max_resolution = (9999, 9999)  # Maximum desired image resolution
    max_missed = 1000  # Max number of failed images before exit
    extra_search_params = '-inurl:freepik.com -inurl:pngtree.com'
    number_of_workers = 1  # Number of "workers" used
    keep_filenames = False  # Keep original URL image filenames

    # Run each search_key in a separate thread
    # Automatically waits for all threads to finish
    # Removes duplicate strings from search_keys
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_workers) as executor:
        executor.map(worker_thread, search_keys)
