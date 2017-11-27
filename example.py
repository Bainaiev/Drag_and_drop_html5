from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://html5demos.com/drag#")
driver.set_script_timeout(10)

# load jQuery helper
with open("js/jquery_load_helper.js") as f:
    load_jquery_js = f.read()

# load drag and drop helper
with open("js/drag_and_drop_helper.js") as f:
    drag_and_drop_js = f.read()

# load jQuery
driver.execute_async_script(load_jquery_js)

# ready to rock
driver.execute_script("jQuery(function($) { " + " $('input[name=\"q\"]').val('bada-bing').closest('form').submit(); "
                    + " }); ")

source = "section#wrapper article ul li:nth-child(4) a"
target = "section#wrapper article div"

# perform drag&drop
java_script = drag_and_drop_js + "window.jQuery('" + source + "').simulateDragDrop({ dropTarget: '" + target + "'});"
driver.execute_script(java_script)

sleep(2)

source = "section#wrapper article ul li:nth-child(2) a"
java_script = drag_and_drop_js + "window.jQuery('" + source + "').simulateDragDrop({ dropTarget: '" + target + "'});"
driver.execute_script(java_script)

sleep(2)

source = "section#wrapper article ul li:nth-child(1) a"
java_script = drag_and_drop_js + "window.jQuery('" + source + "').simulateDragDrop({ dropTarget: '" + target + "'});"
driver.execute_script(java_script)


