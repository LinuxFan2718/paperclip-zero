from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#options = FirefoxOptions()
#options.add_argument("--headless")
#driver = webdriver.Firefox(options=options)

driver = webdriver.Firefox()
url = "https://www.decisionproblem.com/paperclips/index2.html"
driver.get(url)

makePaperclipButton = driver.find_element_by_id('btnMakePaperclip')
lowerPriceButton = driver.find_element_by_id('btnLowerPrice')
raisePriceButton = driver.find_element_by_id('btnRaisePrice')
expandMarketingButton = driver.find_element_by_id('btnExpandMarketing')
buyWireButton = driver.find_element_by_id('btnBuyWire')
allButtons = [ \
        makePaperclipButton, \
        lowerPriceButton, \
        raisePriceButton, \
        expandMarketingButton, \
        buyWireButton ]

numPaperclipsSpan = driver.find_element_by_id('clips')
availableFundsSpan = driver.find_element_by_id('funds')
unsoldInventorySpan = driver.find_element_by_id('unsoldClips')
pricePerClipSpan = driver.find_element_by_id('margin')
publicDemandSpan = driver.find_element_by_id('demand')
marketingLevelSpan = driver.find_element_by_id('marketingLvl')
marketingCostSpan = driver.find_element_by_id('adCost')
clipsPerSecondSpan = driver.find_element_by_id('clipmakerRate')
inchesOfWireSpan = driver.find_element_by_id('wire')
wireCostSpan = driver.find_element_by_id('wireCost')

def numFromSpan(element):
    return float(element.text)

def enabledButtons():
    return [button for button in allButtons if button.is_enabled()]


#import pdb; pdb.set_trace()
