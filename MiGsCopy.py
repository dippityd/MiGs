from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from tkinter import *
import time
import pygubu
import tkinter as tk
import pyperclip
from pywinauto.application import Application
import tkinter.messagebox

driver = webdriver.Firefox()


class Applications:
    def __init__(self, master):
        self.master = master

        # Create builder
        self.builder = builder = pygubu.Builder()
        # Load ui file
        builder.add_from_file('main.ui')
        # Create widget, using master as parent
        self.mainwindow = builder.get_object('Frame_2', master)

        builder.connect_callbacks(self)

        self.Entry1 = entry1 = builder.get_object('Entry_1')
        self.Entry2 = entry2 = builder.get_object('Entry_2')
        self.Entry3 = entry3 = builder.get_object('Entry_3')
        self.Entry4 = entry4 = builder.get_object('Entry_4')
        self.Entry5 = entry5 = builder.get_object('Entry_5')
        self.Entry6 = entry6 = builder.get_object('Entry_6')
        self.Entry9 = entry9 = builder.get_object('Entry_9')
        self.Entry10 = entry10 = builder.get_object('Entry_10')
        self.Entry11 = entry11 = builder.get_object('Entry_11')
        self.Entry13 = entry13 = builder.get_object('Entry_13')
        self.Checkbutton = pop = builder.get_object('Checkbutton_1')

        self.pox = builder.get_variable('var')
        self.pox.set('False')

    def on_button_click(self):
        self.master.withdraw()
        goldMigs.startPage(self.master)


class goldMigs:
    def startPage(self):

        # Opening Firefox
        driver.get("https://migs.mastercard.com.au/mm")
        driver.maximize_window()

        # Logging into MiGs
        loginElem = driver.find_element_by_id("ownerId")
        loginElem.send_keys("securepay")
        loginElem = driver.find_element_by_id("userName")
        loginElem.send_keys(app.Entry1.get())
        loginElem = driver.find_element_by_id("password")
        loginElem.send_keys(app.Entry2.get())
        loginElem = driver.find_element_by_class_name("Submitlogin")
        type(loginElem)
        loginElem.click()
        try:
            errorMessage = driver.find_element_by_class_name('ErrorMessage')
            errorMessage.is_displayed()
            root.deiconify()
            message = tkinter.messagebox
            message.showerror('Incorrect Login Details', 'Please re-check your login details')
        except NoSuchElementException:
            goldMigs.createMerchant(self, preAuth=False, completeGoldMigs=False)

    def createMerchant(self, preAuth, completeGoldMigs):
        # Creating a new merchant
        try:
            pageElement = driver.find_element_by_link_text("New Merchant")
            type(pageElement)
            pageElement.click()
        except NoSuchElementException:
            print("Exception caught")

        merchantId = app.Entry3.get()
        preMerchantID = merchantId + "_P"
        pageElement = driver.find_element_by_id("merchantId")

        if preAuth:
            pageElement.send_keys(preMerchantID)
        else:
            pageElement.send_keys(merchantId)

        pageElement = driver.find_element_by_id("merchantName")
        pageElement.send_keys(app.Entry4.get())
        pageElement = driver.find_element_by_id("categoryCode")
        pageElement.send_keys(app.Entry5.get())
        pageElement = driver.find_element_by_id("goodsDescription")
        pageElement.send_keys(app.Entry4.get())
        pageElement = driver.find_element_by_id("address.address1")
        pageElement.send_keys(app.Entry9.get())
        pageElement = driver.find_element_by_id("address.city")
        pageElement.send_keys(app.Entry10.get())
        pageElement = driver.find_element_by_id("address.state")
        pageElement.send_keys(app.Entry11.get())
        pageElement = driver.find_element_by_id("password")
        pageElement.send_keys("----")
        pageElement = driver.find_element_by_id("repeatPassword")
        pageElement.send_keys("----")
        pageElement = driver.find_element_by_class_name("SubmitContinue")
        type(pageElement)
        pageElement.click()

        # Manage Merchants - Merchant Payment Details

        if preAuth:
            pageElement = driver.find_element_by_id("transactionMode")
            type(pageElement)
            pageElement.click()
            pageElement.send_keys(Keys.ARROW_DOWN)
            pageElement.send_keys(Keys.ARROW_UP)
            pageElement.click()

        pageElement = driver.find_element_by_id("vpc")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("csc")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("standAloneRefund")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("standAloneCapture")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("advanceMA")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("cardDetailsInDO")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("merchTxSrc")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_id("merchTxSrcSubType")
        type(pageElement)
        pageElement.click()
        pageElement = driver.find_element_by_class_name("SubmitContinue")
        type(pageElement)
        pageElement.click()

        # Manage Merchants - Payment Client Details

        try:
            pageElement = driver.find_element_by_partial_link_text("Generate")
            type(pageElement)
            pageElement.click()
            driver.implicitly_wait(3)
            pageElement = driver.find_element_by_class_name("SubmitContinue")
            type(pageElement)
            pageElement.click()
        except NoSuchElementException:
            print("Exception Caught")

        # Manage Merchants - Acquirer Link Summary
        pageElement = driver.find_element_by_css_selector('select')
        type(pageElement)
        pageElement.click()

        count = 0

        while count < 3:
            count += 1
            pageElement.send_keys(Keys.ARROW_DOWN)

        pageElement.click()

        pageElement = driver.find_element_by_class_name("SubmitAddLink")
        type(pageElement)
        pageElement.click()

        # Manage Merchants - Acquirer Link Details

        pageElement = driver.find_element_by_id("acquirerLinkStatus")
        type(pageElement)
        pageElement.click()

        pageElement.send_keys(Keys.ARROW_DOWN)
        pageElement.send_keys(Keys.ARROW_UP)

        pageElement.click()

        pageElement = driver.find_element_by_id("caic")
        caic = app.Entry6.get()
        caic = caic[1:]
        pageElement.send_keys(caic)

        pageElement = driver.find_element_by_id("defaultMerchantTransactionSource")
        type(pageElement)
        pageElement.click()
        pageElement.send_keys(Keys.ARROW_DOWN)
        pageElement.click()

        pageElement = driver.find_element_by_xpath("//*[@name='allowableMerchantTransactionSources'][@value='MT']")
        type(pageElement)
        pageElement.click()

        pageElement = driver.find_element_by_xpath("//*[@name='allowableMerchantTransactionFrequencies'][@value='SI']")
        type(pageElement)
        pageElement.click()

        if not preAuth:
            pageElement = driver.find_element_by_xpath(
                "//*[@name='allowableMerchantTransactionFrequencies'][@value='RE']")
            type(pageElement)
            pageElement.click()

        select = Select(driver.find_element_by_id("groupAvailableCurrencies"))
        select.select_by_visible_text("AUD - Australian Dollar")

        pageElement = driver.find_element_by_id("currenciesRight")
        type(pageElement)
        pageElement.click()

        select = Select(driver.find_element_by_id("groupAvailableCardBrands"))
        select.select_by_visible_text("MasterCard")

        pageElement = driver.find_element_by_id("cardBrandsRight")
        type(pageElement)
        pageElement.click()

        select = Select(driver.find_element_by_id("groupAvailableCardBrands"))
        select.select_by_visible_text("Visa")

        pageElement.click()

        counts2 = 1

        while counts2 < 6:
            pageElement = driver.find_element_by_id("inputAA" + str(counts2))
            type(pageElement)
            pageElement.click()
            pageElement.send_keys("CBAS2I1" + str(counts2))
            counts2 += 1

        pageElement = driver.find_element_by_name("submit")
        type(pageElement)
        pageElement.click()

        pageElement = driver.find_element_by_link_text("Continue")
        type(pageElement)
        pageElement.click()

        htmlElem = driver.find_element_by_tag_name('html')
        htmlElem.send_keys(Keys.END)  # scrolls to bottom

        addAmex = app.pox.get()

        if addAmex:
            pageElement = driver.find_element_by_class_name("SubmitAddLink")
            type(pageElement)
            pageElement.click()

            pageElement = driver.find_element_by_class_name("InputFieldsB")
            pageElement.send_keys(app.Entry13.get())

            pageElement = driver.find_element_by_id("acquirerLinkStatus")
            type(pageElement)
            pageElement.click()

            pageElement.send_keys(Keys.ARROW_DOWN)
            pageElement.send_keys(Keys.ARROW_UP)

            pageElement.click()

            pageElement = driver.find_element_by_id("defaultMerchantTransactionSource")
            type(pageElement)
            pageElement.click()
            pageElement.send_keys(Keys.ARROW_DOWN)
            pageElement.click()

            if not preAuth:
                pageElement = driver.find_element_by_xpath(
                    "//*[@name='allowableMerchantTransactionFrequencies'][@value='RE']")
                type(pageElement)
                pageElement.click()

            pageElement = driver.find_element_by_xpath("//*[@name='allowableMerchantTransactionSources'][@value='MT']")
            type(pageElement)
            pageElement.click()

            select = Select(driver.find_element_by_id("groupAvailableCurrencies"))
            select.select_by_visible_text("AUD - Australian Dollar")

            pageElement = driver.find_element_by_id("currenciesRight")
            type(pageElement)
            pageElement.click()

            select = Select(driver.find_element_by_id("groupAvailableCardBrands"))
            select.select_by_visible_text("American Express")

            pageElement = driver.find_element_by_id("cardBrandsRight")
            type(pageElement)
            pageElement.click()

            counts3 = 1

            while counts3 < 6:
                pageElement = driver.find_element_by_id("inputAA" + str(counts3))
                type(pageElement)
                pageElement.click()
                pageElement.send_keys("CBAS2I1" + str(counts3))
                counts3 += 1

            pageElement = driver.find_element_by_name("submit")
            type(pageElement)
            pageElement.click()

        # quit()

        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        pageElement = driver.find_elements(By.LINK_TEXT, 'Approve Merchant')[1]
        type(pageElement)
        pageElement.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        pageElement = driver.find_element(By.CLASS_NAME, 'SubmitSubmit')
        type(pageElement)
        pageElement.click()

        if preAuth and completeGoldMigs:
            print('Gold MiGs Setup Complete')
            whiteMigs.beginSetup()
        else:
            goldMigs.createMerchant(self, preAuth=True, completeGoldMigs=True)


class whiteMigs:
    @staticmethod
    def beginSetup(completePreAuth=False, completeSetup=None):

        if not completePreAuth:
            body = driver.find_element_by_tag_name("body")
            body.send_keys(Keys.CONTROL + 't')

        time.sleep(1)

        global accessCode, accessCode1
        driver.get('https://migs.mastercard.com.au/ma')
        if not completePreAuth:
            driver.maximize_window()

        loginElem = driver.find_element_by_id('ownerId')
        if completePreAuth:
            loginElem.send_keys(app.Entry3.get() + "_P")
        else:
            loginElem.send_keys(app.Entry3.get())
        loginElem = driver.find_element_by_id('userName')
        loginElem.send_keys('Administrator')
        loginElem = driver.find_element_by_id('password')
        loginElem.send_keys('----')
        loginElem = driver.find_element_by_class_name('Submitlogin')
        type(loginElem)
        loginElem.click()

        loginElem = driver.find_element_by_link_text('Admin')
        type(loginElem)
        loginElem.click()
        driver.implicitly_wait(3)

        loginElem = driver.find_element_by_link_text('Operators')
        type(loginElem)
        loginElem.click()
        driver.implicitly_wait(3)

        loginElem = driver.find_element_by_link_text('Create a new Merchant Administration Operator')
        type(loginElem)
        loginElem.click()
        driver.implicitly_wait(3)

        loginElem = driver.find_element_by_id('userName')
        loginElem.send_keys('appoperator')

        loginElem = driver.find_element_by_id('name')
        loginElem.send_keys('operator')

        loginElem = driver.find_element_by_id('password')
        loginElem.send_keys('----')

        loginElem = driver.find_element_by_id('repeatPassword')
        loginElem.send_keys('----')

        pageElem = driver.find_element_by_id('moto')
        type(pageElem)
        pageElem.click()

        if completePreAuth:
            pageElem = driver.find_element_by_id('capture')
            type(pageElem)
            pageElem.click()
        else:
            pageElem = driver.find_element_by_id('purchase')
            type(pageElem)
            pageElem.click()

        pageElem = driver.find_element_by_id('standAloneCapture')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_id('refund')
        type(pageElem)
        pageElem.click()

        driver.implicitly_wait(1)

        pageElem = driver.find_element_by_id('standAloneRefund')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_id('configure')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_id('agentAdmin')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_name('submit')
        type(pageElem)
        pageElem.click()

        driver.implicitly_wait(2)

        pageElem = driver.find_element_by_link_text('Logout')
        type(pageElem)
        pageElem.click()

        driver.implicitly_wait(2)

        loginElem = driver.find_element_by_id('ownerId')

        if completePreAuth:
            loginElem.send_keys(app.Entry3.get() + "_P")
        else:
            loginElem.send_keys(app.Entry3.get())

        loginElem = driver.find_element_by_id('userName')
        loginElem.send_keys('appoperator')
        passwordElem = driver.find_element_by_id('password')
        passwordElem.send_keys('----')
        loginElem = driver.find_element_by_class_name('Submitlogin')
        type(loginElem)
        loginElem.click()

        pageElem = driver.find_element_by_link_text('Admin')
        type(pageElem)
        pageElem.click()

        driver.implicitly_wait(2)

        pageElem = driver.find_element_by_partial_link_text('Configuration')
        type(pageElem)
        pageElem.click()

        if not completePreAuth:
            accessCode = driver.find_element_by_id('finTransResultaccessCode.value').text
        else:
            accessCode1 = driver.find_element_by_id('finTransResultaccessCode.value').text

        pageElem = driver.find_element_by_link_text('Operators')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_link_text('Edit')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_id('advanceMA')
        type(pageElem)
        pageElem.click()

        pageElem = driver.find_element_by_name('submit')
        type(pageElem)
        pageElem.click()

        if completePreAuth and completeSetup:
            notePad = Application()
            notePad.Start('notepad.exe')

            pyperclip.copy(
                "Please continue to the intranet and paste the appropriate variables \n\r " + "\n\r" + "Merchant ID:     " + app.Entry3.get() + "\n\r" + "Access Code:     " + accessCode + "\n\r" + "Password:     " + '---- \n\r'
                + "\n\r" + "Preauth details" + "\n\r" + "Merchant ID:     " + app.Entry3.get() +"_P" + "\n\r" + "Access Code:     " + accessCode1 + "\n\r" + "Password:     " + '----')
            spam = pyperclip.paste()
            notePad.notepad.edit.TypeKeys(spam, with_spaces=True)
            sys.exit()

        if not completePreAuth:
            pageElem = driver.find_element_by_link_text("Logout")
            type(pageElem)
            pageElem.click()
            whiteMigs.beginSetup(completePreAuth=True, completeSetup=True)


whiteMigsClass = whiteMigs()
goldMigsClass = goldMigs()

if __name__ == '__main__':
    root = tk.Tk()
    root.resizable(0, 0)
    app = Applications(root)
    root.mainloop()
