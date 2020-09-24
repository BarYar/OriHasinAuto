import unittest
from unittest import TestCase
from selenium import webdriver
from OriHasinAutomationTesting.Pages import HomePage,CategoryPage,CartPage,CartIcon,ProductPage
from random import randint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import StaleElementReferenceException
from time import sleep

class AOSTests(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/User/Desktop/Ori Selenium/chromedriver.exe")
        self.driver.get("http://advantageonlineshopping.com/#/")
        self.ListOfCategories=['headphones','mice','tablets','laptops','speakers']
        self.Hpage = HomePage(self.driver)
        self.Cpage = CategoryPage(self.driver)
        self.Ppage = ProductPage(self.driver)
        self.Cicon=CartIcon(self.driver)
        self.Cartpage=CartPage(self.driver)

    def tearDown(self):
        self.driver.find_element_by_xpath('//div[@class="logo"]')
        self.driver.close()

    def Excrisice1(self):
        pass
    def test_Exercise2(self):
      #  pointer=3
        plus=0
        index=0
        ListOfProducts = []

        for i in range(3):
            index2=randint(0,4) # Index of category
            self.Hpage.WaitToHomepage()
            self.Hpage.CategoryIcon(self.ListOfCategories[index2])
            self.Cpage.WaitToCategorypage()
            index3=randint(0,self.Cpage.NumberOfProducts()-1) # Index of product
            while index==1 and index3==1: # Specific product that Out Of Stock
                index3=randint(0,self.Cpage.NumberOfProducts()-1)
            self.Cpage.GetProduct(index3)
            self.Ppage.WaitToProductpage()
            self.Ppage.PlusQuantity(plus)
            plus+=plus
            ListOfProducts.append(self.Ppage.ProductAttributes())
            ListOfProducts[i][2] = (plus+1) # Update quantity of product
            ListOfProducts[i][3] = (plus+1) * ListOfProducts[i][3] # Update the price by quantity
            self.Ppage.AddToCartButton()
            self.Ppage.BackToCategory()
            self.Cpage.BackToHomepage()
        for i in range(3):
            print(ListOfProducts[i][0],"hey")
            print(self.Cicon.NameInCartIcon(2-i),"bye")
            self.Cicon.CartIcon()
            self.assertEqual(ListOfProducts[i][0], self.Cicon.NameInCartIcon(2-i))
            self.assertEqual(ListOfProducts[i][1], self.Cicon.ColorInCartIcon(2-i))
            self.assertEqual(ListOfProducts[i][2], self.Cicon.QtyInCartIcon(2-i))
            self.assertEqual(ListOfProducts[i][3], self.Cicon.PriceInCartIcon(2-i))
            #pointer-=1























